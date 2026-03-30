import os

import requests

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

KEYWORD = "chess.com"


def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}

    response = requests.post(url, data=data)
    print(response.text)


def authenticate():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds


def check_emails():
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)

    results = service.users().messages().list(
        userId='me',
        q="chess.com",
        maxResults=30
    ).execute()

    messages = results.get('messages', [])

    for msg in messages:
        msg_data = service.users().messages().get(
            userId='me',
            id=msg['id']
        ).execute()

        snippet = msg_data['snippet']


        if KEYWORD.lower() in snippet.lower():
            print("Match found!")

            send_telegram(f" Email Match:\n{snippet}")


if __name__ == "__main__":
    check_emails()
