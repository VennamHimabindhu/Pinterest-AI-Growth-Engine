from src.content.models import PinterestContent


def validate_content(content: PinterestContent, context):
    errors = []

    if not content.title.strip():
        errors.append("Title is empty.")

    if not content.description.strip():
        errors.append("Description is empty.")

    if not content.keywords:
        errors.append("Keywords are missing.")

    if not content.cta.strip():
        errors.append("CTA is empty.")

    if not content.image_prompt.strip():
        errors.append("Image prompt is empty.")

    if not content.objective.strip():
        errors.append("Objective is empty.")

    if not content.evidence.strip():
        errors.append("Evidence is empty.")

    if not content.creative_strategy.strip():
        errors.append("Creative strategy is empty.")

    text = (
        content.title
        + " "
        + content.description
        + " "
        + content.cta
        + " "
        + content.image_prompt
    ).lower()

    topic = context["topic"].lower()

    if topic not in text:
        errors.append("Generated content does not clearly mention the target topic.")

    if "price" in text or "₹" in text or "$" in text:
        errors.append("Generated content may contain an unsupported price.")

    if "discount" in text or "% off" in text:
        errors.append("Generated content may contain an unsupported discount.")

    if "buy now" in text or "shop now" in text:
        errors.append("Generated content may contain an unsupported purchase CTA.")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
    }


if __name__ == "__main__":
    content = PinterestContent(
        title="Minimalist Skincare Routine",
        description="A simple skincare routine.",
        keywords=["skincare", "minimalist skincare"],
        cta="Save this for later.",
        image_prompt="Minimalist skincare products on a clean bathroom counter.",
        objective="increase_ctr",
        evidence="Minimalist skincare has a 42% growth signal in the supplied trend data.",
        creative_strategy="Create a click-focused concept around the growing skincare topic.",
    )

    context = {
        "topic": "minimalist skincare",
        "board": "Skincare",
        "growth": 42,
        "goal": "increase_ctr",
    }

    result = validate_content(content, context)
    print(result)
