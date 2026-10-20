import json
from openai import OpenAI

api_key = "123456"  # 如需鉴权填入真实 key，不需要则随便填非空值，无需鉴权
base_url = "http://112.17.28.80:8080/ac-health-open/health/ai/v1/chat/completions"
model_id = "medbench-agent-cn"
question = "请帮我分析一下高血压患者的日常饮食注意事项"

client = OpenAI(
    api_key=api_key,
    base_url=base_url,
)

completion = client.chat.completions.create(
    model=model_id,
    messages=[{"role": "user", "content": question}],
)

resp = json.loads(completion.model_dump_json())
answer = resp["choices"][0]["message"]["content"]
print(answer)
