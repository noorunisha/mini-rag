# Mini RAG Project

A simple Retrieval-Augmented Generation (RAG) project built with Python using local AI models.

## What is RAG?

RAG stands for Retrieval-Augmented Generation.

Instead of asking an AI model to answer only from its existing knowledge, RAG first retrieves relevant information from a knowledge source and then gives that information to the AI model to generate an answer.

## Project Workflow

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

## Tech Stack

- Python
- LangChain
- FAISS
- Hugging Face Sentence Transformers
- all-MiniLM-L6-v2
- Ollama
- Llama 3.2

## Example

### Question

What is Nisha trying to become?

### Retrieved Information

Nisha is learning Python and Generative AI.
She wants to become a Python AI developer.

### Answer

A Python AI developer.

## Key Concepts

- Document loading
- Text chunking
- Embeddings
- Vector search
- Similarity search
- Retrieval
- Context augmentation
- LLM generation
- Local LLMs

## Project Status

Completed successfully as a beginner RAG learning project.