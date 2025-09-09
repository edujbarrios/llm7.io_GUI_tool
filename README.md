# [UNOFFICIAL] LLM7.io GUI with Chainlit

A modern and elegant graphical interface for interacting with **llm7.io** AI models using **Chainlit**.

**![STILL ON DEVELOPMENT](https://img.shields.io/badge/STILL%20ON%20DEVELOPMENT-0345fc?style=for-the-badge)**
**![ToDo: Improving UI](https://img.shields.io/badge/ToDo:%20IMPROVING%20UI-a903fc?style=for-the-badge)**

⭐ **Like the project?** Give it a star on GitHub!

Or... collaborate! Fork the repo, make changes, and submit a pull request.


## 🚀 What is this?

LLM7.io GUI is a conversational web interface that allows you to:

- **Chat with 37+ AI models** from providers like Mistral, Azure, Bedrock, NebulaBlock
- **Switch models in real-time** without restarting the application
- **Adjust parameters** (temperature, max tokens) on the fly
- **View detailed information** about token usage and model capabilities
- **Use multimodal models** that support both text and images


## 📖 Documentation

- **[📚 Quick Start Guide](docs/quick-start.md)** - Detailed installation instructions
- **[📋 Available Models](models/models.md)** - Complete list of 37 supported models

## 🎯 Key Features

- **Real-time model switching** - No need to restart
- **Parametrized configuration** - Everything in YAML files
- **Professional structure** - Well-organized codebase
- **Comprehensive documentation** - Guides for users and developers
- **Cross-platform scripts** - Works on Windows, Linux, and Mac

---
### ⚡ Fast Setup
````bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure environment
cp .env.example .env
# Edit .env and set your LLM7_API_KEY or use "unused" for basic access

# 3. Run application
chainlit run src/app.py -w
````

### 🔑 API Key Options

**Good news!** The app works immediately with basic access using `**"unused"**` as API key.

For enhanced limits, you can upgrade:
- **Free tokens**: Get from https://token.llm7.io for enhanced limits

Simply edit `.env` file:
```bash
LLM7_API_KEY=unused              # Basic access (current default)
LLM7_API_KEY=your_free_token     # Enhanced limits  
```

---

### About the GUI

This is the chosen pallete:

![#0B3D0B](https://img.shields.io/badge/-%230B3D0B-0B3D0B?style=for-the-badge&logoColor=white)
![#145214](https://img.shields.io/badge/-%23145214-145214?style=for-the-badge&logoColor=white)
![#1E6B1E](https://img.shields.io/badge/-%231E6B1E-1E6B1E?style=for-the-badge&logoColor=white)
![#2E8B2E](https://img.shields.io/badge/-%232E8B2E-2E8B2E?style=for-the-badge&logoColor=white)
![#45A845](https://img.shields.io/badge/-%2345A845-45A845?style=for-the-badge&logoColor=white)
![#6BCF6B](https://img.shields.io/badge/-%236BCF6B-6BCF6B?style=for-the-badge&logoColor=white)
![#A8E6A8](https://img.shields.io/badge/-%23A8E6A8-A8E6A8?style=for-the-badge&logoColor=black)
![#DFF8DF](https://img.shields.io/badge/-%23DFF8DF-DFF8DF?style=for-the-badge&logoColor=black)



By [Eduardo J. Barrios](https://edujbarrios.com)



