from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
#temperature is creativity parameter...lower values means mode deterministic and predictable ans....
#if higher value the answer is more random and creative
#max tokens means kitne words me response chahie

model = ChatOpenAI(model = 'gpt-4', temperature=2 , max_completion_tokens=10)

result = model.invoke("What is the capital of India")


print(result)
#agar sirf result dekhna hai toh sirf result ki jagah result.content use krte