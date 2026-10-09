from src.content.context import build_content_context
from src.content.prompt import build_content_prompt
from src.content.llm import generate_content
from src.content.validator import validate_content
from src.content.evaluator import evaluate_content
from src.visual.generator import CloudImageGenerator

def run_content_pipeline(
    opportunity,
    board_context=None
):
    # Build context using BOTH opportunity + selected board context
    context = build_content_context(
        opportunity,
        board_context
    )

    prompt = build_content_prompt(context)

    content = generate_content(prompt)

    validation = validate_content(
        content,
        context
    )

    if not validation["valid"]:
        return {
            "status": "rejected",
            "context": context,
            "content": content,
            "validation": validation,
            "evaluation": None,
        }

    evaluation = evaluate_content(
        content,
        context
    )

    return {
        "status": "approved",
        "context": context,
        "content": content,
        "validation": validation,
        "evaluation": evaluation,
    }


if __name__ == "__main__":

    opportunity = {
        "trend": "minimalist skincare",
        "board": "Skincare",
        "growth": 42,
        "goal": "increase_ctr",
    }

    # Test board context
    board_context = {
        "board_id": "1119426119819648286",
        "board_name": "Korean Skincare",
        "board_description": "",
        "board_context": (
            "Create content specifically for the Pinterest board "
            "'Korean Skincare'. Keep the topic, wording, keywords, "
            "and visual direction relevant to this board."
        ),
    }

    result = run_content_pipeline(
        opportunity,
        board_context=board_context
    )

    print("STATUS:")
    print(result["status"])

    print("\nCONTEXT:")
    print(result["context"])

    print("\nCONTENT:")
    print(result["content"])

    print("\nVALIDATION:")
    print(result["validation"])

    print("\nEVALUATION:")
    print(result["evaluation"])