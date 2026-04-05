"""
Test requests for the Sentiment Analysis API
"""
import requests
import json
from typing import Dict, Any

BASE_URL = "http://localhost:8000"


def health_check():
    """Test health check endpoint"""
    print("\n▶ Testing Health Check...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    return response.status_code == 200


def get_api_info():
    """Get API information"""
    print("\n▶ Getting API Info...")
    response = requests.get(f"{BASE_URL}/info")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    return response.status_code == 200


def analyze_single_sentiment(text: str):
    """Test single sentiment analysis"""
    print(f"\n▶ Analyzing: '{text}'")
    payload = {"text": text}
    response = requests.post(
        f"{BASE_URL}/analyze",
        json=payload
    )
    print(f"Status: {response.status_code}")
    result = response.json()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    if response.status_code == 200:
        sentiment = result.get("sentiment", "").upper()
        confidence = result.get("confidence", 0)
        print(f"✓ Result: {sentiment} (confidence: {confidence})")
    
    return response.status_code == 200


def analyze_batch_sentiments(texts: list):
    """Test batch sentiment analysis"""
    print(f"\n▶ Analyzing {len(texts)} texts in batch...")
    payload = {"texts": texts}
    response = requests.post(
        f"{BASE_URL}/analyze-batch",
        json=payload
    )
    print(f"Status: {response.status_code}")
    result = response.json()
    
    if response.status_code == 200:
        print(f"Total analyzed: {result.get('total')}")
        for i, item in enumerate(result.get("results", []), 1):
            print(f"  {i}. {item['sentiment'].upper()} (confidence: {item['confidence']})")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    
    return response.status_code == 200


def run_all_tests():
    """Run all test cases"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║       Sentiment Analysis API - Test Suite                   ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    results = {
        "health_check": False,
        "api_info": False,
        "single_analysis": False,
        "batch_analysis": False
    }
    
    try:
        # Test 1: Health Check
        results["health_check"] = health_check()
        
        # Test 2: API Info
        results["api_info"] = get_api_info()
        
        # Test 3: Single Sentiment Analysis
        test_texts_single = [
            "I absolutely love this product! It's amazing and works perfectly!",
            "This is terrible, I'm very disappointed with this product.",
            "It's okay, nothing special.",
            "Eu amo este produto! É excelente!",  # Portuguese
            "¡Me encanta este producto! ¡Es fantástico!"  # Spanish
        ]
        
        for text in test_texts_single:
            analyze_single_sentiment(text)
        results["single_analysis"] = True
        
        # Test 4: Batch Analysis
        batch_texts = [
            "This is the best thing ever!",
            "I hate this so much",
            "It's fine",
            "Amazing quality and customer service",
            "Horrible experience"
        ]
        results["batch_analysis"] = analyze_batch_sentiments(batch_texts)
        
    except requests.exceptions.ConnectionError:
        print("\n✗ Error: Could not connect to API. Make sure the server is running.")
        print("  Run: python main.py")
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
    
    # Print summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    for test_name, passed in results.items():
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{test_name.replace('_', ' ').title():<30} {status}")
    
    print("="*60)


if __name__ == "__main__":
    run_all_tests()
