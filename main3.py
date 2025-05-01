from langchain_core.prompts import PromptTemplate
from langchain_community.utilities import SQLDatabase
# to get ans in string format
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough 

# We use StrOutputParser to convert the model's output into a plain string 
# RunnablePassthrough to pass data through a step unchanged in a LangChain pipeline.

# from langchain_ollama import OllamaLLM  # Don't use this since we're replacing LLM call

from openai import OpenAI
from env import key


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=key,
)

# DB connection
db_uri = "mysql+mysqlconnector://root:sql%402005@localhost:3306/chinook"
db = SQLDatabase.from_uri(db_uri)


# get schema of the  database, for the SQL query
def get_schema(_):
    return db.get_table_info()



# Prompt template
prompt = PromptTemplate.from_template(
    """Based on the database Schema below, write a SQL query to answer the user's question:
Schema:
{schema}
Question: {question}
now, just give me the SQL Query, nothing else, dont do any font highlighting, and no markdown syntax as well, just the query no explanation, just the query to execute. And make sure u dont hallucinate the column names, as it is."""
)


# build manual input using LangChain prompt template
question = "Give 5 youngest employees"
schema = get_schema(None)
final_prompt = prompt.format(schema=schema, question=question)


# model 
completion = client.chat.completions.create(
    extra_headers={
        "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional
        "X-Title": "<YOUR_SITE_NAME>",      # Optional
    },
    extra_body={},
    model="nvidia/llama-3.3-nemotron-super-49b-v1:free",
    messages=[
        {
            "role": "user",
            "content": final_prompt
        }
    ]
)

# Print result
query = completion.choices[0].message.content
ans = db.run(query)
print(ans)


