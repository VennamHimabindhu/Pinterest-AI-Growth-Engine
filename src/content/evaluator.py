from src.content.models import PinterestContent


def evaluate_content(content: PinterestContent, context):
    scores = {}

    topic_words = set(context["topic"].lower().split())
    board_name = context.get("board_name", context.get("board", "")).lower()
    board_words = set(board_name.split())

    text = (
        content.title
        + " "
        + content.description
        + " "
        + content.cta
        + " "
        + " ".join(content.keywords)
        + " "
        + content.image_prompt
        + " "
        + content.visual_subject
        + " "
        + content.creative_strategy
    ).lower()

    # -----------------------------
    # 1. TOPIC RELEVANCE
    # -----------------------------

    topic_matches = sum(
        1 for word in topic_words
        if word in text
    )

    topic_relevance = (
        topic_matches / len(topic_words)
        if topic_words
        else 0.0
    )

    # -----------------------------
    # 2. BOARD RELEVANCE
    # -----------------------------

    board_matches = sum(
        1 for word in board_words
        if word in text
    )

    board_relevance = (
        board_matches / len(board_words)
        if board_words
        else 0.0
    )

    # Combine topic + board relevance
    scores["relevance"] = (
        topic_relevance * 0.60
        + board_relevance * 0.40
    )

    # -----------------------------
    # 3. COMPLETENESS
    # -----------------------------

    completeness_checks = [
        bool(content.title.strip()),
        bool(content.description.strip()),
        bool(content.keywords),
        bool(content.cta.strip()),
        bool(content.image_prompt.strip()),
        bool(content.visual_subject.strip()),
        bool(content.visual_hook.strip()),
        bool(content.composition.strip()),
        bool(content.camera_angle.strip()),
        bool(content.lighting.strip()),
        bool(content.color_palette.strip()),
        bool(content.background.strip()),
        bool(content.props.strip()),
        bool(content.style.strip()),
        bool(content.creative_strategy.strip()),
    ]

    scores["completeness"] = (
        sum(completeness_checks) / len(completeness_checks)
    )

    # -----------------------------
    # 4. OBJECTIVE ALIGNMENT
    # -----------------------------

    goal = context["goal"]

    if goal == "increase_ctr":
        if (
            len(content.title.strip()) > 0
            and len(content.cta.strip()) > 0
            and len(content.visual_hook.strip()) > 0
        ):
            scores["objective_alignment"] = 1.0
        else:
            scores["objective_alignment"] = 0.0

    else:
        scores["objective_alignment"] = 0.5

    # -----------------------------
    # 5. OVERALL SCORE
    # -----------------------------

    scores["overall"] = (
        scores["relevance"] * 0.40
        + scores["completeness"] * 0.30
        + scores["objective_alignment"] * 0.30
    )

    return scores


if __name__ == "__main__":

    content = PinterestContent(
        title="Minimalist Skincare Routine",
        description="A simple Korean skincare routine.",
        keywords=[
            "minimalist skincare",
            "Korean skincare",
        ],
        cta="Save this routine for later.",
        image_prompt="Minimalist Korean skincare products on a clean counter.",

        visual_subject="Minimalist Korean skincare routine",
        visual_hook="Close-up of a clean skincare arrangement",
        composition="Centered product arrangement with negative space",
        camera_angle="Slightly above eye level",
        lighting="Soft natural lighting",
        color_palette="Soft pink, white and pastel blue",
        background="Clean minimal background",
        props="Minimal skincare props",
        style="Modern minimalist editorial",
        text_placement="Negative space on the upper left",
        negative_constraints="No text, no pricing, no offers",

        objective="increase_ctr",
        evidence="Minimalist skincare has a 42% growth signal.",
        creative_strategy="Create a click-focused concept around minimalist Korean skincare.",
    )

    context = {
        "topic": "minimalist skincare",
        "board": "Skincare",
        "board_name": "Korean Skincare",
        "growth": 42,
        "goal": "increase_ctr",
    }

    result = evaluate_content(content, context)

    print(result)