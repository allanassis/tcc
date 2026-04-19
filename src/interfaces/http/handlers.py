
import logging
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from dotenv import load_dotenv

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

@app.route('/generate', methods=['POST'])
def generate_readme():
    try:
        data = request.json
        url = data.get('url', '')
        model = data.get('model', 'gpt')

        if not url:
            return jsonify({'error': 'GitHub URL is required'}), 400

        logger.info(f"Generating README for: {url} using model: {model}")

        content = llm_manager.generate_doc(url, False, model)

        logger.info("README generated successfully")
        return jsonify({'response': content, 'model': model})

    except Exception as e:
        logger.error(f"Error generating README: {str(e)}")
        return jsonify({'error': str(e)}), 500
