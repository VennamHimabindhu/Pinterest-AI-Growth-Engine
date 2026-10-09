import json
import ollama
from pydantic import BaseModel


# 1. Define the structure we expect from the LLM
class PinterestContent(BaseModel):
    title: str
    description: str
    keywords: list[str]
    cta: str
    image_prompt: str


# 2. Pinterest opportunity discovered by our analytics system
opportunity = """
   "topic": "Budget skincare",
    "board": "Skincare",
    "audience": "People looking for affordable skincare",
    "performance_signal": "Affordable skincare content is getting higher clicks",
    "goal": "Increase affiliate clicks"
"""


# 3. Give the opportunity to the LLM
prompt = f"""
We found this Pinterest opportunity:

{json.dumps(opportunity, indent=2)}

Create a Pinterest content strategy for this opportunity.

Rules:
- Do not invent products.
- Do not invent discounts.
- Do not claim something is free.
- Do not create fake affiliate links.
- Only use information provided in the opportunity.
- The goal is to create content that can eventually be published to Pinterest.

Return:
- title
- description
- keywords
- CTA
- image prompt
"""


# 4. Send the prompt to the local LLM
response = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {
        "role": "system",
        "content": """
You are a Pinterest content strategist.

Your job is to create accurate Pinterest content
based only on the information provided.

Rules:
- Do not invent products, offers, discounts, guides, or facts.
- Do not claim that something is free unless explicitly stated.
- Do not invent information that is not provided.
- The goal is to create useful, realistic Pinterest content.
"""
    },
    {
        "role": "user",
        "content": prompt
    }
    ],
    format=PinterestContent.model_json_schema(),
    options={
        "temperature": 0.7
    }
)


# 5. Validate the LLM's JSON output
content = PinterestContent.model_validate_json(
    response["message"]["content"]
)


# 6. Use the structured result in Python
print("\n--- PINTEREST CONTENT ---")

print("TITLE:", content.title)

print("DESCRIPTION:", content.description)

print("KEYWORDS:", content.keywords)

print("CTA:", content.cta)

print("IMAGE PROMPT:", content.image_prompt)