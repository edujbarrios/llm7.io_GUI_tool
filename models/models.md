# Available Models - LLM7.io

This document provides a comprehensive list of all models available through the LLM7.io API, organized by provider and category.

## Summary Statistics

- **Total Models**: 37
- **Text-only Models**: 35
- **Multimodal Models**: 12
- **Providers**: 7
- **Categories**: 10

---

## Models by Provider

### 🔶 Mistral AI (15 models)

Mistral AI is a French AI company focused on open and efficient language models.

#### General Purpose
- **mistral-medium** - Balanced performance model for general tasks
- **mistral-small-2402** - February 2024 version optimized for efficiency
- **mistral-small-2409** - September 2024 version with improvements
- **mistral-small-2501** - January 2025 latest version
- **mistral-small-2503** - March 2025 cutting-edge version

#### Reasoning
- **mistral-large-2411** - November 2024 large model for complex reasoning
- **mistral-large-2402** - February 2024 version for advanced tasks
- **mistral-large-2407** - July 2024 version with enhanced capabilities

#### Code Generation
- **codestral-2405** - May 2024 specialized coding model
- **codestral-2501** - January 2025 latest coding model

#### Compact Models
- **ministral-3b-2410** - 3B parameter compact model
- **ministral-8b-2410** - 8B parameter balanced compact model

#### Open Source
- **open-mistral-7b** - 7B open source base model
- **open-mistral-nemo** - Specialized open source model
- **open-mixtral-8x22b** - 8x22B mixture of experts
- **open-mixtral-8x7b** - 8x7B mixture of experts

#### Multimodal
- **pixtral-12b-2409** - 12B multimodal model (text + image)
- **pixtral-large-2411** - Large multimodal model (text + image)

#### Specialized
- **mistral-saba-2502** - February 2025 specialized model

---

### 🔷 Microsoft Azure (5 models)

Microsoft's cloud AI platform providing access to advanced models.

#### Multimodal
- **gpt-4o-mini-2024-07-18** - GPT-4 Omni mini with vision capabilities
- **gpt-4.1-nano-2025-04-14** - GPT-4.1 nano version with image support
- **bidara** - Specialized multimodal model
- **mirexa** - Advanced multimodal reasoning model

#### Creative
- **rtist** - Creative text generation model

---

### 🟠 Amazon Bedrock (3 models)

Amazon's managed AI service providing access to foundation models.

#### Reasoning
- **deepseek-r1-0528** - DeepSeek R1 optimized for reasoning tasks

#### General Purpose
- **nova-fast** - Fast inference model for quick responses

#### Gaming
- **roblox-rp** - Specialized for Roblox role-playing scenarios

---

### 🟣 NebulaBlock (6 models)

Specialized AI model provider with focus on fine-tuned models.

#### Reasoning
- **deepseek-v3-0324** - DeepSeek V3 March 2024 version
- **deepseek-r1** - DeepSeek R1 reasoning model

#### Creative
- **midnight-rose-70b-v2.0.3** - 70B creative writing model

#### Specialized
- **l3.3-ms-nevoria-70b** - Llama 3.3 MS Nevoria 70B specialized
- **l3-70b-euryale-v2.1** - Llama 3 70B Euryale v2.1

#### Compact
- **l3-8b-stheno-v3.2** - Llama 3 8B Stheno compact model

---

### 🔵 Scaleway (2 models)

European cloud provider offering AI services.

#### Instruction Following
- **mistral-small-3.1-24b-instruct-2503** - 24B instruction-tuned model

#### Code Generation
- **qwen2.5-coder-32b-instruct** - 32B programming specialist

---

### 🌊 API Navy (2 models)

API aggregation service providing access to various models.

#### General Purpose
- **gemini** - Google's Gemini model for conversations
- **gpt-o4-mini-2025-04-16** - OpenAI GPT-4 optimized mini

---

### ⭐ Nebius (1 model)

AI infrastructure and model provider.

#### Code Generation
- **qwen2.5-coder-7b** - 7B programming-focused model

---

## Models by Category

### 🧠 Reasoning (5 models)
High-performance models optimized for complex problem-solving and logical reasoning.

- deepseek-r1-0528 (Bedrock)
- mistral-large-2411 (Mistral)
- mistral-large-2402 (Mistral)
- mistral-large-2407 (Mistral)
- deepseek-v3-0324 (NebulaBlock)
- deepseek-r1 (NebulaBlock)

### 💻 Code Generation (4 models)
Specialized models for programming, code completion, and technical tasks.

- codestral-2405 (Mistral)
- codestral-2501 (Mistral)
- qwen2.5-coder-32b-instruct (Scaleway)
- qwen2.5-coder-7b (Nebius)

### 🎯 General Purpose (7 models)
Versatile models suitable for a wide range of conversational and text tasks.

- gemini (API Navy)
- gpt-o4-mini-2025-04-16 (API Navy)
- nova-fast (Bedrock)
- mistral-medium (Mistral)
- mistral-small-2402 (Mistral)
- mistral-small-2409 (Mistral)
- mistral-small-2501 (Mistral)
- mistral-small-2503 (Mistral)

