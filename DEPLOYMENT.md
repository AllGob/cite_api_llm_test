# 🚀 Deployment Checklist

Use this checklist to deploy to Render step-by-step.

## Pre-Deployment (Do This First!)

- [ ] Have a GitHub account
- [ ] Created/cloned this repository on GitHub
- [ ] Have your LLM API key ready:
  - OpenAI: https://platform.openai.com/api-keys
  - Claude: https://console.anthropic.com
  - Other: Your provider's API dashboard

## Local Testing (Optional but Recommended)

- [ ] Cloned repo locally
- [ ] Ran `setup.bat` or `setup.sh`
- [ ] Added LLM API key to `.env`
- [ ] Ran `python app.py` successfully
- [ ] Tested at `http://localhost:5000`:
  - [ ] Passport toggle works
  - [ ] Can send messages
  - [ ] Get responses from LLM
  - [ ] Can toggle status and get different responses

## GitHub Setup

- [ ] Pushed code to GitHub:
  ```bash
  git init
  git add .
  git commit -m "Initial commit: AI Booking Assistant"
  git remote add origin https://github.com/YOUR_USERNAME/citellmapi
  git branch -M main
  git push -u origin main
  ```

- [ ] Repository is public (for Render to access)

## Render Deployment - Step by Step

### Step 1: Connect to Render
- [ ] Go to https://render.com
- [ ] Sign up or log in with GitHub
- [ ] Grant Render permission to access your GitHub repos

### Step 2: Create Web Service
- [ ] Click "New +" button (top right)
- [ ] Select "Web Service"
- [ ] Under "GitHub", search for `citellmapi`
- [ ] Click "Connect" next to your repository

### Step 3: Configure Service
In the form that appears:
- [ ] **Name**: `ai-booking-assistant` (or your choice)
- [ ] **Environment**: `Python 3`
- [ ] **Region**: Choose closest to your users
- [ ] **Branch**: `main`
- [ ] **Build Command**: `pip install -r requirements.txt` (should be auto-filled)
- [ ] **Start Command**: `gunicorn app:app` (should be auto-filled)
- [ ] **Plan**: `Free` (starter) - you can upgrade later

### Step 4: Add Environment Variables
- [ ] Click "Advanced" section (bottom of form)
- [ ] Click "Add Environment Variable" button
- [ ] Add these variables:

**Variable 1:**
- Key: `LLM_API_KEY`
- Value: `sk-proj-xxxxxxxx...` (your actual API key)
- Encrypted: Yes (checked)

**Variable 2:**
- Key: `LLM_API_URL`
- Value: `https://api.openai.com/v1/chat/completions`
- Encrypted: No

**Variable 3:**
- Key: `LLM_MODEL`
- Value: `gpt-3.5-turbo`
- Encrypted: No

**Variable 4:**
- Key: `FLASK_ENV`
- Value: `production`
- Encrypted: No

### Step 5: Deploy
- [ ] Scroll to bottom
- [ ] Click "Create Web Service" button
- [ ] Wait for deployment (2-5 minutes)
- [ ] Watch the logs scroll by (look for green ✓ indicators)

### Step 6: Verify Deployment
- [ ] You'll see a URL like: `https://ai-booking-assistant.onrender.com`
- [ ] Click the URL to open your app
- [ ] Test the chat functionality
- [ ] Verify responses are working

## Post-Deployment

- [ ] App is live and accessible
- [ ] API key is working (app shows responses, not error)
- [ ] Different passport statuses give different responses
- [ ] Share URL with others: `https://ai-booking-assistant.onrender.com`

## Troubleshooting Deployment

### "Build failed"
- [ ] Check your build log in Render (click service → logs)
- [ ] Make sure `requirements.txt` is in repo root
- [ ] Try pushing a new commit to trigger rebuild: `git commit --allow-empty -m "Trigger rebuild" && git push`

### "Build succeeded but app crashed"
- [ ] Check start command log
- [ ] Make sure `app.py` is in repo root
- [ ] Make sure environment variables are set correctly
- [ ] Check that Python version is 3.8+

### "App running but blank page"
- [ ] Clear browser cache (Ctrl+Shift+Delete)
- [ ] Check browser console for errors (F12)
- [ ] Check Render logs for Flask errors

### "LLM API error"
- [ ] Verify API key is correct
- [ ] Check that API key hasn't been rate-limited
- [ ] Ensure API key has credits/usage available
- [ ] Try a fresh API key from your provider's dashboard

### "Connection refused"
- [ ] Wait a bit longer - Render might still be starting
- [ ] Check service logs to see if it's running
- [ ] Try refreshing the page

## Cost Estimates

**Render.com:**
- Free tier: First 750 hours/month (always-on or sleeping)
- Your app uses: ~730 hours/month if running 24/7
- Cost: **FREE** (barely fits in free tier)
- **Tip**: Apps sleep after 15 min inactivity on free tier (takes ~3-5 sec to wake)

**LLM API Costs:**
- OpenAI GPT-3.5: ~$0.001 per chat
- OpenAI GPT-4: ~$0.03 per chat  
- Claude 3 Sonnet: ~$0.003 per chat
- **Budget**: Start with $5 credit to test, then set up billing

**Total cost**: $0-10/month depending on usage

## After Deployment

### Keep Deployed App Warm (Optional)
If you want to avoid the 15-minute sleep on free tier:

1. Go to https://uptimerobot.com
2. Add a new HTTP monitor
3. URL: Your Render app URL
4. Interval: 5 minutes
5. Uptimerobot will ping your app, keeping it awake

### Monitor Your App
- [ ] Add to favorites in browser
- [ ] Bookmark the URL
- [ ] Test occasionally to ensure it's working
- [ ] Check Render dashboard for service status

### Next Steps
- [ ] Share with friends/colleagues for testing
- [ ] Customize the system prompt for your use case
- [ ] Add more booking context fields
- [ ] Improve the UI styling
- [ ] Consider upgrading to Render paid plan for guaranteed uptime

## Common Deployment Questions

**Q: Can I see the logs?**
A: Yes, go to your service on Render → Logs tab

**Q: Can I update my code without redeploying?**
A: Any push to GitHub automatically triggers a redeploy

**Q: How do I change the API key?**
A: Edit it in Render → Environment tab → Update the variable → Redeploy

**Q: Can I use a custom domain?**
A: Yes, Render has custom domain support (in service settings)

**Q: What if the free tier runs out?**
A: Your app will sleep/pause. Upgrade to a paid plan to keep it running 24/7

---

**You're ready to deploy!** Follow the steps above and your app will be live in 10 minutes. 🎉
