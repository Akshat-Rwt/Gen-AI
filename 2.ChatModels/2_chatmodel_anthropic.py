from langchain_anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model = "Model link")
result = model.invoke("What is the capital of india")
print(result)

