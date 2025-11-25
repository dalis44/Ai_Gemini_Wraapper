
# AI Gemini Wrapper & Calculator Project

## Requirements
- Python 3.10+
- `uv` package manager (recommended)
- `google-generativeai` SDK
- `python-dotenv`

## Setup
```bash
uv init ai-agent
cd ai-agent
uv add google-genai python-dotenv
```

## Environment
Create a file named `prod.env`:
```
GEMINI_API_KEY="your-api-key"
```

## Run Gemini Agent
```bash
uv run main.py "What is the meaning of life?" --verbose
```

## Run Calculator
```bash
uv run calculator/main.py "3 + 5"
```

## Run Tests
```bash
uv run calculator/tests.py
```
