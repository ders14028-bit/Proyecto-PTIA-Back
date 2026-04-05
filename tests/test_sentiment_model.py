"""
Unit tests for the Sentiment Analysis Model
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.sentiment_model import SentimentAnalyzer


def test_sentiment_analyzer():
    """Test the sentiment analyzer"""
    print("\nInitializing Sentiment Analyzer...")
    analyzer = SentimentAnalyzer()
    
    # Test cases
    test_cases = [
        {
            "text": "I absolutely love this! It's amazing!",
            "expected": "positive",
            "description": "Positive sentiment"
        },
        {
            "text": "I hate this, it's terrible!",
            "expected": "negative",
            "description": "Negative sentiment"
        },
        {
            "text": "It's okay, nothing special.",
            "expected": "neutral",
            "description": "Neutral sentiment"
        },
        {
            "text": "This product exceeded my expectations!",
            "expected": "positive",
            "description": "Positive sentiment (expectations)"
        },
        {
            "text": "Worst purchase ever made.",
            "expected": "negative",
            "description": "Negative sentiment (worst)"
        },
    ]
    
    print("\nRunning Tests:")
    print("="*70)
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(test_cases, 1):
        result = analyzer.predict(test["text"])
        sentiment = result["sentiment"]
        confidence = result["confidence"]
        
        is_correct = sentiment == test["expected"]
        status = "✓ PASS" if is_correct else "✗ FAIL"
        
        print(f"\nTest {i}: {test['description']}")
        print(f"Text: {test['text']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {sentiment} (confidence: {confidence})")
        print(f"Status: {status}")
        
        if is_correct:
            passed += 1
        else:
            failed += 1
    
    # Summary
    print("\n" + "="*70)
    print(f"Tests Passed: {passed}/{len(test_cases)}")
    print(f"Tests Failed: {failed}/{len(test_cases)}")
    print("="*70)
    
    return failed == 0


if __name__ == "__main__":
    success = test_sentiment_analyzer()
    sys.exit(0 if success else 1)
