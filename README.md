# API Documentation Agent

- Usar somente a parte da teoria robusta de API sobre domain, api e facts. Evitar usar o artigo completo para isso.
- Tunar o context do prompt, eliminando o nao necessário.
- Suportar URL's github/gitlab/bitbucket por exemplo
- Utilizar repos com um README.md bem escrito com uma boa documentacao
- Utilizar repos sem um README.md bem escrito com uma má documentacao
- Utilizar o GPT (provavelmente o mais utilizado)
-

A Flask-based web application that compares API documentation generation using "A Theory of Robust API Knowledge" (ATORAK) principles against raw LLM responses.

## Features

- **Dual Chat Interface**: Compare ATORAK-enhanced vs raw LLM responses side-by-side
- **Multi-LLM Support**: GPT, Gemini, Bedrock, and DeepSeek models
- **ATORAK Context**: Implements principles from "A Theory of Robust API Knowledge" paper
- **Simple UI**: Clean HTML/CSS/JavaScript interface
- **Extensible**: Easy to add new LLM providers

## Setup

1. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Keys**:

   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. **Set Environment Variables**:
   - `OPENAI_API_KEY`: OpenAI API key
   - `GOOGLE_API_KEY`: Google Gemini API key
   - `AWS_ACCESS_KEY_ID`: AWS access key for Bedrock
   - `AWS_SECRET_ACCESS_KEY`: AWS secret key for Bedrock
   - `AWS_REGION`: AWS region (default: us-east-1)
   - `DEEPSEEK_API_KEY`: DeepSeek API key

## Usage

### Web Interface

1. **Start Server**:

   ```bash
   python server.py
   ```

2. **Open Browser**: Navigate to `http://localhost:5000`

3. **Select Model**: Choose your preferred LLM from the dropdown

4. **Compare Responses**:
   - Left panel: ATORAK-enhanced documentation generation
   - Right panel: Raw LLM responses

### CLI Interface

1. **Direct CLI execution**:

   ```bash
   python cli.py "Your API documentation prompt" --model gpt
   ```

2. **Module execution**:

   ```bash
   python -m api-doc-agent "Your API documentation prompt" --model gemini
   ```

3. **Available models**: gpt, gemini, bedrock

## API Endpoints

- `GET /`: Main interface
- `POST /atorak/chat/<model>`: ATORAK-enhanced chat
- `POST /raw/chat/<model>`: Raw LLM chat
- `GET /models`: List available models

## ATORAK Principles

The ATORAK agent follows these key principles:

- **Completeness**: Document all endpoints and parameters
- **Consistency**: Uniform naming and response formats
- **Clarity**: Clear descriptions and examples
- **Correctness**: Accurate types and schemas
- **Context**: Authentication and usage guidelines
- **Comprehensiveness**: Edge cases and error handling

## Adding New LLM Models

1. Add provider setup method to `LLMManager` class
2. Update `providers` dictionary
3. Add model option to HTML select element
4. Configure required environment variables
