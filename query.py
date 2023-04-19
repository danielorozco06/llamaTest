from llama_index import GPTSimpleVectorIndex, LLMPredictor, ServiceContext
from langchain.chat_models import ChatOpenAI
import os
import argparse

# set api key
os.environ["OPENAI_API_KEY"] = ''

# parse args
parser = argparse.ArgumentParser()
parser.add_argument('--query', type=str, help='Query to search')
args = parser.parse_args()

# define LLM
llm_predictor = LLMPredictor(llm=ChatOpenAI(
    temperature=0, model_name="gpt-3.5-turbo"))
service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

# load index vectors from disk
index = GPTSimpleVectorIndex.load_from_disk(
    'index/index_data.json', service_context=service_context)

# query
completion = index.query(args.query)
print(completion)
