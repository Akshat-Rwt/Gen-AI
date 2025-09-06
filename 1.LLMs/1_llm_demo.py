from langchain_openai import OpenAI     # From here langchain know about that they can connect with the openai 
from dotenv import load_dotenv          # It import the secret key form the enviroment to your current enviroment

load_dotenv()

llm = OpenAI(model = 'gpt-3.5-turbo-instruct')  # It's and object which tell which openAI model we want to connenct

result = llm.invoke("What is the capital of India")                            # Its an important function in langchain  - It help us to communicate with the gpt-3.4

print(result)