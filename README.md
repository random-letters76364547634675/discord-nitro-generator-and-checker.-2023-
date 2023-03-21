# discord-nitro-generator-and-checker.-2023
a python discord nitro code generator and checker. i made in 2023!

REMENBER!
1 code has a chance od 47,670,000,000,000,000,000,000,000,000 to be found.
If you are using 1 generator it would take 63,450,000,000,000,000,000,000 YEARS to generate 1 code.
If you are using 100 generators it would take 201,084,000,000,000,000 YEARS to generate 1 code.
If you are using 1000 generators it would take 9,590,000,000,000,000,000,000,000,000,000 YEARS to generate 1 code.
...
...
...
If you are using 1,000,000 generators it would take 63,472,930,000 YEARS to generate 1 code.

BUT!!!!!
there is not only 1 code on discord. so try it.

Instalation: copy past the code in main.py into your replit on replit.com ( create an accound and also an new python replit. )
make 2 ( or 1 ) discord webhook(s) and past the link into the 
webhook_url_1 = '(link of an webhook that the generator sends EVERY generated code! valid and not valid!)'
webhook_url_2 = '(link of an webhook that only be used if an code was found'

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
note: the generator generates also an new discord token for eatch code that get chacked! 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
note: the generator needs 41 secounds cooldown, or it will be temporaly banned from the discord api (up to an hour!!!)!
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
note: the massage that was send to an webhook contains:
      the discord gift-link implemented with the generated code (-> https://discord.gift/CODE ),
      the discord token that was used to check the validity,
      and just the code in normal letters printed.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
note: If you want to be pinged (@USERNAME) just put your username or user-id behind the @ letter in the code. its set so, that it only pings an person if an code was found! 
( If you dont want to be pinged, delete this text in line 38 ( let the {code} there!!! ) -> \n<@USERNAME>   keep the (") there! )
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

optinal: use https://cron-job.org to remotly see if your script is still running. ( image )![Screenshot (468)](https://user-images.githubusercontent.com/128254887/226699800-ddb57c0b-b3f3-420b-991f-9db2263caa2c.png)
just paste the link that is in the "webview" panel seen into the create menu.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
for the fast ones that just want to copy the code:



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
        message = f"https://discord.gift/{code}.\ntoken used: {token}\nvalid code: {code}\n<@username>"
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
 
















-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
thats my first script im oploading here! i dont know if i make updates or even upload my other scripts. This acound is ment for me as an throw away account so i could creat an replit account. i used courvix.com for my email and signed on github with that email up so i could create on replit an account using github.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
if anyone even sees my script here: have a nice day :)
