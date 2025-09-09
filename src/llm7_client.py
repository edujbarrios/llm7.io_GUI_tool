"""
LLM7.io API Client

A Python client for interacting with the llm7.io API using OpenAI-compatible interface
"""
import openai
import os
import yaml
from typing import List, Dict, Optional, AsyncGenerator
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

class LLM7Client:
    """Client for interacting with llm7.io API"""
    
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None, config_path: Optional[str] = None):
        """
        Initialize the LLM7 client
        
        Args:
            api_key: API key for llm7.io (optional, can be set via env var)
            base_url: Base URL for the API (optional, can be set via env var)
            config_path: Path to configuration file (optional)
        """
        self.api_key = api_key or os.getenv("LLM7_API_KEY", "unused")
        self.base_url = base_url or os.getenv("LLM7_BASE_URL", "https://api.llm7.io/v1")
        
        # LLM7.io accepts "unused" for basic access without tokens
        if self.api_key == "unused":
            print("ℹ️  Using LLM7.io basic access (no tokens). For enhanced limits, get a free token from https://token.llm7.io")
        
        # Initialize OpenAI client with LLM7.io endpoint
        self.client = openai.OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )
        
        # Load models from config file if provided
        self.config = self._load_config(config_path)
        self.available_models = self.config.get('models', [])
    
    def _load_config(self, config_path: Optional[str] = None) -> Dict:
        """Load configuration from YAML file"""
        if not config_path:
            config_path = Path(__file__).parent.parent / "config" / "config.yaml"
        
        try:
            with open(config_path, 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except FileNotFoundError:
            # Fallback to hardcoded models if config file not found
            return {"models": self._get_default_models()}
    
    def _get_default_models(self) -> List[Dict]:
        """Get default model list as fallback"""
        return [
            {"id": "deepseek-r1-0528", "owned_by": "bedrock", "modalities": ["text"]},
            {"id": "gemini", "owned_by": "api.navy", "modalities": ["text"]},
            {"id": "mistral-small-3.1-24b-instruct-2503", "owned_by": "scaleway", "modalities": ["text"]},
            {"id": "nova-fast", "owned_by": "bedrock", "modalities": ["text"]},
            {"id": "gpt-4o-mini-2024-07-18", "owned_by": "azure", "modalities": ["text", "image"]},
            {"id": "gpt-4.1-nano-2025-04-14", "owned_by": "azure", "modalities": ["text", "image"]},
            {"id": "gpt-o4-mini-2025-04-16", "owned_by": "api.navy", "modalities": ["text"]},
            {"id": "qwen2.5-coder-32b-instruct", "owned_by": "scaleway", "modalities": ["text"]},
            {"id": "roblox-rp", "owned_by": "bedrock", "modalities": ["text"]},
            {"id": "bidara", "owned_by": "azure", "modalities": ["text", "image"]},
            {"id": "mirexa", "owned_by": "azure", "modalities": ["text", "image"]},
            {"id": "rtist", "owned_by": "azure", "modalities": ["text"]},
            {"id": "mistral-large-2411", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "codestral-2405", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "codestral-2501", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "ministral-3b-2410", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "ministral-8b-2410", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "mistral-large-2402", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "mistral-large-2407", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "mistral-medium", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "mistral-saba-2502", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "mistral-small-2402", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "mistral-small-2409", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "mistral-small-2501", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "mistral-small-2503", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "open-mistral-7b", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "open-mistral-nemo", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "open-mixtral-8x22b", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "open-mixtral-8x7b", "owned_by": "mistral", "modalities": ["text"]},
            {"id": "pixtral-12b-2409", "owned_by": "mistral", "modalities": ["text", "image"]},
            {"id": "pixtral-large-2411", "owned_by": "mistral", "modalities": ["text", "image"]},
            {"id": "deepseek-v3-0324", "owned_by": "nebulablock", "modalities": ["text"]},
            {"id": "deepseek-r1", "owned_by": "nebulablock", "modalities": ["text"]},
            {"id": "l3.3-ms-nevoria-70b", "owned_by": "nebulablock", "modalities": ["text"]},
            {"id": "midnight-rose-70b-v2.0.3", "owned_by": "nebulablock", "modalities": ["text"]},
            {"id": "l3-70b-euryale-v2.1", "owned_by": "nebulablock", "modalities": ["text"]},
            {"id": "l3-8b-stheno-v3.2", "owned_by": "nebulablock", "modalities": ["text"]},
            {"id": "qwen2.5-coder-7b", "owned_by": "nebius", "modalities": ["text"]},
        ]
    
    def get_models(self) -> List[Dict]:
        """Get list of available models"""
        return self.available_models
    
    def get_models_by_provider(self, provider: str) -> List[Dict]:
        """Get models filtered by provider"""
        return [model for model in self.available_models if model["owned_by"] == provider]
    
    def get_text_models(self) -> List[Dict]:
        """Get models that support text only"""
        return [model for model in self.available_models if "text" in model["modalities"]]
    
    def get_multimodal_models(self) -> List[Dict]:
        """Get models that support both text and images"""
        return [model for model in self.available_models if "image" in model["modalities"]]
    
    def get_providers(self) -> List[str]:
        """Get list of unique providers"""
        return list(set(model["owned_by"] for model in self.available_models))
    
    async def chat_completion(
        self, 
        model: str, 
        messages: List[Dict[str, str]], 
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        stream: bool = False
    ) -> Dict:
        """
        Send a chat completion request to llm7.io API
        
        Args:
            model: Model ID to use
            messages: List of message objects
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            stream: Whether to stream the response
            
        Returns:
            API response as dictionary
        """
        try:
            # Use OpenAI client synchronously (LLM7.io compatible)
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stream=stream
            )
            
            # Convert response to dictionary for compatibility
            return {
                "choices": [{
                    "message": {
                        "content": response.choices[0].message.content,
                        "role": "assistant"
                    }
                }],
                "usage": {
                    "total_tokens": getattr(response.usage, 'total_tokens', 0) if response.usage else 0
                }
            }
                
        except Exception as e:
            return {"error": f"API Error: {str(e)}"}
    
    async def stream_chat_completion(
        self, 
        model: str, 
        messages: List[Dict[str, str]], 
        temperature: float = 0.7,
        max_tokens: Optional[int] = None
    ) -> AsyncGenerator[str, None]:
        """
        Send a streaming chat completion request
        
        Args:
            model: Model ID to use
            messages: List of message objects
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            
        Yields:
            Streaming response chunks
        """
        try:
            # Use OpenAI client synchronously for streaming
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                stream=True
            )
            
            for chunk in response:
                if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
                    
        except Exception as e:
            yield f"Error: {str(e)}"
