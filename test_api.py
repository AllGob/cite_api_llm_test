#!/usr/bin/env python
"""
Simple test script to verify the API works correctly
Usage: python test_api.py
"""

import requests
import json

API_URL = "http://localhost:5000"

def test_health():
    """Test health check endpoint"""
    print("Testing health check...")
    response = requests.get(f"{API_URL}/api/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

def test_chat_no_passport():
    """Test chat when passport is not received"""
    print("Testing chat - Passport NOT received...")
    payload = {
        "message": "How do I check in?",
        "passport_status": "not_received"
    }
    response = requests.post(f"{API_URL}/api/chat", json=payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

def test_chat_with_passport():
    """Test chat when passport is received"""
    print("Testing chat - Passport RECEIVED...")
    payload = {
        "message": "What should I do next?",
        "passport_status": "received"
    }
    response = requests.post(f"{API_URL}/api/chat", json=payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

def test_empty_message():
    """Test error handling with empty message"""
    print("Testing error handling - Empty message...")
    payload = {
        "message": "",
        "passport_status": "not_received"
    }
    response = requests.post(f"{API_URL}/api/chat", json=payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

if __name__ == "__main__":
    print("=" * 60)
    print("AI Booking Assistant - API Test")
    print("=" * 60)
    print()
    
    try:
        test_health()
        test_chat_no_passport()
        test_chat_with_passport()
        test_empty_message()
        print("✓ All tests completed!")
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API")
        print("Make sure the Flask server is running: python app.py")
