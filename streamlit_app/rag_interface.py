import sys
import os

# Obter o caminho absoluto do diretório atual (streamlit_app)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Adicionar o diretório pai (rag_ppc) ao sys.path
parent_dir = os.path.join(current_dir, os.pardir)
sys.path.append(parent_dir)

import streamlit as st
from app import (
    extrair_texto_pdf,
    preparar_paragrafos,
    tokenizar_paragrafos,
    configurar_bm25,
    carregar_modelo,
    responder
)

import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")

# Carregar dados e modelo
caminho_pdf = os.path.join(parent_dir, "data", "PPC-LC-atualizao.pdf")
texto = extrair_texto_pdf(caminho_pdf)
paragrafos = preparar_paragrafos(texto)
tokenizados = tokenizar_paragrafos(paragrafos)
bm25 = configurar_bm25(tokenizados)

modelo, tokenizer = carregar_modelo()

# --- Configuração da Página ---
st.set_page_config(
    page_title="Chatbot RAG - PPC",
    layout="wide",
    initial_sidebar_state="collapsed"  # Pode ser útil para um chatbot
)

st.title("RAG - PPC Licenciatura em Computação (UFRPE)")
st.markdown("Faça uma pergunta sobre o Projeto Pedagógico do Curso de Licenciatura em Computação:")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

chat_placeholder = st.container(height=500)

with chat_placeholder:
    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

prompt = st.chat_input("Digite sua pergunta aqui...")

if prompt:
    # Adicionar a pergunta do usuário ao histórico
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # Adicionar a pergunta do usuário à interface imediatamente
    with chat_placeholder:
        with st.chat_message("user"):
            st.markdown(prompt)

    # --- Lógica de Geração da Resposta ---
    st.sidebar.markdown("---")  # Para depuração na sidebar
    st.sidebar.markdown("**DEBUG INFO:**")
    st.sidebar.markdown(f"Pergunta: {prompt}")

    tokens_pergunta_debug = word_tokenize(prompt.lower())
    documentos_recuperados_debug = bm25.get_top_n(tokens_pergunta_debug, paragrafos, n=5)

    contexto_final_debug = []
    current_tokens_debug = 0

    for doc in documentos_recuperados_debug:
        doc_tokens_debug = tokenizer.encode(doc, add_special_tokens=False)
        if current_tokens_debug + len(doc_tokens_debug) > 400:  # max_context_tokens
            break
        contexto_final_debug.append(doc)
        current_tokens_debug += len(doc_tokens_debug)

    contexto_para_modelo_debug = " ".join(contexto_final_debug)

    st.sidebar.markdown(f"Docs recuperados ({len(documentos_recuperados_debug)}):")
    for i, doc in enumerate(documentos_recuperados_debug[:3]):  # Mostra os 3 primeiros docs
        st.sidebar.text(f"Doc {i + 1}: {doc[:100]}...")
    st.sidebar.markdown(f"Contexto final (primeiros 200 chars): {contexto_para_modelo_debug[:200]}...")
    st.sidebar.markdown("---")

    # Gerar a resposta do chatbot
    with chat_placeholder:  # Mostra a resposta no placeholder do histórico
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):  # Indicador de carregamento
                resposta = responder(prompt, bm25, paragrafos, (modelo, tokenizer))
            st.markdown(resposta)

    # Adicionar a resposta do chatbot ao histórico
    st.session_state.chat_history.append({"role": "assistant", "content": resposta})
