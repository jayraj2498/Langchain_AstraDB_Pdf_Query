# In[ ]:
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import ConversationChain
from langchain.memory import VectorStoreRetrieverMemory

# Initialize the embedding function
embedding_func = OpenAIEmbeddings(openai_api_key='your_openai_api_key')

# Create and persist the Chroma vector store
db = Chroma(embedding_function=embedding_func, persist_directory="./chro_db")

# Convert the vector store to a retriever
retriever = db.as_retriever()

# Initialize the memory with the retriever
memory = VectorStoreRetrieverMemory(retriever=retriever)

# Create the conversation chain with memory
conversation = ConversationChain(llm=chat, memory=memory, verbose=True)

# Perform the conversation
print("First interaction:")
conversation.predict(input="hi my name is ironman")
print("Second interaction:")
conversation.predict(input="my favorite game is football")
print("Third interaction:")
conversation.predict(input="my favorite food is burger")
print("Fourth interaction:")
conversation.predict(input="my favorite country is France")
print("Fifth interaction:")
response = conversation.predict(input="what is my favorite game?")
print("Response:", response)

# Print the memory variables to check what is stored
# We need to provide the expected input key for load_memory_variables
input_key = "input"  # or whatever key the model is using for the main input
memory_variables = memory.load_memory_variables({input_key: "what is my favorite game?"})
print("Memory Variables:", memory_variables)


# Example of defining tools
def greet_tool(input_text):
    return f"Hello! You said: {input_text}"

tools = {"greet": greet_tool}

# Example of creating an agent
from langchain.agents import Agent, AgentExecutor

class MyAgent(Agent):
    def __init__(self, llm, tools, memory):
        super().__init__(llm, tools, memory)

    def decide_action(self, input_text):
        if "hello" in input_text.lower():
            return "greet"
        else:
            return None

agent = MyAgent(llm=llm, tools=tools, memory=memory)
agent_executor = AgentExecutor(agent=agent)

# Run the agent
input_text = "Hello, how are you?"
output = agent_executor.run(input_text)
print(output)  # Output: "Hello! You said: Hello, how are you?"

# Advanced agent example with multiple tools
def search_tool(input_text):
    return f"Search results for: {input_text}"

tools = {
    "greet": greet_tool,
    "search": search_tool
}

class AdvancedAgent(Agent):
    def __init__(self, llm, tools, memory):
        super().__init__(llm, tools, memory)

    def decide_action(self, input_text):
        if "hello" in input_text.lower():
            return "greet"
        elif "search" in input_text.lower():
            return "search"
        else:
            return None

advanced_agent = AdvancedAgent(llm=llm, tools=tools, memory=memory)
agent_executor = AgentExecutor(agent=advanced_agent)

input_text = "Please search for AI developments."
output = agent_executor.run(input_text)
print(output)  # Output: "Search results for: Please search for AI developments."

# Custom logic agent example
class CustomLogicAgent(Agent):
    def __init__(self, llm, tools, memory):
        super().__init__(llm, tools, memory)

    def decide_action(self, input_text):
        if "hello" in input_text.lower():
            return "greet"
        elif "search" in input_text.lower():
            return "search"
        else:
            return "default_response"

    def default_response(self, input_text):
        return "I'm not sure how to respond to that."

custom_agent = CustomLogicAgent(llm=llm, tools=tools, memory=memory)
agent_executor = AgentExecutor(agent=custom_agent)

input_text = "Tell me a joke."
output = agent_executor.run(input_text)
print(output)  # Output: "I'm not sure how to respond to that."
