# AI-Powered Code Assistant (Flask)

## Overview
This Flask-based API provides AI-powered coding assistance, including:
- Code autocompletion
- Code refactoring
- Error detection and auto-fixing
- Code summarization

The API utilizes OpenAI's GPT-4 model to analyze and improve code snippets.

## Features
- **Autocomplete**: Suggests next logical steps for a given code snippet.
- **Refactor**: Enhances code efficiency and readability.
- **Error Detection**: Identifies and fixes errors.
- **Summarization**: Provides a natural language explanation of the code.

## Prerequisites
- Python 3.7+
- OpenAI API Key
- Flask

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/code-assistant.git
   cd code-assistant
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your-api-key"  # On Windows use: set OPENAI_API_KEY="your-api-key"
   ```

## Running the Application
Start the Flask server:
```bash
python app.py
```
The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints
### 1. Autocomplete
- **Endpoint:** `/autocomplete`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "code": "print('Hello, world!')"
  }
  ```
- **Response:**
  ```json
  {
    "suggestions": "- Add user input handling..."
  }
  ```

### 2. Refactor Code
- **Endpoint:** `/refactor`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "code": "def add(a,b): return a+b"
  }
  ```
- **Response:**
  ```json
  {
    "refactored": "def add(a, b):\n    return a + b"
  }
  ```

### 3. Error Detection
- **Endpoint:** `/error-detection`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "code": "print('Hello, world'"
  }
  ```
- **Response:**
  ```json
  {
    "fixed_code": "print('Hello, world!')"
  }
  ```

### 4. Summarization
- **Endpoint:** `/summarize`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "code": "def greet(): print('Hello!')"
  }
  ```
- **Response:**
  ```json
  {
    "summary": "This function prints a greeting message."
  }
  ```
