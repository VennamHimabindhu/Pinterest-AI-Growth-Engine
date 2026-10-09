# Pinterest AI Growth Engine 🚀

**An AI-powered Pinterest content intelligence and publishing system that analyzes content opportunities, generates board-specific Pins, creates visuals, and publishes through the Pinterest API.**

The Pinterest AI Growth Engine is a Python-based project designed to automate and improve the Pinterest content workflow. It combines data analytics, rule-based scoring, Large Language Models (LLMs), structured content validation, image generation, and Pinterest API integration in a modular pipeline.

The goal is to build a feedback-driven system that helps creators identify promising content opportunities, generate relevant Pins, and improve future content using performance data.

> **Project status:** Core content and visual-generation pipelines implemented. Pinterest Sandbox publishing verified. Production access request pending Pinterest approval.

## ✨ Features

### 1. Pinterest API Integration
- Connects to the Pinterest API v5.
- Retrieves existing Pinterest boards.
- Supports OAuth-based authorization.
- Handles API responses and common request errors.
- Separates Sandbox testing from production publishing.

### 2. Content Intelligence and Analytics
- Calculates click-through rate (CTR), save rate, and engagement rate.
- Extracts useful performance features from Pin metrics.
- Identifies potential winners, laggards, and improvement opportunities.
- Uses scoring and ranking logic to prioritize content opportunities.
- Supports trend signals and board-relevance analysis.
- Includes baseline machine-learning experiments for classification and regression.

### 3. LLM-Powered Content Generation
- Uses a locally hosted Qwen 2.5 3B model through Ollama.
- Generates Pinterest titles, descriptions, keywords, calls to action, and creative strategies.
- Produces structured outputs using Pydantic schemas.
- Validates generated content before it proceeds through the pipeline.
- Evaluates topic relevance, completeness, and objective alignment.

### 4. Board-Aware Content Selection
- Retrieves existing Pinterest boards rather than creating a new board for every Pin.
- Scores board relevance against a content topic.
- Selects a suitable existing board.
- Passes board context into the content-generation pipeline.

### 5. Advanced Visual Generation
- Converts generated content into a structured visual specification.
- Defines the subject, visual hook, composition, camera angle, lighting, color palette, background, props, and negative constraints.
- Builds a detailed image-generation prompt.
- Uses the Pollinations image-generation API with the Flux model.
- Saves generated image assets locally for downstream use.

### 6. Pinterest Pin Publishing
- Combines a selected board, generated title, description, and image.
- Uses the Pinterest API to create Pins in the Sandbox environment.
- Keeps Sandbox and production credentials separate.
- Supports a production publisher configuration, subject to Pinterest app-access permissions.

### 7. Modular Architecture
- Separates Pinterest integration, content generation, visual generation, analytics, and publishing logic.
- Uses reusable Python modules instead of placing the entire workflow in one script.
- Supports incremental testing and extension.

## 🏗️ Architecture

```text
Pinterest Account
       |
       v
Pinterest API v5
       |
       v
Data Collection
       |
       v
Analytics and Feature Engineering
       |
       v
Scoring and Opportunity Detection
       |
       v
Existing Board Selection
       |
       v
Board-Aware Content Context
       |
       v
Ollama + Qwen 2.5 3B
       |
       v
Structured Content Generation
       |
       v
Validation and Evaluation
       |
       v
Visual Specification
       |
       v
Image Prompt Construction
       |
       v
Pollinations / Flux
       |
       v
Generated Image
       |
       v
Pinterest Sandbox Publisher
       |
       v
Pin Performance and Future Feedback
```

The feedback loop is the long-term objective: use performance data to improve opportunity ranking and future content decisions.

## 🛠️ Tech Stack

| Area | Technologies |
|---|---|
| Language | Python |
| LLM inference | Ollama, Qwen 2.5 3B |
| Structured output | Pydantic |
| Data processing | Pandas, NumPy |
| Machine learning | Scikit-learn |
| Image generation | Pollinations API, Flux |
| Pinterest integration | Pinterest API v5, OAuth 2.0 |
| HTTP requests | Requests |
| Configuration | python-dotenv |
| Testing | Python tests and module-level checks |

## 📁 Project Structure

