import os
import requests
import json

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Get the API key from environment
api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    print("Error: OPENROUTER_API_KEY not found in environment")
    exit(1)

# Print API key format (first 10 chars for verification)
print(f"API key format check: {api_key[:10]}...")

# Test configuration
url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "X-Title": "TestApp"
}
data = {
    "model": "meta-llama/Llama-3.3-8B-Instruct",
    "messages": [
        {"role": "user", "content": "Hello, how are you?"}
    ],
    "max_tokens": 256,
    "temperature": 0.2
}

print("\nSending test request...")
try:
    response = requests.post(url, headers=headers, json=data, timeout=30)
    
    print(f"\nResponse status code: {response.status_code}")
    print(f"Response headers: {dict(response.headers)}")
    print(f"Response body: {response.text}")
    
    if response.status_code != 200:
        print("\nError details:")
        try:
            error = response.json()
            print(json.dumps(error, indent=2))
        except:
            print("Could not parse error as JSON")
    
except Exception as e:
    print(f"\nError occurred: {str(e)}")
    import traceback
    print("Full traceback:")
    print(traceback.format_exc())

print("\nTest complete. Check the output above for any error messages.")