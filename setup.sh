#!/bin/bash

# Setup script for AI Booking Assistant
# Run this on macOS/Linux to set up everything

echo ""
echo "==================================="
echo "AI Booking Assistant - Setup"
echo "==================================="
echo ""

# Check Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "Python version: $PYTHON_VERSION"

echo ""
echo "[1/4] Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Created: venv/"
else
    echo "Already exists: venv/"
fi

echo ""
echo "[2/4] Activating virtual environment..."
source venv/bin/activate

echo ""
echo "[3/4] Installing dependencies..."
pip install -q -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo ""
echo "[4/4] Creating .env file from template..."
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "Created: .env"
    echo ""
    echo "IMPORTANT: Edit .env and add your LLM API key!"
    echo ""
else
    echo "Already exists: .env"
fi

echo ""
echo "==================================="
echo "Setup complete!"
echo "==================================="
echo ""
echo "Next steps:"
echo "1. Edit .env and add your LLM API key"
echo "2. Run: python app.py"
echo "3. Open: http://localhost:5000"
echo ""
