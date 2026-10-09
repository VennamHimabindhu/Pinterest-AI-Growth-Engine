def build_content_prompt(context):
    prompt = f"""
Create ONE Pinterest content candidate for the following opportunity.

TOPIC:
{context["topic"]}

TARGET BOARD:
{context.get("board_name", context["board"])}

BOARD CONTEXT:
{context.get("board_context", "Create content that is strongly relevant to the target board.")}

BOARD DESCRIPTION:
{context.get("board_description", "")}

TREND GROWTH:
{context["trend_growth"]}%

OBJECTIVE:
{context["goal"]}


CONTENT STRATEGY
Create an original Pinterest concept that:

- strongly matches the topic
- is specifically appropriate for the target board
- supports the stated objective
- uses the provided trend signal as evidence
- feels native to Pinterest
- has a clear visual hook
- is useful, saveable, or curiosity-driven
- does not feel generic

The selected board is important.

Do NOT create generic content that could belong to any Pinterest board.
The topic, wording, keywords, creative strategy, and visual concept
must all fit the selected board.


ADVANCED VISUAL STRATEGY

Design the visual concept specifically for Pinterest.

The image should have:

- a strong visual subject
- an immediate visual hook that can stop scrolling
- clear visual hierarchy
- intentional composition
- appropriate camera angle
- suitable lighting
- a coherent color palette
- a relevant background
- carefully selected props
- a consistent visual style
- intentional negative space
- a clear area where text could optionally be placed
- realistic and visually coherent objects

Prefer a vertical Pinterest-friendly composition.

The visual should communicate the Pin idea quickly even before
the viewer reads the title.


IMAGE PROMPT

Create a detailed image_prompt that describes the complete scene
for an image-generation model.

The image_prompt must incorporate:

- subject
- visual hook
- composition
- camera angle
- lighting
- color palette
- background
- props
- style
- text placement / negative space
- realistic visual constraints

Do not write a vague prompt such as:
"make a beautiful skincare image."

Instead describe the actual visual scene in detail.


SAFETY AND FACTUAL CONSTRAINTS
Do not use purchase-oriented CTAs such as:
- Shop now
- Buy now
- Shop our products
- Purchase this
- Get this product

unless actual product data or an affiliate link is provided.

For this stage, use informational or engagement CTAs such as:
- Save this routine for later
- Try this routine
- Learn the routine
- Save for your skincare board
- Discover the routine

Do not invent:

- products
- prices
- discounts
- offers
- statistics
- medical claims
- unsupported factual claims

Do not claim that a specific product exists unless it was provided
in the input context.

Return content for ONE Pin only.


The output must include EXACTLY these fields:

- title
- description
- keywords
- cta
- image_prompt
- visual_subject
- visual_hook
- composition
- camera_angle
- lighting
- color_palette
- background
- props
- style
- text_placement
- negative_constraints
- objective
- evidence
- creative_strategy

Make every field specific to the selected Pinterest board.
"""

    return prompt