# 🤖 Chatbot RAG - PPC de Licenciatura em Computação (UFRPE)

Este projeto implementa uma solução **Retrieval-Augmented Generation (RAG)** para responder perguntas com base no Projeto Pedagógico do Curso (PPC) de Licenciatura em Computação da UFRPE. O objetivo é fornecer respostas eficientes e precisas, combinando a recuperação de informações de um documento específico com a capacidade de geração de um modelo de linguagem.

---

## 👥 Integrantes

* **Caio César Farias da Silva**
* **Tarcísio Barbosa da Costa**
* **Victor Henrique dos Santos Oliveira** 


---

## 📚 Base de Conhecimento Utilizada

O sistema RAG utiliza o seguinte documento como sua base de conhecimento:

* [**PPC - Licenciatura em Computação**](http://www.lc.ufrpe.br/sites/ww2.lc.ufrpe.br/files/PPC-LC-atualizao.pdf)

---

## ✨ Funcionalidades

* **Extração de Texto**: Leitura e processamento do conteúdo do PDF do PPC.
* **Recuperação de Informações**: Utilização do algoritmo BM25 para encontrar os trechos mais relevantes do documento com base na pergunta do usuário.
* **Geração de Respostas**: Emprego de um modelo de linguagem grande (LLM) para formular respostas precisas e contextuais a partir dos trechos recuperados.
* **Interface Interativa**: Chatbot construído com Streamlit para uma experiência de usuário amigável.

---

## 🚀 Tecnologias e Bibliotecas

Este projeto foi desenvolvido utilizando as seguintes tecnologias e bibliotecas Python:

* **Python**: Linguagem de programação principal.
* **Streamlit**: Framework para criação da interface web interativa do chatbot.
* **PyMuPDF (fitz)**: Utilizado para a extração eficiente de texto de arquivos PDF.
* **NLTK**: Kit de ferramentas de Processamento de Linguagem Natural, empregado para tokenização de texto.
* **Rank-BM25**: Implementação do algoritmo BM25 para a fase de recuperação de documentos (ranking de relevância).
* **Hugging Face Transformers**: Biblioteca para acesso e utilização de modelos de linguagem pré-treinados.

---

## 📦 Estrutura do Projeto

A organização do projeto segue uma estrutura modular para facilitar o desenvolvimento, a manutenção e a colaboração:

```bash
rag_ppc/
├── app.py                      # Contém as funções centrais de processamento do PDF, configuração do BM25 e a lógica de interação com o LLM.
├── data/
│   └── PPC-LC-atualizao.pdf    # O arquivo PDF original que serve como base de conhecimento.
├── notebooks/
│   └── colab.ipynb             # Notebook Jupyter para a análise exploratória inicial dos dados e validação das etapas de pré-processamento.
├── requirements.txt            # Lista de todas as dependências Python necessárias para o projeto.
├── README.md                   # Este arquivo, contendo a descrição, instruções e detalhes do projeto.
├── .gitignore                  # Arquivo para especificar arquivos e diretórios a serem ignorados pelo Git.
└── streamlit_app/
    └── chatbot_interface.py    # O script principal que define e executa a interface do chatbot Streamlit.