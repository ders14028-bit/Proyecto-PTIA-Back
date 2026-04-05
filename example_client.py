#!/usr/bin/env python3
"""
Simple example client for the Sentiment Analysis API
Demonstrates how to use the API endpoints
"""
import requests
import json


class SentimentAPIClient:
    """Client for Sentiment Analysis API"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
    
    def analyze(self, text: str) -> dict:
        """Analyze sentiment of a single text"""
        response = requests.post(
            f"{self.base_url}/analyze",
            json={"text": text}
        )
        return response.json()
    
    def analyze_batch(self, texts: list) -> dict:
        """Analyze sentiment of multiple texts"""
        response = requests.post(
            f"{self.base_url}/analyze-batch",
            json={"texts": texts}
        )
        return response.json()
    
    def health(self) -> dict:
        """Check API health"""
        response = requests.get(f"{self.base_url}/health")
        return response.json()
    
    def info(self) -> dict:
        """Get API information"""
        response = requests.get(f"{self.base_url}/info")
        return response.json()


def main():
    """Main example usage"""
    client = SentimentAPIClient()
    
    print("""
╔══════════════════════════════════════════════════════════════╗
║      Sentiment Analysis API - Example Client                 ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Check health
    print("\n1. Health Check:")
    health = client.health()
    print(f"   Status: {health.get('status')}")
    print(f"   Message: {health.get('message')}")
    
    # Get info
    print("\n2. API Information:")
    info = client.info()
    print(f"   Title: {info.get('title')}")
    print(f"   Version: {info.get('version')}")
    print(f"   Model: {info.get('model', {}).get('name')}")
    
    # Analyze single texts
    print("\n3. Single Text Analysis:")
    test_texts = [
        "This product is amazing! I love it!",
        "This is the worst experience I've had.",
        "It's just an average product."
    ]
    
    for text in test_texts:
        result = client.analyze(text)
        print(f"\n   Text: {text}")
        print(f"   Sentiment: {result['sentiment'].upper()}")
        print(f"   Confidence: {result['confidence']:.2%}")
    
    # Analyze batch
    print("\n4. Batch Analysis:")
    batch_result = client.analyze_batch(test_texts)
    print(f"   Total analyzed: {batch_result['total']}")
    for i, result in enumerate(batch_result['results'], 1):
        print(f"   {i}. {result['sentiment'].upper()} ({result['confidence']:.2%})")


if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("\n✗ Error: Could not connect to the API.")
        print("  Make sure the server is running: python main.py")
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
