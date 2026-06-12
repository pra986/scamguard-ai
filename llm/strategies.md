# In prompt.py Load ALL your prompt files
REACT_PROMPT = load_prompt("react.md")
FEWSHOT_PROMPT = load_prompt("fewshot.md")
STRICT_JSON_PROMPT = load_prompt("strict_json.md")
SIMPLIFIED_PROMPT = load_prompt("simplified.md")

#Update generate_prompt to accept a strategy
def generate_prompt(user_input: str, strategy: str = "react") -> str:
    
    # Map strategy names to the prompt templates
    strategy_map = {
        "react":       REACT_PROMPT,
        "fewshot":     FEWSHOT_PROMPT,
        "strict_json": STRICT_JSON_PROMPT,
        "simplified":  SIMPLIFIED_PROMPT,
    }

    # Pick the right template, fall back to react if unknown
    template = strategy_map.get(strategy, REACT_PROMPT)
    
    return f"{template}\n\nUser Message:\n{user_input.strip()}"
#Update build_prompt.py to pass strategy through
    def build_prompt(message: str, strategy: str = "react") -> str:
    return generate_prompt(message, strategy)  # pass strategy along