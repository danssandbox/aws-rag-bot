# A Serverless RAG Chatbot Application using AWS
This is a RAG chatbot application based on AWS components and designed to be optimized for a serverless architecture
and cost optimized for public application use.  The AWS Services being used are:
1. AWS Lambda
2. AWS Bedrock with the Titan LLM and Titan embeddings
3. OpenSearch (aka Elasticsearch) vector database - this is instance based but can be serverless



# Setup
- Uses python 3.11.6 (via pyenv and virtualenv)

## Features
- Uses LangSmith - for logging and debugging
- LangChain LLM Callbacks - for custom costing 
- Conversational Memory -- Designed to manage chat history memory from the client side - to support a serverless model
- OpenSearch - for vector database
- LLM Models - Defaults to AWS Bedrock Titan LLM, but supports other Bedrock models (LLama 2, Jurrasic) OpenAI, Google Gemini
- Package Management - Poetry for package management
- Model Evaluation - Ragas for RAG model evaluation
- Langchain LCEL Chains - for more flexible chaining
- Multiple embedding models - Defaults to Bedrock Titan, but supports OpenAI and Hugging Face
- Web and directory crawlers - for content retrieval.  Lots of fine tuning to document selection - whitelisting, black listing, etc.
- Prompt library management - with query routing to optimize for specific domains of questions


### TODO:
1. Add Google Gemini, variants of OpenAI and variants of Bedrock
2. Add vector database stub for FAISS
3. Add Huggingface service for embeddings?