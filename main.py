from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS

load_dotenv()

# Load the document, split it into chunks, embed each chunk and load it into the vector store.
raw_documents = TextLoader('data/state_of_the_union.txt').load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
db = FAISS.from_documents(documents, OpenAIEmbeddings())

query = "What did the president say about Ketanji Brown Jackson"

docs = db.similarity_search(query)
print(docs[0].page_content)
