# 🔍 Semantic Search App

This project is a simple **AI-powered** semantic search app built with [Sentence-BERT](https://www.sbert.net/).  
It finds the most relevant text passages based on a user query using **Natural Language Processing (NLP)** techniques.  
The AI model understands the *meaning* of text, not just keywords, and therefore produces more intelligent search results.

---

## 📂 Project Structure

```text
semantic-search-app/
├── data/                  # Text files for searching
│   ├── text.txt
│   └── it_security.txt
│
├── src/                   # Source code
│   ├── embedder.py        # Wrapper for Sentence-BERT embeddings
│   ├── search.py          # Semantic search with cosine similarity
│   └── main.py            # Simple CLI search engine
│
├── requirements.txt       # Python dependencies
└── README.md              # Project description
```

---

## ⚙️ Installation

1. Clone the project:

   ```bash
   git clone https://github.com/<your-repo>/semantic-search-app.git
   cd semantic-search-app
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Add a `text.txt` file to the `./data/` folder.  
   The project already includes a sample file (`text.txt`), which you can replace or extend with your own text.

---

## 🚀 Usage

Run a search from the project root:

```bash
python src/main.py
```

---

## 🧠 How the AI Works

This project uses **Sentence-BERT**, a type of **transformer-based AI model** (built on top of BERT, a state-of-the-art NLP model).  
Sentence-BERT is designed for **semantic similarity** tasks – meaning it can tell whether two pieces of text *mean the same thing*, even if they use different words.

Here’s what happens under the hood:

1. **AI Model (Sentence-BERT)**  
   - The text and user queries are converted into **embeddings**: numerical vector representations in a high-dimensional space.  
   - These embeddings capture semantic meaning, not just surface-level keywords.

2. **Similarity Measure (Cosine Similarity)**  
   - Once all texts are represented as vectors, we compute the **cosine similarity** between the query vector and the document vectors.  
   - A higher score (closer to `1.0`) means the AI judges the texts to be more semantically related.

This is what makes the search *AI-powered*: it uses a **pre-trained neural network model** to understand language meaning, instead of relying on keyword matching.

---

## 🌍 Language Support

The model **all-MiniLM-L6-v2** is **multilingual**, meaning it supports **Danish**, **English**, and many other languages.  
Simply add `.txt` files in your language of choice to the `data/` folder and the AI will make them searchable.

---

## 📊 Example

```text
🔍 Semantic Search App

Enter query (or 'quit' to exit): phishing

Top results:
- One of the most common threats is phishing... (score: 0.89)
- Security is not only about technology but also about people... (score: 0.72)
- Cybersecurity is about protecting data... (score: 0.66)
```
