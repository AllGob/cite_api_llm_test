# 📋 Project Guide - AI Booking Assistant

## Overview

This is a working prototype that demonstrates AI integration with booking data. It's a simple yet complete application ready for production deployment.

**Key Features:**
- ✅ Real LLM integration (OpenAI, Claude, etc.)
- ✅ Context-aware responses based on booking status
- ✅ Beautiful, responsive web interface
- ✅ Production-ready Flask backend
- ✅ Easy Render deployment
- ✅ Docker support
- ✅ Comprehensive documentation

## Project Structure

```
citellmapi/
│
├── Core Application Files
│   ├── app.py                      # Main Flask application
│   ├── requirements.txt             # Python dependencies
│   └── templates/
│       └── index.html              # Web UI (HTML/CSS/JavaScript)
│
├── Configuration & Deployment
│   ├── .env.example                # Environment variables template
│   ├── Procfile                    # Render/Heroku deployment config
│   ├── Dockerfile                  # Docker image definition
│   ├── docker-compose.yml          # Docker local development
│   ├── render.yaml                 # Render-specific configuration
│   └── .gitignore                  # Git exclusions
│
├── Documentation
│   ├── README.md                   # Full documentation
│   ├── QUICK_START.md              # 5-minute setup guide
│   └── PROJECT_GUIDE.md            # This file
│
├── Development Tools
│   ├── test_api.py                 # API testing script
│   ├── setup.bat                   # Windows setup script
│   ├── setup.sh                    # macOS/Linux setup script
│   └── CLAUDE.md                   # Project context (AI docs)
│
└── Hidden Directories
    └── .claude/                    # AI context files
```

## File Descriptions

### Application Files

#### `app.py` - The Heart of the Application
- **Purpose**: Flask backend with LLM integration
- **What it does**:
  - Serves the web UI at `/` (routes to `index.html`)
  - Handles chat requests at `/api/chat` endpoint
  - Calls your LLM provider (OpenAI, Claude, etc.)
  - Includes error handling and health checks
- **Key components**:
  - `SYSTEM_PROMPT`: Defines AI behavior (customize for your use case)
  - `get_llm_response()`: Makes API calls to LLM provider
  - Route handlers for frontend communication

#### `templates/index.html` - The Frontend
- **Purpose**: Complete user interface
- **Features**:
  - Passport status toggle (Not Received ↔ Received)
  - Message input textarea
  - "Get AI Response" button
  - Real-time response display
  - Responsive design (mobile-friendly)
- **Technology**: HTML5, CSS3, vanilla JavaScript (no frameworks)
- **Size**: Single file, ~400 lines (easy to customize)

#### `requirements.txt` - Python Dependencies
```
Flask==3.0.0              # Web framework
Flask-CORS==4.0.0         # Cross-Origin Resource Sharing
python-dotenv==1.0.0      # Environment variable management
requests==2.31.0          # HTTP requests for LLM API
gunicorn==21.2.0          # Production web server
```

### Configuration Files

#### `.env.example` - Template
- **Purpose**: Shows what environment variables you need
- **Action needed**: Copy to `.env` and add your API key
- **Variables**:
  - `LLM_API_KEY`: Your LLM provider API key (required)
  - `LLM_API_URL`: API endpoint (pre-filled for OpenAI)
  - `LLM_MODEL`: Model name/version
  - `FLASK_ENV`: Development or production

#### `Procfile` - Deployment Configuration
- **Purpose**: Tells Render how to start your app
- **Content**: `web: gunicorn app:app`
- **Used by**: Render.com, Heroku, and similar platforms

#### `Dockerfile` - Container Definition
- **Purpose**: Packages your app in a container
- **Includes**:
  - Python 3.11 slim image
  - Dependency installation
  - Port exposure
  - Production-ready gunicorn
- **Useful for**: Local Docker testing, alternative deployments

#### `docker-compose.yml` - Local Docker Setup
- **Purpose**: Easy development with Docker
- **Command**: `docker-compose up`
- **Benefits**: No Python install needed, consistent environment

#### `render.yaml` - Render-Specific Config
- **Purpose**: Auto-configure Render deployment
- **What it does**:
  - Specifies Python 3
  - Sets build/start commands
  - Pre-fills environment variables
  - Can be ignored if deploying manually

### Documentation Files

#### `README.md` - Full Documentation
- **Content**:
  - Feature overview
  - Local setup instructions
  - API documentation
  - Deployment guides
  - Troubleshooting
  - Environment variable reference
- **Audience**: New developers joining the project

#### `QUICK_START.md` - Fast Setup Guide
- **Content**:
  - 5-minute Windows/Mac/Linux setup
  - Testing scenarios
  - LLM provider pricing
  - Troubleshooting table
  - API reference
- **Audience**: Anyone wanting to get running quickly

#### `PROJECT_GUIDE.md` - This File
- **Content**: File descriptions and architecture
- **Audience**: Developers understanding the codebase

### Development Tools

#### `test_api.py` - API Testing
- **Purpose**: Test the API without the web UI
- **Usage**: `python test_api.py` (after running `python app.py`)
- **Tests**:
  - Health check
  - Chat without passport
  - Chat with passport
  - Error handling

#### `setup.bat` - Windows Setup
- **Purpose**: Automated setup for Windows users
- **Usage**: Double-click `setup.bat`
- **What it does**:
  - Creates virtual environment
  - Installs dependencies
  - Creates `.env` from template

#### `setup.sh` - macOS/Linux Setup
- **Purpose**: Automated setup for Unix systems
- **Usage**: `bash setup.sh`
- **What it does**: Same as `setup.bat` but for Unix

## How It Works

### Flow Diagram

