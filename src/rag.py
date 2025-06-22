from nltk.tokenize import word_tokenize
from transformers import pipeline, AutoTokenizer
from rank_bm25 import BM25Okapi

def carregar_modelo(): #retorna modelo e tokenizer prontos pra usar
    nome = "pierreguillou/t5-base-qa-squad-v1.1-portuguese"
    tokenizer = AutoTokenizer.from_pretrained(nome)
    modelo   = pipeline("text2text-generation", model=nome)
    return modelo, tokenizer

def responder(pergunta, 
              bm25, 
              paragrafos, 
              modelo_e_tokenizer, 
              top_n=5, 
              max_context_tokens=400): # Adicione max_context_tokens
    modelo, tokenizer = modelo_e_tokenizer # Desempacote modelo e tokenizer

    tokens_pergunta = word_tokenize(pergunta.lower())
    documentos_recuperados = bm25.get_top_n(tokens_pergunta, paragrafos, n=top_n)

    contexto_final = []
    current_tokens = 0

    # Iterar sobre os documentos recuperados e adicionar ao contexto até atingir o limite de tokens
    for doc in documentos_recuperados:
        doc_tokens = tokenizer.encode(doc, add_special_tokens=False)
        if current_tokens + len(doc_tokens) > max_context_tokens:
            break

        contexto_final.append(doc)
        current_tokens += len(doc_tokens)

    contexto = " ".join(contexto_final)

    resposta = modelo(f"question: {pergunta} context: {contexto}", max_new_tokens=150, do_sample=False)

    return resposta[0]["generated_text"]