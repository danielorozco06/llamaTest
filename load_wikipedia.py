from llama_index import GPTSimpleVectorIndex, download_loader
import os

# set api key
os.environ["OPENAI_API_KEY"] = ''

# create a wikipedia download loader object
WikipediaReader = download_loader("WikipediaReader")

# load the wikipedia reader object
loader = WikipediaReader()
documents = loader.load_data(pages=['Strawberry', 'Apple'])

# construct the index with the Wikipedia document
index_wikipedia = GPTSimpleVectorIndex.from_documents(documents)

# save index vectors to disk
index_wikipedia.save_to_disk('index/index_wikipedia.json')
