# pipeline/scam_detector/parser.py

from typing import Dict, Any
from utils import get_logger, extract_json_from_text

logger = get_logger(__name__)

class OutputParser:
    """Parses LLM output into structured format."""
    
    def parse_llm_output(self, llm_output: str) -> Dict[str, Any]:
        """
        Extract and parse JSON structure from LLM response.
        
        Args:
            llm_output: Raw text output from the LLM
            
        Returns:
            Dictionary containing structured detection results with keys:
            - label: str - Classification result ("Scam", "Not Scam", "Uncertain")
            - reasoning: str - Step-by-step analysis
            - intent: str - Description of user intent
            - risk_factors: List[str] - List of identified red flags
            
        Note:
            If parsing fails, returns a fallback dictionary with "Uncertain" label
            and error information in the reasoning field.
        """
        logger.info(f"Parsing LLM output of length: {len(llm_output)}")
        
        # Try to extract JSON using utils function
        parsed_json = extract_json_from_text(llm_output)
        
        if parsed_json:
            logger.info("Successfully parsed LLM output to JSON.")
            return parsed_json
        else:
            logger.warning("No JSON found in LLM output.")
            # Return fallback result
            fallback_result = {
                "label": "Uncertain",
                "reasoning": "Failed to parse response: No JSON found",
                "intent": "Could not determine",
                "risk_factors": []
            }
            return fallback_result 