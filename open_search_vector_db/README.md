## AWS OpenSearch Vector Database and LangChain
The aws_openssaerch_vector.py includes classes and utility functions that can make it easy to connect to
and load multiple content sources into an OpenSearch vector database.

This was created to support easy RAG application development

### Features
- This supports multiple embedding types
  - Bedrock (Titan)
  - OpenAI (default)
  - HuggingFace (default - local)
- It uses a list of source definitions to drive the loading process
   - Sources can be entire websites (or a list of URLs) and local files
   - The website can be a sitemap file and optional whitelist and blacklist specifications to control it

### How to use

#### Prerequisites

#### Sample Code
You can find some sample code in the [test_aws_opensearch_vector.py](test_aws_opensearch_vector.py) file.  
Here is a simple example to load a list of URLs into a vector database:
```python
from aws_opensearch_vector_database import OpenSearchVectorDBLoader

content_source = [{"name": "Reports", "type": "Website", "items": url_list}]

vectordb_loader = OpenSearchVectorDBLoader(domain_name='my-os-domain-name',  
                                     index_name='my-index-name',
                                     data_sources=content_sources)

vectordb_loader.load()
```
Then you can query it like this: 
```python
from aws_opensearch_vector_database import OpenSearchVectorDBQuery
vectordb = OpenSearchVectorDBQuery(domain_name='my-os-domain-name', index_name='my-index-name')
results = vectordb.query("semantic query text here")

```
#### Defining Data Sources
How the json works for loading

## Research References

## Basics of creating an AWS OpenSearch Vector Database
Need to define - just point to references I used


### TODO:
MVP
1. Edit for better and complete style (use GPT) - look at other refs
2. Add json structure for data sources
3. Add references (for creating search and using via LangChain)
4. Remove prereq for now and follow-up with it

Future
1. Finish whitelist and blacklist for directory loads
2. Add OpenSearch serverless to the class as an option
2. Add an S3 directory loader
3. Add a Google Drive loader
4. Clean-up Kustomer use of param store - use .env file instead
5. Create a simple test file to run through tests of mine... validating each major function


https://blog.langchain.dev/improving-document-retrieval-with-contextual-compression/

