from agno.agent import Agent

from agno.tools.file import FileTools

from agno.models.openai import OpenAIChat
from agno.models.google import Gemini

from src.context.main import ATORAK_CONTEXT

ATORAK_CONTEXT = """
You are an expert API documentation generator based on "A Theory of Robust API Knowledge" paper. 
Given the following instructions create a documentation based on the paper guidelines to create documentation.

""" + ATORAK_CONTEXT

class LLMManager:
    def __init__(self):
        self.providers = {
            'gpt': self._setup_openai,
            'gemini': self._setup_gemini,
        }
    
    def _setup_openai(self):
        return OpenAIChat(
            id="gpt-4.1-mini-2025-04-14",
        )
    
    def _setup_gemini(self):
        return Gemini(
            id="gemini-2.5-flash",
        )
    
    def get_provider(self, model_name):
        if model_name in self.providers:
            return self.providers[model_name]()
        raise ValueError(f"Unsupported model: {model_name}")

    def generate_doc(self, path, local, model):
        provider = self.get_provider(model)
        prompt = f"Generate API documentation for the package in the following address {path}. You can search on the web to understand what are the most importants parts to be added in the documentation."
        if local:
            prompt = f"Generate API documentation for the package located in the following directory {path}. Try to identify the public APIs of the package and the most important parts of these API to use in the documentation."

        prompt = prompt + "You MUST output ONLY the documentation in Markdown format, no more data."

        agent = Agent(
            name="API Documentation Generator",
            instructions=ATORAK_CONTEXT,
            model=provider,
            tools=[FileTools()]
        )
        response = agent.run(prompt)
        return response.content
    
    def run_prompt(self, prompt, model):
        provider = self.get_provider(model)
        agent = Agent(
            name="API Documentation Generator",
            instructions=ATORAK_CONTEXT,
            model=provider,
        )
        response = agent.run(prompt)
        return response.content
