# AstraDB PDF LangChain Query Project

This project demonstrates the integration of various technologies to create a conversational AI system capable of querying document embeddings stored in AstraDB using natural language. The project utilizes LangChain for managing conversations and embedding queries, and Chroma for vector storage and retrieval.



## Introduction

The AstraDB PDF LangChain Query Project is designed to showcase the power of combining several modern technologies to build a sophisticated AI-based query system. The system leverages LangChain for conversation management, OpenAI for generating embeddings, Chroma for vector storage, and AstraDB for persisting and retrieving these embeddings.

## Technologies Used

- **LangChain**: A framework for building applications with large language models, used here for managing conversations and query logic.
- **OpenAI**: Provides the embedding function used to convert documents into vector representations.
- **Chroma**: A vector database used for efficient storage and retrieval of vector embeddings.
- **AstraDB**: A cloud-native database built on Apache Cassandra, used to store and manage the vector data.
- **Python**: The programming language used for implementing the project logic.

## Project Objective

The main objective of this project is to demonstrate how to build a conversational AI system that can:
1. Embed documents into vectors using OpenAI embeddings.
2. Store these vectors in a Chroma vector store.
3. Persist the vector data in AstraDB.
4. Retrieve and query the stored vectors using LangChain for natural language processing and conversation management.

## Setup

### Prerequisites

- Python 3.6+
- AstraDB Account
- OpenAI API Key

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/astra-langchain-query.git
   cd astra-langchain-query
