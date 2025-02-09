from flask import Flask, request, jsonify
import openai
import os
import logging
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

openai.api_key_path = os.getenv("/home/abhi/Documents/easygpt/.env")

def query_openai(prompt):
    """Helper function to query OpenAI API with proper error handling"""
    try:
        response = openai.ChatCompletion.create(  # ✅ Correct method
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        return response["choices"][0]["message"]["content"]  # ✅ Correct response format
    except openai.error.OpenAIError as e:
        logging.error(f"OpenAI API error: {e}")
        return f"OpenAI API Error: {e}"
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return f"Unexpected error: {e}"

def validate_code_input(code):
    """Validate input code parameter"""
    if not code or len(code.strip()) < 10:  # Basic length check
        return False
    if len(code) > 10000:  # Prevent excessively long inputs
        return False
    return True

@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    data = request.get_json()
    if not data or 'code' not in data:
        return jsonify({'error': 'Invalid request format'}), 400
    
    code_snippet = data['code']
    if not validate_code_input(code_snippet):
        return jsonify({'error': 'Invalid code provided'}), 400
    
    suggestion = query_openai(
        f'Provide 3 concise code suggestions for this code snippet. '
        f'Focus on next logical steps. Return as bullet points.\n\n{code_snippet}'
    )
    
    if not suggestion:
        return jsonify({'error': 'Failed to get suggestions'}), 500
    
    return jsonify({'suggestions': suggestion})

@app.route('/refactor', methods=['POST'])
def refactor_code():
    data = request.get_json()
    if not data or 'code' not in data:
        return jsonify({'error': 'Invalid request format'}), 400
    
    code = data['code']
    if not validate_code_input(code):
        return jsonify({'error': 'Invalid code provided'}), 400
    
    refactored_code = query_openai(
        f"Improve this code's efficiency and readability."
        f'Return only the refactored code without explanations.\n\n{code}'
    )
    
    if not refactored_code:
        return jsonify({'error': 'Failed to refactor code'}), 500
    
    return jsonify({'refactored': refactored_code})

@app.route('/error-detection', methods=['POST'])
def detect_errors():
    data = request.get_json()
    if not data or 'code' not in data:
        return jsonify({'error': 'Invalid request format'}), 400
    
    code = data['code']
    if not validate_code_input(code):
        return jsonify({'error': 'Invalid code provided'}), 400
    
    fixed_code = query_openai(
        f'Identify and fix errors in this code. '
        f'Return the corrected code first, followed by brief explanations.\n\n{code}'
    )
    
    if not fixed_code:
        return jsonify({'error': 'Failed to analyze code'}), 500
    
    return jsonify({'fixed_code': fixed_code})

@app.route('/summarize', methods=['POST'])
def summarize_code():
    data = request.get_json()
    if not data or 'code' not in data:
        return jsonify({'error': 'Invalid request format'}), 400
    
    code = data['code']
    if not validate_code_input(code):
        return jsonify({'error': 'Invalid code provided'}), 400
    
    summary = query_openai(
        f'Explain this code in natural language. '
        f'Keep the summary under 100 words.\n\n{code}'
    )
    
    if not summary:
        return jsonify({'error': 'Failed to generate summary'}), 500
    
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True, port=5000)