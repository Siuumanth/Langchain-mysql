from openai import OpenAI

key = "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"


client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=key,
)

completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="nvidia/llama-3.3-nemotron-super-49b-v1:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)