import os
import google.generativeai as genai
from dataclasses import dataclass
from typing import Optional, Tuple
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@dataclass
class HealthMetrics:
    """Dataclass to store crop health metrics"""
    soil_health: float  # 0-100
    water_management: float  # 0-100
    pest_presence: float  # 0-100
    nutrient_levels: float  # 0-100

class CropHealthAnalyzer:
    def __init__(self):
        """Initialize the Gemini API connection"""
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable is not set")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
        self.recommendation_prompt = """As an agricultural expert, analyze these crop health metrics:
        
        Soil Health: {soil_health}/100
        Water Management: {water_management}/100  
        Pest Control: {pest_presence}/100
        Nutrient Levels: {nutrient_levels}/100
        
        Provide:
        1. Overall health assessment
        2. Specific improvement recommendations
        3. Priority actions
        Give practical advice farmers can implement immediately."""

    def calculate_overall_score(self, metrics: HealthMetrics) -> float:
        """Calculate weighted average health score"""
        weights = {
            'soil_health': 0.3,
            'water_management': 0.25,
            'pest_presence': 0.2,
            'nutrient_levels': 0.25
        }
        return (
            metrics.soil_health * weights['soil_health'] +
            metrics.water_management * weights['water_management'] +
            metrics.pest_presence * weights['pest_presence'] +
            metrics.nutrient_levels * weights['nutrient_levels']
        )

    def get_score_status(self, score: float) -> str:
        """Classify health score into status category"""
        if score >= 80:
            return "Excellent"
        elif score >= 60:
            return "Good"
        elif score >= 40:
            return "Fair"
        else:
            return "Poor"

    def get_health_recommendations(self, metrics: HealthMetrics) -> Tuple[Optional[str], Optional[str]]:
        """Get AI-powered recommendations for crop health improvement"""
        try:
            prompt = self.recommendation_prompt.format(
                soil_health=metrics.soil_health,
                water_management=metrics.water_management,
                pest_presence=metrics.pest_presence,
                nutrient_levels=metrics.nutrient_levels
            )
            
            response = self.model.generate_content(prompt)
            
            if response.text:
                return response.text, None
            return None, "No recommendations generated"
            
        except Exception as e:
            error_msg = f"AI Error: {str(e)}"
            if "API key" in error_msg.lower():
                error_msg += "\nPlease check your GOOGLE_API_KEY configuration"
            return None, error_msg