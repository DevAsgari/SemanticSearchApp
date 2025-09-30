# 🔍 Semantic Search App

```text
🔍 Semantic Search App

Enter query (or 'quit' to exit): phishing

Top results:
- One of the most common threats is phishing... (score: 0.89)
- Security is not only about technology but also about people... (score: 0.72)
- Cybersecurity is about protecting data... (score: 0.66)
```

A prototype AI-powered search app that finds text based on meaning, not just keywords.  
Built with **Sentence-BERT** and **FAISS**, it turns text into vector embeddings and finds the passages that are semantically closest to your query.  
It’s a prototype showing how modern NLP can make search more accurate, flexible, and human-like. 

---

## 📂 Project Structure

```text
semantic-search-app/
├── data/                 # Text files for searching
│   └── text.md
│
├── src/                   # Source code
│   ├── embedder.py        # Wrapper for Sentence-BERT embeddings
│   ├── search.py          # Semantic search using FAISS
│   └── main.py            # Simple CLI search engine
│
├── requirements.txt       # Python dependencies
└── README.md              # Project description
```

---

## ⚙️ Installation

1. Clone the project:

```bash
git clone https://github.com/<your-repo>/SemanticSearchApp.git
cd SemanticSearchApp
```

2. Set up a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Add your text files to the `./data/` folder.
The repo comes with a sample text.md you can replace or extend.

## 🚀 Usage

Run a search from the project root:

```bash
python src/main.py
```

Type a query, and the app will return the passages it finds most semantically relevant.

---

## 🧠 How the AI Works

This app uses modern NLP and vector search to retrieve passages based on meaning rather than exact words. Here's how it works under the hood:

### 1. Embeddings (Sentence-BERT)
- Both the text passages and user queries are encoded into vectors using Sentence-BERT.
- These embeddings capture semantic meaning, so that even differently worded texts can be recognized as similar.

### 2. Vector Indexing (FAISS)
- All embeddings are stored in a FAISS index that enables fast and scalable similarity search.
- When a query is submitted, its embedding is compared to the stored ones to find the nearest matches.

### 3. Similarity Scores (cosine similarity)
- Each result includes a **similarity score**, calculated using **cosine similarity** between the query and each passage.
- A score close to **1.0** means high semantic overlap; a score closer to **0.0** means weak or no similarity.
- For example, `(score: 0.89)` means the model finds that result highly relevant to the query's meaning.

## 🛠️ Tech Stack
- Python
- HuggingFace Sentence-BERT
- FAISS for similarity search
- NLTK for text preprocessing

## ✨ Future Improvements
- Add a web interface to make the app easier to use
- Combine semantic search with a generative LLM to create full, natural language answers based on the most relevant passages.  
  Instead of just returning matching snippets, the model could generate helpful responses using the retrieved context.

## 🌍 Language Support
- Uses the multilingual model all-MiniLM-L6-v2, supporting Danish, English, and many other languages.

