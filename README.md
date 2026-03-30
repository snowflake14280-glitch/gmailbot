# Gmail to Telegram Notifier

This Python script monitors Gmail for specific keywords and sends notifications to a Telegram bot.

## Features
- Gmail API integration
- Keyword-based email filtering
- Telegram alerts

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Create a `.env` file:

   TELEGRAM_TOKEN=your_token
   CHAT_ID=your_chat_id

3. Add Google credentials:
   - credentials.json

4. Run:
   python gmailbot.py
