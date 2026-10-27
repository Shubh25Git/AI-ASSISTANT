from openai import OpenAI
from dotenv import load_dotenv  # Loads environment variables from a .env file.
import os  # Provides functions to access environment variables and interact with the operating system.

load_dotenv() ## by default looks for .env file and load the all the values in the environment variable

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

response=client.chat.completions.create(   
    model=os.getenv("MODEL"),
    messages=[
        {
            "role":"user",
            "content":"Hello LLM"
        }
    ]
)

# print("LLM rsponse :",response) #==>ollama send response in json but opneai change that into python object 
print(response.choices[0].message.content)