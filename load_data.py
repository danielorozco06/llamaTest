from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
import os

# set api key
os.environ["OPENAI_API_KEY"] = ''

# load the .txt data and convert it into an index
documents_data = SimpleDirectoryReader('data').load_data()

# construct the index with the txt document
index_data = GPTSimpleVectorIndex.from_documents(documents_data)

# save index vectors to disk
index_data.save_to_disk('index/index_data.json')
