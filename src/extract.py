import fitz  # PyMuPDF

def extrair_texto_pdf(caminho_pdf):
    doc = fitz.open(caminho_pdf)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    return texto

def preparar_paragrafos(texto, chunk_size=500, chunk_overlap=50):
    chunks = []
    for i in range(0, len(texto), chunk_size - chunk_overlap):
        chunk = texto[i:i + chunk_size]
        if len(chunk.strip()) > 50:
            chunks.append(chunk.strip())
    return chunks