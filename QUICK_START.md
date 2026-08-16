# 🚀 Quick Start Guide

## What Was Created

Your AI Booking Assistant prototype is ready! Here's what you got:

```
citellmapi/
├── app.py                 # Flask backend with LLM integration
├── templates/index.html   # Modern responsive UI
├── requirements.txt       # Python dependencies
├── .env.example          # Template for environment variables
├── Procfile              # Deployment configuration
├── Dockerfile            # Docker containerization
├── docker-compose.yml    # Local Docker setup
├── render.yaml           # Render.com deployment config
├── test_api.py           # API testing script
├── README.md             # Full documentation
└── .gitignore            # Git configuration
```

## 5-Minute Setup (Windows)

### Step 1: Install Python Dependencies
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: Create .env File
Copy `.env.example` to `.env`:
```powershell
Copy-Item .env.example .env
```

### Step 3: Add Your API Key
Edit `.env` and add your LLM API key (you can use OpenAI, Anthropic Claude, or other compatible providers):
```
LLM_API_KEY=sk-xxxxxxxxxxxx
LLM_API_URL=https://api.openai.com/v1/chat/completions
LLM_MODEL=gpt-3.5-turbo
```

### Step 4: Run the Application
```powershell
python app.py
```

### Step 5: Open in Browser
Navigate to: **http://localhost:5000**

## How It Works

1. **Select Passport Status**: Toggle between "Not Received" and "Received"
2. **Type a Question**: Ask "How do I check in?" or "What should I do next?"
3. **Click "Get AI Response"**: The AI replies based on the context
4. **See Context-Aware Answers**: 
   - Without passport: Explains they need to provide it + test link
   - With passport: Confirms it's received, mentions next steps (payment)

## Testing

Test your API without using the UI:
```powershell
python test_api.py
```

## Deployment to Render (Recommended)

### Prerequisites
- GitHub account
- Push this repo to GitHub

### Steps
1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Choose the `citellmapi` repository
5. Configuration auto-fills from `render.yaml` - just verify it
6. Click "Create Web Service"
7. Add environment variables in Render dashboard:
   - `LLM_API_KEY`: Your API key
   - Keep `LLM_API_URL` and `LLM_MODEL` as-is
8. Deploy! Your app will be live in 2-3 minutes

**Your public URL will be**: `https://ai-booking-assistant.onrender.com`

## Supported LLM Providers

| Provider | LLM_API_URL | LLM_MODEL | Notes |
|----------|------------|-----------|-------|
| **OpenAI** | `https://api.openai.com/v1/chat/completions` | `gpt-3.5-turbo` | Default, cheap |
| **OpenAI** | `https://api.openai.com/v1/chat/completions` | `gpt-4` | More capable |
| **Claude** | `https://api.anthropic.com/v1/messages` | `claude-3-sonnet-20240229` | Better for long text |

**Cost estimate**: 
- OpenAI GPT-3.5: ~$0.001 per chat
- OpenAI GPT-4: ~$0.03 per chat
- Claude 3 Sonnet: ~$0.003 per chat

## Demo Scenarios to Try

### Scenario 1: Without Passport
1. Keep "❌ Not Received" selected
2. Ask: "How do I check in?"
3. Expected: AI explains need for passport + upload link

### Scenario 2: With Passport  
1. Toggle to "✅ Received"
2. Ask: "What should I do next?"
3. Expected: Confirms passport, mentions payment deposit

### Scenario 3: Other Questions
Try asking:
- "What time can I check in?"
- "Do you have WiFi?"
- "Where is the parking?"
- "What if I arrive late?"

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `Connection refused` | Make sure `python app.py` is running |
| "LLM API key not configured" | Add `LLM_API_KEY` to `.env` file |
| "Error from LLM API" | Check your API key is valid and has credits |
| Port 5000 in use | Change `PORT` in `.env` or kill the process using it |

## Project Structure Explanation

- **app.py**: Flask server that:
  - Serves the web UI
  - Handles `/api/chat` requests
  - Calls your LLM API with guest message + passport status
  
- **templates/index.html**: Beautiful, responsive UI with:
  - Status toggle buttons
  - Message textarea
  - Real-time response display
  
- **Deployment files**:
  - `Procfile`: For Render/Heroku
  - `Dockerfile`: For Docker
  - `render.yaml`: Render-specific config

## What's Next?

After testing locally and deploying to Render:

1. **Customize the prompt**: Edit `SYSTEM_PROMPT` in `app.py` for different use cases
2. **Add more fields**: Extend the booking context (room number, check-in date, etc.)
3. **Improve the UI**: Customize colors, layout, language in `templates/index.html`
4. **Add database**: Store chat history or booking data
5. **Connect to real booking system**: Integrate with your actual booking database

## API Reference

### POST /api/chat
```json
Request:
{
  "message": "How do I check in?",
  "passport_status": "not_received"
}

Response:
{
  "response": "To check in, you first need to provide your passport...",
  "status": "success"
}
```

### GET /api/health
Quick health check:
```json
Response:
{
  "status": "ok",
  "llm_configured": true
}
```

## Need Help?

- Check `.env.example` for all configuration options
- Read [README.md](README.md) for detailed documentation
- Look at `test_api.py` to see how the API is called
- Check Render logs if deployment fails: https://dashboard.render.com

## Key Features ✨

✅ Real LLM integration (not hardcoded responses)  
✅ Context-aware (uses passport status)  
✅ Mobile-friendly UI  
✅ Production-ready (gunicorn, CORS)  
✅ Easy Render deployment  
✅ Docker support  
✅ Error handling  
✅ Health check endpoint  

---

**Ready?** Start with Step 1 of the 5-Minute Setup above! 🚀
