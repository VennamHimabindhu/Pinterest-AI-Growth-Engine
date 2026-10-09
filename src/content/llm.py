import ollama

from src.content.models import PinterestContent
from src.content.context import build_content_context
from src.content.prompt import build_content_prompt
from src.content.validator import validate_content


def generate_content(prompt):
    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        format=PinterestContent.model_json_schema(),
    )

    content = PinterestContent.model_validate_json(
        response["message"]["content"]
    )

    return content


def generate_validated_content(opportunity):
    context = build_content_context(opportunity)
    prompt = build_content_prompt(context)
    content = generate_content(prompt)
    validation_result = validate_content(content, context)

    return {
        "content": content,
        "validation": validation_result,
    }


if __name__ == "__main__":
    opportunity = {
        "trend": "minimalist skincare",
        "board": "Skincare",
        "growth": 42,
        "goal": "increase_ctr",
    }

    result = generate_validated_content(opportunity)

    print("CONTENT:")
    print(result["content"])

    print("\nVALIDATION:")
    print(result["validation"])
