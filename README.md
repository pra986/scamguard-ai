# ScamGuard AI : Scam Detection System

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-4285F4.svg)](https://ai.google.dev/)

An intelligent AI-powered system that uses Google's Gemini Large Language Model to detect and classify text messages as scam, legitimate, or uncertain. Built for educational purposes to demonstrate AI/ML concepts with production-ready architecture.

## Features

- **Multi-Strategy AI Detection**: Support for ReAct, Few-shot, Strict JSON, and Simplified prompting strategies
- **Web interface**: User-friendly Streamlit application for single message analysis
- **Batch Processing**: Efficient processing of large datasets with progress tracking
- **Comprehensive Evaluation**: Built-in evaluation tools with accuracy metrics
- **Robust Error Handling**: Retry mechanisms, fallback responses, and graceful degradation
- **Extensive Logging**: Detailed logging for debugging and monitoring
- **Modular Architecture**: Clean separation of concerns for maintainability and extensibility

## Installation

### Prerequisites

- Python 3.11 or higher
- Google API key for Gemini (get it from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/programteam-cn/Project-1-Scam_Detection.git
   cd Project-1-Scam_Detection
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root:

   ```env
   GEMINI_API_KEY=your_google_api_key_here
   ```

5. **Verify installation**

   ```bash
   python main.py
   ```

## Quick Start

### Single Message Detection

```python
from pipeline.scam_detector import ScamDetector

# Initialize detector
detector = ScamDetector()

# Analyze a message
result = detector.detect("Congratulations! You've won $1000. Click here to claim your prize!")

print(f"Classification: {result['label']}")
print(f"Confidence: {result['confidence']}")
print(f"Reasoning: {result['reasoning']}")
```

### Web Interface

```bash
cd streamlit
streamlit run app.py
```

### Batch Processing

```python
# Process multiple messages
messages = [
    "Your account will be suspended unless you verify immediately",
    "Meeting scheduled for 2 PM tomorrow",
    "URGENT: Click this link to claim your reward"
]

results = detector.detect_batch(messages, batch_size=10)
```

## Usage

### Command Line Interface

**Single Message Analysis:**

```bash
python main.py
# Enter your message when prompted
```

**Batch Evaluation:**

```bash
python evaluate.py path/to/dataset.csv
```

### Web Interface

1. Start the Streamlit app:

   ```bash
   cd streamlit
   streamlit run app.py
   ```

2. Open your browser to `http://localhost:8501`

3. Use the interface to:
   - Analyze single messages
   - Upload and evaluate CSV datasets
   - View detailed results and metrics

### Python API

```python
from pipeline.scam_detector import ScamDetector

# Initialize with different strategies
detector = ScamDetector(strategy="react")  # Default
detector = ScamDetector(strategy="fewshot")
detector = ScamDetector(strategy="strict_json")
detector = ScamDetector(strategy="simplified")

# Single message detection
result = detector.detect("Your message here")

# Batch processing
results = detector.detect_batch(messages, batch_size=10)

# Access results
print(f"Label: {result['label']}")
print(f"Confidence: {result['confidence']}")
print(f"Reasoning: {result['reasoning']}")
print(f"Risk Factors: {result['risk_factors']}")
```

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Required
GEMINI_API_KEY=your_google_api_key_here

# Optional Project-1-Scam_Detection- with defaults
DEFAULT_MODEL=gemini-2.5-flash
MAX_RETRIES=3
RETRY_DELAY=2
DEFAULT_BATCH_SIZE=10
STREAMLIT_BATCH_SIZE=5
```

### Dataset Format

CSV files should have the following structure:

```csv
text,label
"Congratulations! You've won $1000",Scam
"Meeting scheduled for tomorrow",Not Scam
"Click here to verify your account",Uncertain
```

Supported column names:

- **Text columns**: `text`, `message_text`, `message`
- **Label column**: `label`

### Prompt Strategy Configuration

Change the AI reasoning strategy by editing `llm/prompts.py`:

```python
# Line 17 - Change this to switch strategies
PROMPT = load_prompt("react.md")      # Step-by-step reasoning
PROMPT = load_prompt("fewshot.md")    # Example-based learning
PROMPT = load_prompt("strict_json.txt") # Clean JSON output
PROMPT = load_prompt("simplified.txt") # Quick classification
```

## Architecture

### System Overview

```markdown
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Input    │───▶│  Scam Detector  │───▶│    Results      │
│ (Web/CLI/API)   │    │    Pipeline     │    │  (JSON/UI)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   LLM Client    │
                    │ (Google Gemini) │
                    └─────────────────┘
```

### Core Components

- **`pipeline/scam_detector/`**: Main detection pipeline
  - `detector.py`: Orchestrates the entire process
  - `builder.py`: Builds prompts with different strategies
  - `executor.py`: Executes LLM calls with retry logic
  - `parser.py`: Parses and validates LLM responses

- **`llm/`**: LLM integration layer
  - `client.py`: Google Gemini API client
  - `prompts.py`: Prompt template management
  - `parser.py`: Response parsing utilities
  - `validator.py`: Output validation schemas

- **`streamlit/`**: Web interface
  - `app.py`: Streamlit web application

For detailed architecture documentation, see [ARCHITECTURE.md](ARCHITECTURE.md).

## Development

### Project Structure

```markdown
scam-detection/
├── llm/                   # LLM integration layer
│   ├── client.py          # Google Gemini API client
│   ├── prompts.py         # Prompt template management
│   ├── parser.py          # Response parsing
│   ├── validator.py       # Output validation
│   └── prompts/           # External prompt templates
├── pipeline/              # Core detection pipeline
│   └── scam_detector/     # Main detector module
├── streamlit/             # Web interface
├── config.py              # Configuration management
├── main.py                # CLI entry point
├── evaluate.py            # Evaluation tools
└── requirements.txt       # Dependencies
```

### Adding New Prompt Strategies

1. Create a new prompt file in `llm/prompts/`:

   ```bash
   touch llm/prompts/my_strategy.md
   ```

2. Define your prompt template:

   ```markdown
   # My Custom Strategy
   
   You are an expert scam detector...
   
   Message: {message}
   
   Analyze and respond with JSON...
   ```

3. Update `llm/prompts.py` to use your strategy:

   ```python
   PROMPT = load_prompt("my_strategy.md")
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
