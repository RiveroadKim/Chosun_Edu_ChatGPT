from openai import OpenAI

client = OpenAI(api_key="")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "모든 설명을 3줄로 요약해서 설명해주세요."},
    {"role": "user", "content": "클라우드 설명해줘."}
  ]
)

print(completion.choices[0].message)

# OpenAI의 API를 사용한 챗봇 문제점
#   1. 개발이 어려움(난이도 상) -> 더 쉽게 개발 할 수 있는 ?(프레임워크) 필요!
#   2. 챗봇 개발 완성 -> Bard 모델 변경 -> Bard API 처음부터 개발!!! -> 프레임워크(LLM)

#   -> LangChain 프레임워크(코드 동일: 모델 바꾸면)