from langchain.chat_models import ChatOpenAI
from langchain.prompts import load_prompt
from langchain.callbacks import StreamingStdOutCallbackHandler
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

prompt = load_prompt("./data.json")
# prompt = load_prompt("./data/yaml")

chat = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.1,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)
prompt.format(country="Japan")