#!/usr/bin/env python3

import sys
import argparse
from dotenv import load_dotenv

from src.llm_manager import LLMManager

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description='Generate API documentation using ATORAK principles')
    parser.add_argument('--path', help='The path of the package that you want to generate the doc. Could be github repo, local folder...', required=True)
    parser.add_argument('--local', help='Indicates if the package path you want to generate the documentation is locally or not', default=False)
    parser.add_argument('--model', default='gpt', choices=['gpt', 'gemini', 'bedrock'], 
                       help='LLM model to use (default: gpt)')
    
    args = parser.parse_args()
    
    try:
        llm_manager = LLMManager()

        response = llm_manager.generate_doc(args.path, args.local, args.model)

        print(response)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
