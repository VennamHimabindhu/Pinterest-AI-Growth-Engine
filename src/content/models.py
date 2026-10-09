from pydantic import BaseModel


class PinterestContent(BaseModel):
    # Core Pinterest content
    title: str
    description: str
    keywords: list[str]
    cta: str

    # Image generation
    image_prompt: str

    # Advanced visual strategy
    visual_subject: str
    visual_hook: str
    composition: str
    camera_angle: str
    lighting: str
    color_palette: str
    background: str
    props: str
    style: str
    text_placement: str
    negative_constraints: str

    # Strategy and reasoning
    objective: str
    evidence: str
    creative_strategy: str


if __name__ == "__main__":

    content = PinterestContent(
        title="Minimalist Korean Skincare Routine",

        description=(
            "A simple Korean skincare routine "
            "for a clean and calming morning."
        ),

        keywords=[
            "korean skincare",
            "skincare routine",
            "morning skincare",
            "glass skin",
        ],

        cta="Save this routine for later.",

        image_prompt=(
            "A clean Korean skincare vanity with "
            "minimal skincare products and soft "
            "morning sunlight."
        ),

        visual_subject=(
            "Minimal Korean skincare products "
            "arranged on a clean vanity."
        ),

        visual_hook=(
            "A visually satisfying transformation "
            "from a simple setup to a complete skincare routine."
        ),

        composition=(
            "Vertical Pinterest composition with "
            "strong foreground subject, balanced negative "
            "space, and clear visual hierarchy."
        ),

        camera_angle=(
            "Slightly elevated three-quarter angle."
        ),

        lighting=(
            "Soft natural morning window light "
            "with subtle highlights."
        ),

        color_palette=(
            "White, cream, soft beige, and subtle pastel tones."
        ),

        background=(
            "Minimal clean bathroom vanity with "
            "softly blurred background."
        ),

        props=(
            "Minimal glass bottles, small towel, "
            "ceramic tray, and subtle botanical element."
        ),

        style=(
            "Premium editorial Korean beauty photography, "
            "clean, realistic, modern, and aesthetic."
        ),

        text_placement=(
            "Leave clean negative space in the upper "
            "left area for optional Pinterest text overlay."
        ),

        negative_constraints=(
            "No clutter, no distorted products, "
            "no extra objects, no excessive text, "
            "no unrealistic anatomy."
        ),

        objective="increase_ctr",

        evidence=(
            "Minimalist skincare has a 42% growth signal "
            "in the supplied trend data."
        ),

        creative_strategy=(
            "Create a click-focused Korean skincare concept "
            "with a premium minimalist visual identity."
        ),
    )

    print(content)