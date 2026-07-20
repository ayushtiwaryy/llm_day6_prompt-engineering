import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key not found")
client = Groq(api_key = my_api_key)
model = "llama-3.3-70b-versatile"
role = "user"

prompt = """
#ROLE : 
You are a support assistant at a mobile/laptop service center
#TASK 
you have to classify the issue in category
#CONSTRAINT 
You have to classify the issue in any of the category that is BILLING,TECHNICAL,RETURN
#OUTPUT FORMAT 
Give output in one word only and from the options from the constraints only
#EXAMPLE 
For instance if a user complian says he wants a refund,then the category should be RETURN 
#FALLBACK 
If the issue is unrelated to any categories from the constraints , then the answer should be other.
This is a user complaint:
My phone is not working.I want refund
"""

message={
    "role":role,
    "content":prompt
}

messages = [message]



response = client.chat.completions.create(model=model,messages=messages)
print(response.choices[0].message.content)