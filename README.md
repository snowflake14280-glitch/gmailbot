# Gmail to Telegram Notifier

This project monitors your Gmail inbox for specific keywords and sends real-time notifications to your Telegram bot.

## Features
- Gmail API integration
- Keyword-based email filtering
- Telegram bot alerts
- OAuth authentication

## Tech Stack
- Python
- Gmail API
- Telegram Bot API

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Add your Google credentials:
   - credentials.json

3. Set environment variables:
   TELEGRAM_TOKEN=your_token
   CHAT_ID=your_chat_id

4. Run:
   python gmailbot.py
