"""
Simple Chainlit GUI Application for LLM7.io

Simplified version to avoid compatibility issues
"""
import chainlit as cl
import os
import sys
from pathlib import Path
from typing import List, Dict

# Add src directory to path for imports
sys.path.append(str(Path(__file__).parent))

from llm7_client import LLM7Client

# Global client instance
client = None

@cl.on_chat_start
async def start():
    """Function executed when chat starts"""
    global client
    
    try:
        client = LLM7Client()
        
        # Get available models
        models = client.get_models()
        text_models = client.get_text_models()
        multimodal_models = client.get_multimodal_models()
        providers = client.get_providers()
        
        # Welcome message
        welcome_msg = f"""
# 🤖 Welcome to LLM7.io GUI

🖤 **Dark theme enabled** | 📷 **Image uploads supported**

**Current model**: gpt-4.1-nano-2025-04-14 (supports images)

- Type any question or message
- **Upload files** by using the attachment button next to the message input
- **Change models: "use [model-name]" or "switch to [model-name]"**
- **View models: "show available models"**

Try uploading an image and asking about it! 🚀
        """
        
        await cl.Message(content=welcome_msg).send()
        
        # Store default settings
        cl.user_session.set("current_model", "gpt-4.1-nano-2025-04-14")
        cl.user_session.set("temperature", 0.7)
        cl.user_session.set("max_tokens", 1000)
        
    except Exception as e:
        error_msg = f"""
❌ **Error initializing client**: {str(e)}

Please check:
1. Your API key is set in the `.env` file  
2. The API key is valid and active
3. Your internet connection is working

**Configuration file**: `.env`
**Required variable**: `LLM7_API_KEY`
        """
        await cl.Message(content=error_msg).send()

@cl.on_message
async def main(message: cl.Message):
    """Main function that handles user messages"""
    global client
    
    if not client:
        await cl.Message(content="❌ Client not initialized. Please reload the page.").send()
        return
    
    user_input = message.content.lower()
    
    # Check if user wants to change model
    if user_input.startswith("use ") or "switch to" in user_input or "change model" in user_input:
        await handle_model_change(message.content)
        return
    
    # Check if user wants to see available models
    if "models" in user_input and ("show" in user_input or "list" in user_input or "available" in user_input):
        await show_available_models()
        return
    
    # Get user settings
    current_model = cl.user_session.get("current_model", "gpt-4.1-nano-2025-04-14")
    temperature = cl.user_session.get("temperature", 0.7)
    max_tokens = cl.user_session.get("max_tokens", 1000)
    
    # Get conversation history
    message_history = cl.user_session.get("message_history", [])
    
    # Handle images and text
    message_content = message.content
    images = []
    
    # Check if message has image attachments
    if message.elements:
        for element in message.elements:
            if hasattr(element, 'path') and element.path:
                # Convert image to base64 for multimodal models
                import base64
                with open(element.path, "rb") as img_file:
                    img_data = base64.b64encode(img_file.read()).decode()
                    images.append({
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{img_data}"
                        }
                    })
    
    # Prepare message content for API
    if images:
        # For multimodal models, use content array format
        user_message = {
            "role": "user",
            "content": [
                {"type": "text", "text": message_content}
            ] + images
        }
    else:
        # For text-only models, use simple string format
        user_message = {
            "role": "user",
            "content": message_content
        }
    
    # Add user message to history
    message_history.append(user_message)
    
    # Prepare message with typing indicator
    msg = cl.Message(content="")
    await msg.send()
    
    try:
        # Call llm7.io API
        response = await client.chat_completion(
            model=current_model,
            messages=message_history,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        if "error" in response:
            msg.content = f"❌ **Error**: {response['error']}"
            await msg.update()
            return
        
        # Extract assistant response
        assistant_response = response.get("choices", [{}])[0].get("message", {}).get("content", "No response received")
        
        # Update message with response
        msg.content = assistant_response
        await msg.update()
        
        # Add assistant response to history
        message_history.append({
            "role": "assistant", 
            "content": assistant_response
        })
        
        # Save updated history
        cl.user_session.set("message_history", message_history)
        
        # Add model info as a small note
        usage = response.get('usage', {})
        total_tokens = usage.get('total_tokens', 'N/A')
        
        info_msg = f"*Model: {current_model} | Tokens: {total_tokens} | Temp: {temperature}*"
        await cl.Message(content=info_msg, author="System").send()
        
    except Exception as e:
        msg.content = f"❌ **Unexpected error**: {str(e)}"
        await msg.update()

async def handle_model_change(user_input: str):
    """Handle model change requests"""
    global client
    
    # Extract model name from user input
    models = client.get_models()
    model_ids = [model['id'] for model in models]
    
    # Simple model name extraction
    found_model = None
    user_lower = user_input.lower()
    
    for model_id in model_ids:
        if model_id.lower() in user_lower:
            found_model = model_id
            break
    
    if found_model:
        cl.user_session.set("current_model", found_model)
        model_info = next((m for m in models if m['id'] == found_model), {})
        provider = model_info.get('owned_by', 'unknown')
        modalities = ', '.join(model_info.get('modalities', []))
        
        await cl.Message(content=f"""
✅ **Model changed successfully!**

- **Current Model**: {found_model}
- **Provider**: {provider}  
- **Modalities**: {modalities}

You can now continue chatting with the new model.
        """).send()
    else:
        await cl.Message(content=f"""
❌ **Model not found**

I couldn't find a model matching your request. 

Try saying: "show available models" to see all options.

**Popular models you can try:**
- use gemini
- use mistral-large-2411
- use codestral-2501
- use gpt-4o-mini-2024-07-18
        """).send()

async def show_available_models():
    """Show available models grouped by provider"""
    global client
    
    models = client.get_models()
    providers = {}
    
    # Group models by provider
    for model in models:
        provider = model["owned_by"]
        if provider not in providers:
            providers[provider] = []
        providers[provider].append(model)
    
    content = "# 📋 Available Models\n\n"
    
    for provider, provider_models in list(providers.items())[:5]:  # Limit to 5 providers to avoid long messages
        content += f"## {provider.title()}\n"
        for model in provider_models[:5]:  # Limit to 5 models per provider
            modalities = ", ".join(model["modalities"])
            content += f"- **{model['id']}** - {modalities}\n"
        content += "\n"
    
    content += "💡 **To switch models, just say**: \"use [model-name]\"\n"
    content += "📖 **For complete list**: Check the `models/models.md` file"
    
    await cl.Message(content=content).send()

# Chainlit configuration
if __name__ == "__main__":
    cl.run()