```
User Browser
    ↓
[Frontend: index.html]
    ├─ Passport status toggle
    ├─ Message input
    └─ Response display
    ↓ (POST /api/chat)
[Backend: app.py]
    ├─ Receive message + status
    ├─ Build context
    └─ Call LLM API
    ↓ (HTTP Request)
[LLM Provider: OpenAI/Claude/etc]
    └─ Generate response
    ↓ (Response)
[Backend: app.py]
    └─ Return to frontend
    ↓ (JSON Response)
[Frontend: index.html]
    └─ Display response
```

### Data Flow

1. **User Input**: Guest enters message and passport status is selected
2. **Frontend Submission**: JavaScript sends POST to `/api/chat`
3. **Backend Processing**: Flask receives request, validates input
4. **LLM API Call**: Backend calls OpenAI/Claude API with context
5. **Response Handling**: Backend receives LLM response
6. **Frontend Display**: Response shown to user in real-time

### Context Sent to LLM

The system prompt and booking context:
```
System: "You are a helpful booking assistant..."
User context: "Passport status: not_received"
Guest message: "How do I check in?"
```

This allows the LLM to understand the booking context and respond appropriately.

## Deployment Paths

### Path 1: Render.com (Recommended) ⭐
**Best for**: Simplicity, free tier, no credit card initially
- Steps: Push to GitHub → Connect on Render → Add API key → Deploy
- Time: 5 minutes
- Cost: Free (hobby tier), paid plans available

### Path 2: Docker (Your Server)
**Best for**: Full control, self-hosting
- Steps: Build image → Run container → Configure reverse proxy
- Time: 15 minutes
- Cost: Whatever server you use

### Path 3: Heroku (Legacy)
**Best for**: Familiar with Heroku
- Steps: Push → Heroku auto-detects from Procfile
- Time: 5 minutes
- Cost: Paid plans only (Heroku sunset free tier)

### Path 4: Local Development
**Best for**: Testing, development
- Steps: `python app.py` → Open browser
- Time: 2 minutes
- Cost: Free

## Customization Guide

### Change AI Behavior
Edit `SYSTEM_PROMPT` in `app.py`:
```python
SYSTEM_PROMPT = """You are a customer support agent for a restaurant...
- If the customer hasn't made a reservation, explain how to book
- If they have a reservation, help them modify it
"""
```

### Add More Context
Extend the message sent to LLM in `app.py`:
```python
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": f"""
        Booking context:
        - Guest name: {guest_name}
        - Room number: {room_number}
        - Check-in date: {check_in_date}
        - Passport status: {passport_status}
        
        Guest message: {guest_message}
    """}
]
```

### Modify UI
Edit `templates/index.html`:
- Change colors in `<style>` section
- Add/remove form fields in the HTML
- Modify button labels and messages

### Support Different Languages
Update the prompt and UI strings to specify language handling.

## Environment Variable Reference

| Variable | Required | Default | Example |
|----------|----------|---------|---------|
| `LLM_API_KEY` | Yes | None | `sk-proj-xxx...` |
| `LLM_API_URL` | No | OpenAI URL | `https://api.openai.com/v1/chat/completions` |
| `LLM_MODEL` | No | `gpt-3.5-turbo` | `gpt-4`, `claude-3-sonnet-20240229` |
| `FLASK_ENV` | No | `production` | `development` |
| `PORT` | No | `5000` | `8000` |

## Testing Checklist

Before deployment:
- [ ] Local setup complete
- [ ] `.env` file configured with API key
- [ ] `python app.py` runs without errors
- [ ] Frontend loads at `http://localhost:5000`
- [ ] Chat works with passport "Not Received"
- [ ] Chat works with passport "Received"
- [ ] Error message appears with empty input
- [ ] Health check works: `curl http://localhost:5000/api/health`
- [ ] Git repository created and pushed

## Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError: No module named 'flask'` | Dependencies not installed | Run `pip install -r requirements.txt` |
| "LLM API key not configured" | Missing `.env` file or `LLM_API_KEY` | Copy `.env.example` to `.env` and add your key |
| Port 5000 already in use | Another process using the port | Change `PORT` in `.env` or kill the other process |
| CORS errors | Frontend and backend on different domains | Should be auto-handled by `Flask-CORS` |
| Blank page loading | JavaScript error or Flask not serving | Check browser console and Flask logs |

## Next Steps

1. **Immediate**: Set up locally (5 minutes) - see QUICK_START.md
2. **Short-term**: Deploy to Render (5 minutes)
3. **Medium-term**: 
   - Customize prompt for your use case
   - Add more booking context fields
   - Improve UI styling
4. **Long-term**:
   - Integrate with real booking database
   - Add user authentication
   - Store chat history
   - Add analytics

## Getting Help

1. Check **QUICK_START.md** for fast setup
2. Read **README.md** for detailed docs
3. Look at **test_api.py** for API usage examples
4. Check browser console (F12) for frontend errors
5. Check Flask logs for backend errors

## Technology Stack

- **Backend**: Python 3 + Flask
- **Frontend**: HTML5 + CSS3 + Vanilla JavaScript
- **LLM Integration**: OpenAI API (or compatible)
- **Deployment**: Render.com (or Docker/Heroku)
- **Production Server**: Gunicorn
- **Containerization**: Docker (optional)

## Key Decisions Made

1. **Single-file frontend** (not React/Vue): Easier to modify, smaller bundle
2. **Flask** (not FastAPI): Simpler, great for prototypes
3. **Environment variables** (not hardcoded): Safe for production
4. **CORS enabled**: Allows future mobile app integration
5. **Health check endpoint**: Deployment monitoring
6. **Error handling**: User-friendly error messages

---

**Ready to get started?** See [QUICK_START.md](QUICK_START.md) for setup instructions.
