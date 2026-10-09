def build_visual_spec(image_prompt):
    return {
        "subject": image_prompt,
        "composition": "Clean, uncluttered composition with clear visual hierarchy.",
        "lighting": "Soft natural lighting.",
        "style": "Clean editorial lifestyle photography.",
        "mood": "Calm, minimal, and visually appealing.",
    }


if __name__ == "__main__":
    image_prompt = (
        "A minimalist skincare routine on a wooden table "
        "with clean glass bottles and a calm aesthetic."
    )

    visual_spec = build_visual_spec(image_prompt)

    print(visual_spec)