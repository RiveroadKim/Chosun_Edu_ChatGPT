from langchain.chat_models import ChatOpenAI
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.callbacks import StreamingStdOutCallbackHandler
import os
from dotenv import load_dotenv, find_dotenv
from langchain.prompts.example_selector.base import BaseExampleSelector

_ = load_dotenv(find_dotenv())

chat = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.1,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()]
)

examples = [
    {
        "question": "What do you know about France?",
        "answer": """
        Here is what I know:
        Capital: Paris
        Language: French
        Food: Wine and Cheese
        Currency: Euro
        """,
    },
    {
        "question": "What do you know about Italy?",
        "answer": """
        I know this:
        Capital: Rome
        Language: Italian
        Food: Pizza and Pasta
        Currency: Euro
        """,
    },
    {
        "question": "What do you know about Greece?",
        "answer": """
        I know this:
        Capital: Athens
        Language: Greek
        Food: Souvlaki and Feta Cheese
        Currency: Euro
        """,
    },
]

# 1.RandomSelector 설계
class RandomExampleSelector(BaseExampleSelector):   #상속받음
    def __init__(self, examples):   # 객체 생성과 초기화
        self.examples = examples
    
    def add_example(self, example):
        self.examples.append(example)
    
    def select_examples(self, input_variables):
        from random import choice
        return [choice(self.examples)]

# 2.RandomSelector 생성
example_selector = RandomExampleSelector(examples=examples)

example_prompt = PromptTemplate.from_template(
    "Human: {question}\nAI:{answer}"
)

prompt = FewShotPromptTemplate(
    example_prompt=example_prompt,
    # examples=examples 전체 예제 모두 활용
    example_selector=example_selector, # 랜덤하게 예제 선택 활용
    suffix="Human: what do you know about {country}?",
    input_variables=["country"],
)

chain = prompt | chat
chain.invoke({
    "country": "Japan"
})
