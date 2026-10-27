from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

response=client.chat.completions.create(   
    model="qwen3:4b",
    messages=[
        {
            "role":"user",
            "content":"Hello LLM"
        }
    ]
)

# print("LLM rsponse :",response) #==>ollama send response in json but opneai change that into python object 
print(response.choices[0].message.content)