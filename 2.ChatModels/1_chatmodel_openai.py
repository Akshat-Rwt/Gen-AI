from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model ='gpt-4', temperature = 0.3 , max_completion_tokens=10)  # Temperature is used for the creative in the code if you want more create taks then make temp to 1 and if you want normal answer than make it 0.
# max_completion_tokens - Tokens means words basically So it will help you then you have a pricing model then you have a pay the bill as per your tokens / words.

result = model.invoke("What is the capital of India ?")
print(result.content) # Content is fetech from the result so it give you the answer

