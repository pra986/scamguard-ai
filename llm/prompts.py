# llm/prompts.py
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))
from utils import load_file
# Directory paths
PROMPTS_DIR = Path(__file__).parent / "prompts"

# Load prompt templates from external files
def load_prompt(filename: str) -> str:
    """Load a prompt template from file."""
    return load_file(PROMPTS_DIR / filename)

# Available prompt templates
PROMPT = load_prompt("react.md") # <-- Edit this to use different prompts

def generate_prompt(user_input: str) -> str:
    """
    Generate a prompt for scam detection - choose your strategy here!
    
    Available strategies:
    - REACT_PROMPT: Step-by-step reasoning 
    - FEWSHOT_PROMPT: Learning from examples
    - STRICT_JSON_PROMPT: Clean JSON output
    - SIMPLIFIED_PROMPT: Quick classification
    
    Args:
        user_input: The message to analyze
        use_react: Legacy parameter, defaults to ReAct strategy
        
    Returns:
        A formatted prompt string ready for LLM execution
    """
    template = PROMPT
    return f"{template}\n\nUser Message:\n{user_input.strip()}"