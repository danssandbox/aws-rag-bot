# A Serverless RAG Chatbot Framework using AWS OpenSearch, AWS Bedrock and LangChain
This is a RAG chatbot application based on AWS components and designed to be optimized for a serverless architecture
and cost optimized for a high-volume mobile application use case.  The AWS Services being used are:
- AWS Bedrock with the Titan LLM and Titan embeddings 
- OpenSearch (aka Elasticsearch) vector database - this is instance based but can be serverless (not implemented yet)

The frameworks I created here abstract out a variety of components to enable easily testing variations.  This makes it easier to tune the implementation based on the 
content being use in my applications.  The goal is to play with different LLM's, different embeddings, parameters like temperature, top_p and more.
Content loading also needed to be highly refined allowing me to control each source easily.


## Features and aspects of interest
- **LangChain** - Great framework building Generative AI applications. 
- **LLM Model Support** - Defaults to AWS Bedrock Titan LLM, but supports other Bedrock models (LLama 2, Jurassic) OpenAI, Google Gemini
- **LangChain LLM Callbacks** - Example of using LLM Callbacks, provided here for custom costing 
- **Conversational Memory** -- Designed to manage chat history memory from the client side - to support a serverless model
- **OpenSearch** - an AWS hosted semantic search service which has a vector database that is valuable in the retrieval feature of RAG
- **Langchain LCEL Chains** - for more flexible chaining of steps in the RAG app
- **Multiple embedding models** - Defaults to Bedrock Titan, but supports OpenAI and Hugging Face
- **Web and directory crawlers** - for loading content into the vector DB.  Lots of fine-tuning to document selection features - whitelisting, black listing, etc.
- **Prompt library management** - making it easier to implement query routing to optimize for specific domains of questions
- **LangSmith logging** - for logging and debugging

## How to use
### Prerequisites
- AWS Account with keys defined in .env file (sample provided)
- OpenSearch Domain created and accessible
- AWS Bedrock with Titan Express LLM (or other LLM supported by this code)
- Ideally an LangChain (LangSmith) API Key defined in .env file (or removed if not using LangSmith)
- Python dependencies installed (dependency manager for this project coming soon)

### Sample Code
This is a very simple, high-level example.  Check out the rag_bot_code_samples.ipynb for a more.
First step is to have content in your vector database.  
```python
from open_search_vector_db.aws_opensearch_vector_database import OpenSearchVectorDBLoader
content_sources = [{"name": "Internal KB Docs", "type": "PDF", "location": "kb-docs"}]
vectordb_loader = OpenSearchVectorDBLoader(domain_name=my_open_search_domain_name,  
                                     index_name=my_index_name,
                                     data_sources=content_sources)

vectordb_loader.load()
```

Then you can start asking questions of it
```python
from rag_chatbot import RagChatbot, LlmModelTypes
from prompt_library import DefaultPrompts
chatbot = RagChatbot(my_open_search_domain_name,
                     LlmModelTypes.BEDROCK_TITAN_EXPRESS,
                     prompt_model=NasaSpokespersonPrompts)
chat_history = []
question = "What...?" # Ask a question related to the content you loaded

response = chatbot.ask_question(question, chat_history, verbose=True)
print(response)
```


### Running chatbot_client.py
A very simple command line client program has been created as an example and tool to test.  It is called chatbot_client.py.  
It is a simple command line program that will ask a question and then print the response while retaining the chat history for context.  

```bash
python chatbot_client.py my-opensource-domain-name
```

## References
**Vector Database:**  May references show using Chroma and FAISS, but I needed a solution that worked well in a Lambda serverless environment.  
Ideally it would be at AWS keeping my stack uniform.  
- https://aws.amazon.com/what-is/vector-databases/

Ultimately I chose OpenSearch because of cost, support by LangChain and a serverless version I plan to evaluate

**Vector Database Loader:**  LangChain has a great library of DataLoaders for loading data into OpenSearch.  I wanted an effective way
to scrape a website with help from this article chose to use Selenium.
- https://www.comet.com/site/blog/langchain-document-loaders-for-web-data/

I also used the directory loader and plan to implement cloud based directory loaders in the future.  Primarily S3 and Google Drive.

**Langsmith Logging and Debugging:**  I used LangSmith for logging and debugging.  It is a great tool for this purpose.
- https://docs.smith.langchain.com



### What's next (Roadmap):
1. Add Google Gemini, variants of OpenAI and variants of Bedrock
2. Add vector database stub for FAISS and easy testing
3. Expand range of support for Embeddings - including Hugging Face cloud service for embeddings
4. Leverage RAGAS for validation and to support heavy testing and tuning
