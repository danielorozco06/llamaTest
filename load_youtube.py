from llama_index import GPTSimpleVectorIndex, download_loader
import os

# set api key
os.environ["OPENAI_API_KEY"] = ''

# create a youtube download loader object
YoutubeTranscriptReader = download_loader("YoutubeTranscriptReader")

# load the youtube_transcript reader
loader = YoutubeTranscriptReader()

# generate the index with the data in the youtube video
documents_youtube = loader.load_data(
    ytlinks=['https://www.youtube.com/watch?v=EYXQmbZNhy8'])


# construct the index with the Youtube document
index_youtube = GPTSimpleVectorIndex.from_documents(documents_youtube)

# save index vectors to disk
index_youtube.save_to_disk('index/index_youtube.json')