```text
Pinterest-AI-Growth-Engine/
├── src/
│   ├── pinterest/
│   │   ├── client.py
│   │   ├── auth.py
│   │   ├── callback.py
│   │   ├── board_selector.py
│   │   ├── board_context.py
│   │   └── publisher.py
│   ├── content/
│   │   ├── models.py
│   │   ├── context.py
│   │   ├── prompt.py
│   │   ├── llm.py
│   │   ├── validator.py
│   │   ├── evaluator.py
│   │   └── pipeline.py
│   ├── visual/
│   │   ├── prompt.py
│   │   ├── generator.py
│   │   └── pipeline.py
│   ├── analytics/
│   └── affiliate/
├── tests/
├── generated_images/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

*The structure above describes the main modules; the exact files may evolve as development continues.*

## ⚙️ Getting Started

### Prerequisites

- Python 3.11 or newer, subject to dependency compatibility.
- Git.
- Ollama installed locally.
- A compatible Ollama model.
- A Pollinations API key for the configured image-generation service.
- A Pinterest Developer application for API integration.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Pinterest-AI-Growth-Engine.git
cd Pinterest-AI-Growth-Engine
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a virtual environment

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Ollama

Install Ollama, then pull the model used by the project:

```bash
ollama pull qwen2.5:3b
```

Ensure Ollama is running before executing the content pipeline.

### 5. Configure environment variables

Create a local `.env` file using `.env.example` as a template.

Example template:

```dotenv
PINTEREST_CLIENT_ID=your_client_id
PINTEREST_CLIENT_SECRET=your_client_secret
PINTEREST_REDIRECT_URI=http://localhost:8000/callback

PINTEREST_ACCESS_TOKEN=your_production_access_token
PINTEREST_REFRESH_TOKEN=your_refresh_token
PINTEREST_SANDBOX_ACCESS_TOKEN=your_sandbox_access_token

POLLINATIONS_API_KEY=your_pollinations_api_key
```

Use only the credentials required by the component being tested. Do not commit `.env` or share access tokens, refresh tokens, client secrets, or API keys.

### 6. Run the content pipeline

```bash
python -m src.content.pipeline
```

This runs the LLM-powered content-generation, validation, and evaluation flow.

### 7. Run the visual pipeline

```bash
python -m src.visual.pipeline
```

The visual pipeline retrieves existing boards, selects a relevant board, generates content with board context, constructs a visual specification, and requests image generation.

Generated images are saved under `generated_images/`.

### 8. Test board selection

```bash
python -m src.pinterest.board_selector
```

This retrieves existing boards and tests the current topic-to-board scoring logic.

### 9. Test Pinterest publishing

Use the Sandbox publisher and Sandbox board while developing. Confirm that the selected board ID belongs to the same environment as the API endpoint and access token.

Production publishing requires the appropriate Pinterest app access and production authorization. Never assume that having a `pins:write` token alone grants production Pin-creation access.

## 🔐 Security Notes

- Keep `.env` out of Git.
- Keep API keys, OAuth tokens, refresh tokens, and client secrets private.
- Use `.env.example` with placeholder values in the public repository.
- Do not expose credentials in screenshots, terminal recordings, logs, or README examples.
- Use separate Sandbox and production credentials.
- Review generated content before publishing it to a real account.
- Do not make unsupported product, medical, pricing, or performance claims.

## 🧪 Testing and Verification

The project has been exercised through module-level runs and an end-to-end Sandbox publishing flow.

Verified components include:

- Retrieval of existing Pinterest boards.
- Selection of a suitable board using topic relevance.
- Structured LLM output.
- Content validation and evaluation.
- Generation of structured visual specifications.
- Image generation through the configured cloud provider.
- Creation of a Pin in the Pinterest Sandbox environment.

Production Pin creation remains dependent on Pinterest approving the application's requested access tier.

## 🗺️ Roadmap

- [x] Local LLM integration
- [x] Structured content generation
- [x] Content validation and evaluation
- [x] Analytics and opportunity-scoring foundations
- [x] Existing-board selection
- [x] Board-aware content generation
- [x] Structured visual prompting
- [x] Cloud image generation
- [x] Sandbox Pin publishing
- [ ] Pinterest Standard access approval
- [ ] Production publishing verification
- [ ] Workflow orchestration, retries, and state management
- [ ] Automated scheduling where supported
- [ ] Performance feedback loop
- [ ] Improved experiments and model evaluation
- [ ] Deployment, monitoring, and cost optimization

## 🎯 Project Objective

Build an extensible AI-powered Pinterest growth system that connects analytics, opportunity detection, content generation, visual generation, publishing, and performance feedback into one workflow.

The long-term objective is to reduce repetitive content-production work while making content decisions more data-informed.

## ⚠️ Disclaimer

This project is a work in progress. Generated content and images can contain errors and should be reviewed before production use. API capabilities depend on Pinterest's current access policies and the permissions granted to the application.

## 👩‍💻 Author

**Himabindu Vennam**

AI/ML Engineering | Generative AI | Python | Machine Learning | API Integration
