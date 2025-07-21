# Ensuite - Study Buddy Module

## Prerequisites

- Python 3.10.11 or compatible version
  - You can install Python directly from [python.org](https://www.python.org/downloads/)
- Ollama for local LLM support
  - Install from [ollama.com](https://ollama.com/download)
  - Required models: llama3.1:8b

## Getting Started

1. Install Ollama:

Download and install from [ollama.com](https://ollama.com/download)

2. Pull required LLM model:

```bash
ollama pull llama3.1
```

3. Verify model installation:

```bash
ollama list
# Should show llama3.1:8b in the list
```

4. Check Python version:

```bash
python3 --version
# Should show Python 3.10.11 or compatible version
```

5. Set up Python environment:

```bash
# Create virtual environment
virtualenv .venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip3 install -r requirements.txt
```

6. Run the development server:

```bash
python3 manage.py runserver
```

This will start the application in development mode. The API will be available at the URL shown in the terminal (<http://localhost:8000/>).

7. When finished, deactivate the virtual environment:

```bash
deactivate
```
