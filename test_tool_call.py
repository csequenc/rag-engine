from dotenv import load_dotenv
from langchain_groq import ChatGroq

from framework_tools import rag_search

load_dotenv()

llm = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0.1
)

llm_with_tools = llm.bind_tools([rag_search])

response = llm_with_tools.invoke(
    "Summarize the uploaded documents."
)

print(response)
print(response.tool_calls)