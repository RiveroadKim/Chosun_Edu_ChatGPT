from openai import OpenAI

client = OpenAI(api_key="")

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": ""},
    {"role": "user", "content": "클라우드 설명해줘."}
  ]
)

print(completion.choices[0].message)