import requests
import string
import time
import random
import threading
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'online'

webhook_url_1 = "DISCORD WEBHOOK FOR EVERY CODE"
webhook_url_2 = "DISCORD WEBHOOK FOR VALID CODE"

def generate_discord_token():
    parts = []
    for i in range(3):
        part = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=24))
        parts.append(part)
    return f'{parts[0]}.{parts[1][:6]}.{parts[2]}'

def generate_nitro_codes():
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16))
        yield code

def check_nitro_code(code):
    token = generate_discord_token()
    headers = {
        "Authorization": token
    }
    response = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{code}", headers=headers)
    print(f"{code} status code: {response.status_code}")
    if response.status_code == 200:
        print(f"{code} is valid! Token used: {token}")
        message = f"https://discord.gift/{code}.\ntoken used: {token}\nvalid code: {code}\n<@USERNAME>"
        send_webhook_message(message, webhook_url_1)
        send_webhook_message(message, webhook_url_2)
    elif response.status_code in [401, 403, 429]:
        print(f"{code} received status code {response.status_code}. Retrying in 41 seconds.")
        time.sleep(41)
        check_nitro_code(code)
    else:
        print(f"{code} is not valid. Token used: {token}")
        message = f"https://discord.gift/{code}.\ntoken used: {token}\ncode: {code}"
        send_webhook_message(message, webhook_url_1)
def send_webhook_message(message, webhook_url):
    while True:
        response = requests.post(webhook_url, data={'content': message})
        if response.status_code == 204:
            break
        else:
            print(f"Failed to send message to webhook. Retrying in 41 second...")
            time.sleep(41)

def main():
    nitro_codes = generate_nitro_codes()
    while True:
        code = next(nitro_codes)
        check_nitro_code(code)
        time.sleep(1.00)

if __name__ == '__main__':
    ping_thread = threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 8080})
    ping_thread.start()
    main()
