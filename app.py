"""
AI-powered booking assistant prototype
Integrates with LLM API for intelligent responses about bookings
"""
from google import genai
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuration
LLM_API_KEY = os.getenv("LLM_API_KEY", "")
LLM_API_URL = os.getenv("LLM_API_URL", "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-3.6-flash")

# System prompt for the AI assistant
SYSTEM_PROMPT = """You are a helpful booking assistant for a hotel. You help guests with their check-in process.
- If the guest asks about check-in or arrival and their passport status is "not_received", explain they need to provide their passport first and direct them to https://example.com/passport for uploading it.
- If the guest asks what to do next and their passport status is "received", inform them the passport has been accepted and the next step is to complete the security deposit payment.
- Be friendly, concise, and helpful in Russian or English depending on the guest's language.
- Keep responses brief (1-2 sentences max) Prefer Russian."""


def get_llm_response(guest_message: str, passport_status: str) -> str:
    """
    Get response from LLM API with booking context
    
    Args:
        guest_message: The guest's question/message
        passport_status: Either "received" or "not_received"
    
    Returns:
        AI response string
    """
    if not LLM_API_KEY:
        return "⚠️ Error: LLM API key not configured. Please set LLM_API_KEY environment variable."
    
    # Context about the booking
    booking_context = f"Guest's passport status: {passport_status}"
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"{booking_context}\n\nGuest message: {guest_message}"}
    ]
    
    try:
        response = requests.post(
            LLM_API_URL,
            headers={
                "Authorization": f"Bearer {LLM_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": LLM_MODEL,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 500
            },
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
        else:
            return f"Error from LLM API: {response.status_code} - {response.text}"
    
    except requests.exceptions.Timeout:
        return "Error: Request to LLM API timed out"
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to LLM API. Check your internet connection."
    except Exception as e:
        return f"Error: {str(e)}"


@app.route("/")
def index():
    """Serve the main page"""
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    """
    Handle chat requests
    Expects JSON: {"message": "guest message", "passport_status": "received" or "not_received"}
    """
    try:
        data = request.json
        
        guest_message = data.get("message", "").strip()
        passport_status = data.get("passport_status", "not_received")
        
        if not guest_message:
            return jsonify({"error": "Message cannot be empty"}), 400
        
        if passport_status not in ["received", "not_received"]:
            return jsonify({"error": "Invalid passport status"}), 400
        
        # Get response from LLM
        ai_response = get_llm_response(guest_message, passport_status)
        
        return jsonify({
            "response": ai_response,
            "status": "success"
        })
    
    except Exception as e:
        return jsonify({
            "error": f"Server error: {str(e)}",
            "status": "error"
        }), 500


@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "ok",
        "llm_configured": bool(LLM_API_KEY)
    })


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_ENV", "production") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
