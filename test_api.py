#!/usr/bin/env python3
"""
Quick test script for LLM7.io API
"""
import openai
from dotenv import load_dotenv
import os

load_dotenv()

def test_llm7_api():
    """Test the LLM7.io API directly"""
    
    # Initialize OpenAI client with LLM7.io settings
    client = openai.OpenAI(
        base_url="https://api.llm7.io/v1",
        api_key="unused"
    )
    
    print("🧪 Testing LLM7.io API...")
    print(f"Base URL: https://api.llm7.io/v1")
    print(f"API Key: unused")
    
    try:
        # Test with models from the official example
        models_to_test = ["gpt-4.1-nano-2025-04-14", "gemini", "mistral-large-2411", "gpt-4"]
        
        for model in models_to_test:
            print(f"\n🔄 Testing model: {model}")
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": "¿Wha is the capital of Spain?"}
                    ]
                )
                
                print(f"✅ Model {model} worked!")
                print(f"Response: {response.choices[0].message.content}")
                break
            except Exception as model_error:
                print(f"❌ Model {model} failed: {str(model_error)}")
                continue
        
    except Exception as e:
        print(f"❌ General API error: {str(e)}")
        print(f"Error type: {type(e)}")

if __name__ == "__main__":
    test_llm7_api()
