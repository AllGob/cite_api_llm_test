# AI Booking Assistant Prototype

A simple web application that demonstrates AI integration with booking data. The assistant helps guests by answering questions about the check-in process based on their passport status.

## Features

- **Booking Status Toggle**: Switch between "Passport Not Received" and "Passport Received"
- **Guest Message Input**: Ask questions like "How do I check in?" or "What should I do next?"
- **AI Responses**: Real-time responses from a language model API
- **Context-Aware**: AI considers the current passport status when responding
- **Clean UI**: Modern, responsive interface

## Quick Start (Local Development)

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository_url>
   cd citellmapi
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create `.env` file**
   ```bash
   cp .env.example .env
   ```

5. **Configure LLM API**
   Edit `.env` and add your API credentials:
   ```
   LLM_API_KEY=your_api_key_here
   LLM_API_URL=https://api.openai.com/v1/chat/completions
   LLM_MODEL=gpt-3.5-turbo
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open in browser**
   Navigate to `http://localhost:5000`

## Demo Scenario

1. **Setup**: Passport status is set to "Not Received"
2. **Test 1**: Ask "How do I check in?"
   - Expected: AI explains you need to provide passport and gives the upload link
3. **Status Change**: Toggle to "Passport Received"
4. **Test 2**: Ask "What should I do next?"
   - Expected: AI confirms passport is received and mentions the next step is payment

## Deployment to Render

### Step 1: Prepare for Deployment

1. Make sure you have a GitHub account
2. Push this repository to GitHub

### Step 2: Create a Render Service

1. Go to [render.com](https://render.com)
2. Sign up/Log in
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure the service:
   - **Name**: `ai-booking-assistant`
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

### Step 3: Add Environment Variables

In the Render dashboard:

1. Go to your service settings
2. Click "Environment" tab
3. Add these variables:
   ```
   LLM_API_KEY=your_openai_api_key
   LLM_API_URL=https://api.openai.com/v1/chat/completions
   LLM_MODEL=gpt-3.5-turbo
   FLASK_ENV=production
   ```

4. Save and deploy

### Step 4: Access Your Application

Your app will be available at: `https://ai-booking-assistant.onrender.com`

## API Documentation

### Endpoints

#### `POST /api/chat`
Send a guest message and get an AI response.

**Request:**
```json
{
  "message": "How do I check in?",
  "passport_status": "not_received"
}
```

**Response:**
```json
{
  "response": "To check in, you first need to provide your passport...",
  "status": "success"
}
```

#### `GET /api/health`
Health check endpoint.

**Response:**
```json
{
  "status": "ok",
  "llm_configured": true
}
```

## Supported LLM Providers

The prototype supports any LLM API with OpenAI-compatible endpoints:

- **OpenAI** (default): ChatGPT 3.5, GPT-4
- **Anthropic Claude**: claude-3-sonnet-20240229
- **Other providers**: Modify `LLM_API_URL` and `LLM_MODEL` in `.env`

## Architecture

```
Frontend (HTML/CSS/JS)
         ↓
    Flask API (/api/chat)
         ↓
    LLM Provider API (OpenAI, Claude, etc.)
```

## What's NOT Included

- CRM functionality
- Telegram bot integration
- User authentication
- Passport upload/recognition
- Real payment processing
- Multiple booking management
- Complex UI/design

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `LLM_API_KEY` | Your LLM provider API key | (empty) |
| `LLM_API_URL` | LLM API endpoint | OpenAI endpoint |
| `LLM_MODEL` | Model name/version | gpt-3.5-turbo |
| `FLASK_ENV` | Flask environment | production |
| `PORT` | Server port | 5000 |

## Error Handling

The application includes error handling for:
- Missing API key
- Network timeouts
- LLM API errors
- Invalid requests

All errors are displayed in the UI with descriptive messages.

## Project Structure

```
citellmapi/
├── app.py                 # Flask application & API logic
├── templates/
│   └── index.html         # Frontend interface
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment file
├── README.md             # This file
└── .gitignore            # Git ignore rules
```

## Next Steps

1. **Configure API Key**: Add your OpenAI or other LLM provider API key
2. **Test Locally**: Run `python app.py` and test the functionality
3. **Deploy to Render**: Follow the deployment steps above
4. **Customize**: Modify `SYSTEM_PROMPT` in `app.py` for different use cases

## Support

For issues or questions:
1. Check the `.env.example` for configuration options
2. Verify your LLM API key is valid
3. Check Render logs for deployment issues

## License

This prototype is provided as-is for demonstration purposes.
