# 🤖 Chatbot RAG - PPC de Licenciatura em Computação (UFRPE)

Este projeto implementa uma solução **Retrieval-Augmented Generation (RAG)** para responder perguntas com base no Projeto Pedagógico do Curso (PPC) de Licenciatura em Computação da UFRPE.

---

## 📚 Base utilizada

[PPC - Licenciatura em Computação](http://www.lc.ufrpe.br/sites/ww2.lc.ufrpe.br/files/PPC-LC-atualizao.pdf)

---

## 🚀 Tecnologias e Bibliotecas

- Python
- Streamlit
- PyMuPDF (extração de texto do PDF)
- NLTK (tokenização)
- BM25 (Rank-BM25)
- Transformers (HuggingFace)
- T5 Fine-tuned (pt-br)

---

## 📦 Estrutura do Projeto

```bash
rag_ppc/
├── app.py                      # Funções centrais: extração, BM25, resposta
├── data/
│   └── PPC-LC-atualizao.pdf    # Base de dados utilizada
├── notebooks/
│   └── analise_inicial.ipynb   # Análise exploratória dos dados
├── requirements.txt            # Dependências do projeto
├── README.md                   # Instruções do projeto
├── .gitignore
└── streamlit_app/
    └── chatbot_interface.py    # Interface do chatbot
