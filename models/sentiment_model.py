"""
Sentiment Analysis Model using HuggingFace Transformers
"""
from typing import Dict, List, Tuple
from transformers import pipeline
import torch
from config.settings import settings


class SentimentAnalyzer:
    """
    Sentiment analysis model wrapper using HuggingFace transformers.
    Detects positive, negative, and neutral sentiments in text.
    """
    
    def __init__(self, model_name: str = settings.MODEL_NAME):
        """
        Initialize the sentiment analysis model
        
        Args:
            model_name: HuggingFace model identifier
        """
        self.device = 0 if torch.cuda.is_available() else -1
        self.model_name = model_name
        
        # Load the pipeline
        self.classifier = pipeline(
            "sentiment-analysis",
            model=model_name,
            device=self.device,
            truncation=True,
            max_length=settings.MAX_TEXT_LENGTH
        )
        
        print(f"✓ Sentiment model loaded: {model_name}")
        print(f"  Device: {'GPU' if torch.cuda.is_available() else 'CPU'}")
    
    def predict(self, text: str) -> Dict:
        """
        Predict sentiment for a given text
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary with sentiment prediction and confidence score
        """
        if not text or len(text.strip()) == 0:
            return {
                "error": "Text cannot be empty",
                "sentiment": None,
                "confidence": 0.0,
                "label": None
            }
        
        if len(text) > settings.MAX_TEXT_LENGTH:
            text = text[:settings.MAX_TEXT_LENGTH]
        
        try:
            result = self.classifier(text)[0]
            
            # Map model output to standardized labels
            label = result['label'].lower()
            score = round(float(result['score']), 4)
            
            # Normalize labels based on model output
            sentiment_map = {
                'negative': 'negative',
                'neutral': 'neutral',
                'positive': 'positive',
                '1 star': 'negative',
                '2 stars': 'negative',
                '3 stars': 'neutral',
                '4 stars': 'positive',
                '5 stars': 'positive'
            }
            
            normalized_label = sentiment_map.get(label, 'neutral')
            
            return {
                "error": None,
                "sentiment": normalized_label,
                "confidence": score,
                "label": label,
                "raw_response": result
            }
            
        except Exception as e:
            return {
                "error": str(e),
                "sentiment": None,
                "confidence": 0.0,
                "label": None
            }
    
    def predict_batch(self, texts: List[str]) -> List[Dict]:
        """
        Predict sentiment for multiple texts
        
        Args:
            texts: List of input texts to analyze
            
        Returns:
            List of prediction dictionaries
        """
        results = []
        for text in texts:
            results.append(self.predict(text))
        return results


# Global instance - instantiated once when module is imported
sentiment_analyzer = None

def get_analyzer() -> SentimentAnalyzer:
    """Lazy load the sentiment analyzer"""
    global sentiment_analyzer
    if sentiment_analyzer is None:
        sentiment_analyzer = SentimentAnalyzer()
    return sentiment_analyzer
