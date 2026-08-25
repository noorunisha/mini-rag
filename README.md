# Mini RAG Project

A simple **Retrieval-Augmented Generation (RAG)** project built with Python using local AI models.

## What is RAG?

RAG stands for **Retrieval-Augmented Generation**.

Instead of asking an AI model to answer only from its existing knowledge, RAG first retrieves relevant information from a knowledge source and provides that information to the AI model as context. The model then uses that context to generate an answer.

## Project Workflow

```text
knowledge.txt
      ↓
Document Loading
      ↓
Text Chunking
      ↓
Embeddings
      ↓
FAISS Vector Store
      ↓
Similarity Search
      ↓
Relevant Context
      ↓
Ollama + Llama 3.2
      ↓
Final Answer
```

## Tech Stack

* Python
* LangChain
* FAISS
* Hugging Face Sentence Transformers
* all-MiniLM-L6-v2
* Ollama
* Llama 3.2

## How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Make sure Llama 3.2 is available through Ollama

```bash
ollama run llama3.2
```

### 3. Run the RAG application

```bash
python rag.py
```

### 4. Ask a question

When prompted with:

```text
Ask something:
```

enter your question.

## Example

### Question

```text
What is the difference between RAG and an AI agent?
```

### Retrieved Information

```text
RAG is primarily a method for retrieving relevant information
and providing it to an LLM as context.

An AI agent is a system that can reason about a goal,
choose actions, and use tools.
```

### Answer

```text
RAG is a method for providing context to an LLM,
while an AI agent is a system that can reason,
choose actions, and use tools to achieve a goal.
```

## Key Concepts

* Document loading
* Text chunking
* Embeddings
* Vector search
* Similarity search
* Retrieval
* Context augmentation
* LLM generation
* Local LLMs

## Project Status

Completed successfully as a **beginner RAG learning project**.

The application successfully loads a knowledge base, creates embeddings, performs similarity search using FAISS, retrieves relevant context, and generates answers using a local Llama 3.2 model through Ollama.
