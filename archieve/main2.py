from langchain_core.prompts import PromptTemplate
from langchain_community.utilities import SQLDatabase
# to get ans in string format
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough 

# We use StrOutputParser to convert the model's output into a plain string 
# RunnablePassthrough to pass data through a step unchanged in a LangChain pipeline.

from langchain_ollama import OllamaLLM

db_uri = "mysql+mysqlconnector://root:sql%402005@localhost:3306/chinook"
db = SQLDatabase.from_uri(db_uri)
model = OllamaLLM(model="llama3.2")


# get schema of the  database, for the SQL query
def get_schema(_):
    return db.get_table_info()



# Prompt template
prompt = PromptTemplate.from_template(
    """Based on the database Schema below, write a SQL query to answer the user's question:
Schema:
{schema}
Question: {question}
SQL Query:"""
)

# building the chain
sql_chain = (
    RunnablePassthrough.assign(schema=get_schema)  # adds schema info to the input
    | prompt                                       # formats the prompt using input + schema
    | model.bind()                                 # prepares the model to be invoked.
    | StrOutputParser()                            # converts output to string.
)


#result = sql_chain.invoke({"question": "How many arists are there?"})
#print(result)

print("hii")

# Define your prompt template
prompt_template = PromptTemplate.from_template(
    "Given the following question: '{question}', please provide the answer."
)


# Format the prompt with the question
formatted_prompt = prompt_template.format(question="What's the capital of Punjab?")

# Run the model with the formatted prompt
response = model.invoke(formatted_prompt)

print(response)