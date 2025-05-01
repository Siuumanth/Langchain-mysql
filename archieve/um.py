from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# Define your prompt template
prompt_template = PromptTemplate.from_template(
    "Given the following question: '{question}', please provide the answer."
)

# Instantiate the model
model = OllamaLLM(model="llama3.2")

# Format the prompt with the question
formatted_prompt = prompt_template.format(question="What's the capital of Punjab?")

# Run the model with the formatted prompt
response = model.invoke(formatted_prompt)

print(response)
