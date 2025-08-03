# 🗃 RAG - PPC de Licenciatura em Computação (UFRPE)

Este projeto implementa uma solução **Retrieval-Augmented Generation** para responder perguntas com base no Projeto Pedagógico do Curso de Licenciatura em Computação da UFRPE. O objetivo é fornecer respostas eficientes e precisas, combinando a recuperação de informações de um documento específico com a capacidade de geração de um modelo de linguagem.
---

## 📚 Base de Conhecimento Utilizada

O sistema RAG utiliza o seguinte documento como sua base de conhecimento:

* [**PPC - Licenciatura em Computação**](http://www.lc.ufrpe.br/sites/ww2.lc.ufrpe.br/files/PPC-LC-atualizao.pdf)

---

## ✨ Funcionalidades

- **📄 Extração de Texto**  
   Leitura e pré-processamento do conteúdo de um arquivo PDF.

-  **✂️ Chunking e Processamento**  
   Segmentação do texto em parágrafos/chunks, com sobreposição para preservar o contexto semântico.

- **🔍 Recuperação de Informação com BM25**  
   Indexação dos trechos utilizando o algoritmo BM25 para busca textual eficiente e relevante.

- **🧠 Geração de Respostas com LLMs**  
   Uso de modelos de linguagem baseados em transformadores  para gerar respostas a partir dos trechos recuperados.

-  **💬 Interface Interativa**  
   Interface de uso simples e acessível, com versões implementadas em:
   - `Streamlit` (para execução local)
   - `Gradio` (para deploy rápido e compartilhável)

---

## 🧱 Arquitetura
Nos baseamos em arquiteturas para construir o projeto, utilizando os dois fluxos abaixo como referenciais para nossas decisões.

  ![RAG Padrão](https://i.imgur.com/RjdXPvf.png)
---
![RAG BM25](https://i.imgur.com/ouTP7HW.png)

- A partir dessas ideias, implementamos um fluxo adaptado em que o documento PDF é carregado, seu conteúdo é extraído e segmentado em chunks textuais com sobreposição. 
- Diferente das abordagens com embeddings e bancos vetoriais, seguimos o caminho do TF-IDF para indexação lexical, e aplicamos o algoritmo BM25 para ranquear os trechos mais relevantes com base na consulta do usuário. 
- Essa estratégia permite recuperar os chunks mais próximos da pergunta de forma eficiente, sem necessidade de modelos de embeddings, mantendo a lógica geral do RAG e combinando o pré-processamento textual com modelos para resposta.

## 🚀 Tecnologias e Bibliotecas

Durante o desenvolvimento do projeto, foram aplicadas as seguintes tecnologias e bibliotecas Python:

* **Python**: Linguagem de programação principal.
* **Streamlit**: Framework para criação da interface web interativa do chatbot.
* **Gradio**: Biblioteca que permite a criação rápida e fácil de interfaces web interativas para deploy de modelos.
* **PyMuPDF (fitz)**: Utilizado para a extração eficiente de texto de arquivos PDF.
* **NLTK**: Kit de ferramentas de Processamento de Linguagem Natural, empregado para tokenização de texto.
* **Rank-BM25**: Implementação do algoritmo BM25 para a fase de recuperação de documentos (ranking de relevância).
* **Hugging Face Transformers**: Biblioteca para acesso e utilização de modelos de linguagem pré-treinados.

---

## 📦 Estrutura do Projeto

A organização do projeto segue uma estrutura modular para facilitar o desenvolvimento, a manutenção e a colaboração:

```bash
📁 data/
│   └── PPC-LC-atualizao.pdf           # Documento-base (PPC)
📁 notebook/
│   ├── [GRADIO]_PPC_t5_large.ipynb    # Demonstração com Gradio + Modelo T5-Large
│   ├── colab.ipynb                    # Código adaptado para Google Colab
│   ├── extracao_ementas_obrigatorias.ipynb # Exemplo que foi feito usando o Ementas Obrigatórias, mas que foi descontinuado por dificuldades.
│   └── ppc_extracao_indexacao.ipynb   # Extração + BM25
📁 src/
│   ├── __init__.py
│   ├── extract.py                     # Funções de extração de texto
│   ├── preprocessing.py               # Limpeza e chunking
│   └── rag.py                         # BM25 + integração com modelo
📁 streamlit_app/
│   └── rag_interface.py               # Interface com Streamlit + Modelo T5-Base de pierreguillou
├── app.py                             # Execução principal (opcional)
├── requirements.txt                   # Lista de dependências
└── README.md                          # Este arquivo
```
## ⚠ Dificuldades e Limitações

Durante o desenvolvimento do projeto, enfrentamos algumas dificuldades e encontramos diversas limitações.

A principal delas foi a escolha e comportamento dos modelos de linguagem. Testamos diferentes modelos, e nem todos conseguiam trazer as respostas certas com precisão, ou sequer mesmo alguma resposta cabível. Muitas vezes, o tempo de processamento era alto para obter uma resposta mais completa e contextualizada, e ainda assim o modelo podia apresentar alucinações — inserindo informações erradas ou incompletas, mesmo quando dávamos palavras-chave específicas. 

Também tivemos dificuldade com o deploy das interfaces. O Streamlit funcionou localmente sem muitos problemas, mas o Gradio, sempre que subíamos no Google Colab, apresentava erro ao tentar carregar o notebook já rodado. A solução foi deixar o notebook do Gradio salvo sem execução, apenas com uma imagem de referência para quando fosse baixado e testado. Para testar a aplicação, é necessário abrir o notebook manualmente no Colab, inserir o arquivo do PPC no ambiente, executar as células e acessar o link gerado.

Por fim, outro desafio foi ajustar o comportamento do modelo para tentar gerar respostas conversativas. O foco era que fosse recuperado trechos relevantes do documento de forma direta e correta, mas nem sempre foi possível, e em segundo plano, tentamos embelezar a contextualização, para trazer respostas seguidas de uma contextualização e em tom de conversa. Em vários casos, a resposta era apenas uma repetição do trecho recuperado, sem o nível de clareza ou elaboração que buscávamos, como vemos em ferramentas mais robustas como o ChatGPT, DeepSeek, Gemini etc.