### 🎨 Multimodal (6 models)
Models capable of processing both text and images.

- gpt-4o-mini-2024-07-18 (Azure)
- gpt-4.1-nano-2025-04-14 (Azure)
- bidara (Azure)
- mirexa (Azure)
- pixtral-12b-2409 (Mistral)
- pixtral-large-2411 (Mistral)

### 🎭 Creative (2 models)
Models optimized for creative writing and content generation.

- rtist (Azure)
- midnight-rose-70b-v2.0.3 (NebulaBlock)

### ⚡ Compact (3 models)
Smaller, efficient models optimized for speed and resource usage.

- ministral-3b-2410 (Mistral)
- ministral-8b-2410 (Mistral)
- l3-8b-stheno-v3.2 (NebulaBlock)

### 🔓 Open Source (4 models)
Open source models available for community use and modification.

- open-mistral-7b (Mistral)
- open-mistral-nemo (Mistral)
- open-mixtral-8x22b (Mistral)
- open-mixtral-8x7b (Mistral)

### 🎯 Specialized (2 models)
Models with specific domain expertise or fine-tuning.

- mistral-saba-2502 (Mistral)
- l3.3-ms-nevoria-70b (NebulaBlock)
- l3-70b-euryale-v2.1 (NebulaBlock)

### 📋 Instruction Following (1 model)
Models specifically fine-tuned to follow instructions precisely.

- mistral-small-3.1-24b-instruct-2503 (Scaleway)

### 🎮 Gaming (1 model)
Models specialized for gaming and role-playing scenarios.

- roblox-rp (Bedrock)

---

## Model Selection Guide

### For General Conversations
- **gemini** - Excellent for natural conversations
- **mistral-medium** - Balanced performance
- **nova-fast** - Quick responses

### For Complex Reasoning
- **mistral-large-2411** - Latest large model
- **deepseek-r1** - Specialized reasoning
- **deepseek-v3-0324** - Advanced reasoning

### For Programming Tasks
- **codestral-2501** - Latest coding model
- **qwen2.5-coder-32b-instruct** - Large coding model
- **qwen2.5-coder-7b** - Efficient coding model

### For Creative Writing
- **midnight-rose-70b-v2.0.3** - Creative storytelling
- **rtist** - Creative text generation

### For Multimodal Tasks
- **pixtral-large-2411** - Advanced vision capabilities
- **gpt-4o-mini-2024-07-18** - GPT-4 with vision
- **mirexa** - Advanced multimodal reasoning

### For Resource-Constrained Environments
- **ministral-3b-2410** - Smallest efficient model
- **ministral-8b-2410** - Balanced compact model
- **l3-8b-stheno-v3.2** - Compact specialized model

---

## Model Capabilities Matrix

| Model | Text | Image | Coding | Reasoning | Creative | Size |
|-------|------|-------|--------|-----------|----------|------|
| deepseek-r1-0528 | ✅ | ❌ | ✅ | ⭐⭐⭐ | ⭐⭐ | Large |
| gemini | ✅ | ❌ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | Medium |
| mistral-large-2411 | ✅ | ❌ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | Large |
| codestral-2501 | ✅ | ❌ | ⭐⭐⭐ | ⭐⭐ | ⭐ | Large |
| pixtral-large-2411 | ✅ | ✅ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | Large |
| gpt-4o-mini-2024-07-18 | ✅ | ✅ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | Medium |
| ministral-8b-2410 | ✅ | ❌ | ⭐ | ⭐⭐ | ⭐ | Small |

**Legend**: ⭐ = Basic, ⭐⭐ = Good, ⭐⭐⭐ = Excellent

---

## Provider Comparison

| Provider | Models | Strengths | Best For |
|----------|--------|-----------|----------|
| **Mistral AI** | 15 | Open source, efficiency, coding | Versatile applications |
| **Azure** | 5 | Multimodal, enterprise-grade | Business applications |
| **Bedrock** | 3 | Managed service, reliability | Production deployments |
| **NebulaBlock** | 6 | Specialized fine-tuning | Domain-specific tasks |
| **Scaleway** | 2 | European data sovereignty | EU compliance |
| **API Navy** | 2 | Model aggregation | Quick prototyping |
| **Nebius** | 1 | AI infrastructure focus | Development workflows |

---

## Usage Recommendations

### Development & Testing
- Start with **gemini** or **mistral-medium** for general tasks
- Use **ministral-8b-2410** for quick iterations
- Try **nova-fast** when speed is priority

### Production Deployment
- **mistral-large-2411** for complex reasoning
- **codestral-2501** for code-heavy applications
- **pixtral-large-2411** for multimodal needs

### Specialized Use Cases
- **Gaming/RP**: roblox-rp
- **Creative Writing**: midnight-rose-70b-v2.0.3
- **Code Generation**: qwen2.5-coder-32b-instruct
- **Multilingual**: gemini, mistral models

---

*Last updated: January 2025*
*Total models tracked: 37*
