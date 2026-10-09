def build_visual_spec(content):
    return {
        "subject": content.visual_subject,
        "visual_hook": content.visual_hook,
        "composition": content.composition,
        "camera_angle": content.camera_angle,
        "lighting": content.lighting,
        "color_palette": content.color_palette,
        "background": content.background,
        "props": content.props,
        "style": content.style,
        "text_placement": content.text_placement,
        "negative_constraints": content.negative_constraints,
    }


def build_image_generation_prompt(visual_spec):
    return f"""
Create a high-quality Pinterest image.

SUBJECT:
{visual_spec["subject"]}

VISUAL HOOK:
{visual_spec["visual_hook"]}

COMPOSITION:
{visual_spec["composition"]}

CAMERA ANGLE:
{visual_spec["camera_angle"]}

LIGHTING:
{visual_spec["lighting"]}

COLOR PALETTE:
{visual_spec["color_palette"]}

BACKGROUND:
{visual_spec["background"]}

PROPS:
{visual_spec["props"]}

STYLE:
{visual_spec["style"]}

NEGATIVE SPACE:
Leave intentional clean negative space suitable for a future
Pinterest text overlay, but DO NOT render any text inside the image.

NEGATIVE CONSTRAINTS:
{visual_spec["negative_constraints"]}

Create a polished, realistic, visually coherent Pinterest-ready image.

Prioritize:
- strong visual hierarchy
- clear focal point
- scroll-stopping visual hook
- realistic objects
- clean composition
- intentional negative space
- cohesive colors
- professional editorial quality
- vertical Pinterest-friendly composition

Do not render text, letters, logos, watermarks, brand names,
prices, discounts, or promotional badges.

Do not invent recognizable brands or specific products.

Do not add unrelated objects.
""".strip()