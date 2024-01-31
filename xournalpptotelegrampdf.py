#!/usr/bin/env python3
import os
import json
import requests
import subprocess
import sys

def check_config():
    config_path = "config.txt"
    
    if not os.path.exists(config_path):
        create_config(config_path)

    with open(config_path, 'r') as file:
        config_data = json.load(file)

    if 'bot_token' not in config_data or 'channel_id' not in config_data:
        update_config(config_path)

    return config_data

def create_config(config_path):
    config_data = {}

    bot_token = input("Enter your Telegram bot token: ")
    config_data['bot_token'] = bot_token

    private_channel = input("Is your Telegram channel private? (YES/no): ").lower() != 'no'

    
    if private_channel:
        channel_id = input("Enter your private channel ID manually: ")
    else:
        channel_name = input("Enter your public channel name (without @): ")
        channel_id = get_channel_id(config_data['bot_token'], channel_name)

    config_data['channel_id'] = channel_id

    with open(config_path, 'w') as file:
        json.dump(config_data, file, indent=2)

def get_channel_id(bot_token, channel_name):
    url = f"https://api.telegram.org/bot{bot_token}/getChat?chat_id=@{channel_name}"
    response = requests.get(url)
    data = response.json()
    return str(data['result']['id'])

def update_config(config_path):
    create_config(config_path)

def export_to_pdf(xopp_file, pdf_file):
    subprocess.run(['xournalpp', xopp_file, f'--create-pdf={pdf_file}'], check=True)

def send_to_telegram(bot_token, channel_id, pdf_file, caption=None):
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    files = {'document': open(pdf_file, 'rb')}
    data = {'chat_id': channel_id, 'caption': caption} if caption else {'chat_id': channel_id}
    response = requests.post(url, files=files, data=data)
    print(response.json())

def main():
    if len(sys.argv) != 2:
        print("Usage: xournalpptotelegrampdf.py <xournal++ file>")
        sys.exit(1)

    xopp_file = sys.argv[1]
    custom_pdf_name = input("Enter a custom name for the PDF file (press Enter to keep the same name): ").strip()

    if not custom_pdf_name:
        custom_pdf_name = os.path.splitext(os.path.basename(xopp_file))[0] + '.pdf'
    else:
        custom_pdf_name += '.pdf'

    config_data = check_config()

    print("Current configuration:")
    print("Bot Token:", config_data['bot_token'])
    print("Channel ID:", config_data['channel_id'])

    proceed_with_config = input("Do you want to proceed with this configuration? (YES/no): ").lower() != 'no'

    if not proceed_with_config:
        update_config("config.txt")
        config_data = check_config()

    caption = input("Enter an optional caption for the PDF file (press Enter to skip): ").strip()

    pdf_file = os.path.join(os.path.dirname(xopp_file), custom_pdf_name)
    export_to_pdf(xopp_file, pdf_file)
    send_to_telegram(config_data['bot_token'], config_data['channel_id'], pdf_file, caption)

if __name__ == "__main__":
    main()
