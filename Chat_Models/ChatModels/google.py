from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model= ChatGoogleGenerativeAI(model = 'gemini-1.5-pro' , temperature=0.8)

result = model.invoke("write 5 line poem on frying pan")
print(result.content)
