from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0.3
)

prompt = ChatPromptTemplate.from_template(
    """
You are an expert teacher.
Explain th topic "{topic}" for a {level} level student.
Keep the explanation simple and minimal and include one real-life example.
"""
)

chain = prompt | llm

topic = input("Enter the topic:\n")

level = input("Enter level (Beginner\Intermediate\Advanced): ")

response = chain.invoke(
    {
        "topic": topic,
        "level": level
    }
)

print("\n")
print("AI Response")
print(response.content)