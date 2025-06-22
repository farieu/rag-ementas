import fitz  # PyMuPDF
import nltk
from nltk.tokenize import word_tokenize
from rank_bm25 import BM25Okapi
from transformers import pipeline, AutoTokenizer # Importe AutoTokenizer

nltk.download("punkt")
nltk.download('punkt_tab')

def extrair_texto_pdf(caminho_pdf):
    doc = fitz.open(caminho_pdf)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    return texto

def preparar_paragrafos(texto, chunk_size=500, chunk_overlap=50):
    # Adaptação mais robusta de chunking
    chunks = []
    for i in range(0, len(texto), chunk_size - chunk_overlap):
        chunk = texto[i:i + chunk_size]
        if len(chunk.strip()) > 50: # Mantém o filtro de tamanho mínimo
            chunks.append(chunk.strip())
    return chunks

def tokenizar_paragrafos(paragrafos):
    return [word_tokenize(p.lower()) for p in paragrafos]

def configurar_bm25(tokenizados):
    return BM25Okapi(tokenizados)

def carregar_modelo():
    # Carregue o tokenizer junto com o modelo para controle de tokens
    tokenizer = AutoTokenizer.from_pretrained("pierreguillou/t5-base-qa-squad-v1.1-portuguese")
    model_pipeline = pipeline("text2text-generation", model="pierreguillou/t5-base-qa-squad-v1.1-portuguese")
    return model_pipeline, tokenizer # Retorne ambos

def responder(pergunta, bm25, paragrafos, modelo_e_tokenizer, top_n=5, max_context_tokens=400): # Adicione max_context_tokens
    modelo, tokenizer = modelo_e_tokenizer # Desempacote modelo e tokenizer

    tokens_pergunta = word_tokenize(pergunta.lower())
    documentos_recuperados = bm25.get_top_n(tokens_pergunta, paragrafos, n=top_n)

    contexto_final = []
    current_tokens = 0

    # Iterar sobre os documentos recuperados e adicionar ao contexto até atingir o limite de tokens
    for doc in documentos_recuperados:
        # Codifique o documento para ver quantos tokens ele tem
        doc_tokens = tokenizer.encode(doc, add_special_tokens=False)

        # Se adicionar este documento exceder o limite, pare
        if current_tokens + len(doc_tokens) > max_context_tokens:
            break

        contexto_final.append(doc)
        current_tokens += len(doc_tokens)

    contexto = " ".join(contexto_final)

    resposta = modelo(f"question: {pergunta} context: {contexto}", max_new_tokens=150, do_sample=False)

    return resposta[0]["generated_text"]
