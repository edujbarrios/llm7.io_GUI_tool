# Quick Start Guide

This document provides quick instructions to get the LLM7.io GUI up and running.

## Prerequisites

- Python 3.8 or higher
- Internet connection
- No API key required for basic usage!

## Starting the Application


```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate it
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Edit .env and set your LLM7_API_KEY or use "unused" for basic access

# 5. Run application
chainlit run src/app.py -w
```

## Configuration

Edit `.env` file:
```bash
LLM7_API_KEY=your_actual_api_key_here # unused by default
LLM7_BASE_URL=https://api.llm7.io/v1
```

## First Use

1. Application opens at `http://localhost:8000`
2. Select a model from the settings panel
3. Adjust temperature and max tokens as needed
4. Start chatting!

## Troubleshooting

- **"Import chainlit could not be resolved"**: Install dependencies first
- **"API key required"**: Set your API key in the `.env` file
- **"Connection error"**: Check internet connection and API status

For more details, see the main [README.md](../README.md) file.
