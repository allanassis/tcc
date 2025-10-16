
import logging
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv
from agno.agent import Agent

from src.llm_manager import LLMManager

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

llm_manager = LLMManager()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/atorak/chat/<model>', methods=['POST'])
def atorak_chat(model):
    try:
        data = request.json
        prompt = data.get('prompt', '')
        
        logger.info(f"ATORAK chat request for model: {model}")
        
        response_content = llm_manager.run_prompt(prompt, model)
        
        logger.info(f"ATORAK response generated successfully")
        return jsonify({'response': response_content, 'model': model, 'type': 'atorak'})
        
    except Exception as e:
        logger.error(f"Error in ATORAK chat: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/raw/chat/<model>', methods=['POST'])
def raw_chat(model):
    try:
        data = request.json
        prompt = data.get('prompt', '')
        
        logger.info(f"Raw chat request for model: {model}")
        
        # Create basic agent without ATORAK context
        provider = llm_manager.get_provider(model)
        agent = Agent(
            name="General Assistant",
            instructions="You are a helpful AI assistant.",
            model=provider
        )
        
        # Generate response
        response = agent.run(prompt)
        
        logger.info(f"Raw response generated successfully {response.to_dict()}")
        return jsonify({'response': response.content, 'model': model, 'type': 'raw'})
        
    except Exception as e:
        logger.error(f"Error in raw chat: {str(e)}")
        return jsonify({'error': str(e)}), 500
