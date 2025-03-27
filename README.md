# Basic-RAG
used OpenAI to create a basic RAG system

# Use Case
Intelligent Document Query System
The Intelligent Document Query System is an advanced application designed to provide precise and contextually relevant information
retrieval from a variety of document formats. By integrating cutting-edge AI technology, this system can handle complex queries 
and return accurate responses based on the content stored in its document database.

# Overview
The system consists of several key components, each responsible for different aspects of document processing and 
query handling. These components are implemented across three main files: functions.py, create_database.py, and main.py.

Components
-----------

# functions.py

This file contains the core logic for processing user queries and generating responses using the AI model and the document database.

Constants:

CHROMA_PATH: Defines the directory path for the Chroma database.
DATA_PATH: Specifies the directory path where documents are stored.
Function predict:

Purpose: To handle user queries by searching the document database and generating a response.
Process:
Conducts a similarity search in the document database based on the query.
If no relevant results are found, returns a message indicating this.
Creates a prompt for the AI model using relevant document chunks.
Invokes the AI model to generate a response based on the constructed prompt.
Output: A formatted response from the AI model.


# create_database.py

This file manages the creation and maintenance of the document database. It handles loading documents, splitting text, 
and saving data to the Chroma vector store.

Constants:

CHROMA_PATH: Specifies the directory path for the Chroma database.
DATA_PATH: Defines the directory path where source documents are stored.
Function generate_data_store:

Purpose: To create and initialize the document database.
Process:
Loads documents from specified directories.
Splits the documents into smaller chunks.
Saves these chunks into the Chroma database.
Output: Returns the initialized document database object.
Function load_documents:

Purpose: To load documents from the specified directory.
Process:
Loads CSV, Excel, and PDF files from the data directory.
Uses appropriate loaders to read and split documents into smaller segments.
Output: A list of document segments.
Function split_text:

Inputs: A list of document objects.
Purpose: To split loaded documents into manageable text chunks.
Process:
Uses a recursive character text splitter to divide documents while maintaining context.
Output: A list of text chunks.
Function save_to_chroma:

Inputs: A list of document chunks.
Purpose: To save the text chunks into the Chroma vector database.
Process:
Creates a new Chroma database.
Adds document chunks to the database in batches.
Saves the database to the specified directory.
Output: Returns the document database object.


# main.py

The main.py file serves as the entry point for the Intelligent Document Query System, setting up and running the FastAPI web application. This file is responsible for initializing the AI model and document database, defining the API endpoints, and handling incoming user queries.

Key Components
Imports:

FastAPI: A modern, fast (high-performance), web framework for building APIs with Python.
CORSMiddleware: Middleware for handling Cross-Origin Resource Sharing (CORS), allowing secure cross-origin requests.
BaseModel from pydantic: Used for data validation and settings management using Python type annotations.
ChatOpenAI from langchain_openai: Facilitates interaction with OpenAI's language models.
Functions generate_data_store from create_database and predict from functions.
Global Variables:

llm: An instance of the ChatOpenAI model.
db: The document database object created by generate_data_store.
Class User:

Represents a user session, initializing a new instance of the AI language model for each user.
Class ChatInput:

A pydantic model that defines the structure of the input data for the chat endpoint. It contains a single field, Question, which holds the user's query.
Middleware:

CORS Middleware: Configures the application to allow secure cross-origin requests from any origin. This is essential for enabling the API to be accessed from different domains.
API Endpoint:

Endpoint /chat:
Method: POST
Input: An instance of ChatInput containing the user's query.
Process:
Calls the predict function with the user's query, the AI model instance (llm), and the document database (db).
Generates a response based on the relevant document chunks retrieved and the AI model's processing.
Output: Returns the generated response to the user in a structured format.
Application Execution:

Uses uvicorn to run the FastAPI application, making it accessible on the specified host and port. This allows the API to listen for and respond to user requests.



