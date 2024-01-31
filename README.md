# Xournal++ to Telegram PDF

Export a Xournal++ file to PDF, input a description, then send it to a Telegram channel

## Requirements and installation

Install the required Python packages listed in the requirements.txt file by running the command
```bash
pip install -r requirements.txt
```

Make the script executable by running the command
```bash
chmod +x xournalpptotelegrampdf.py
```

Add this script to your PATH by adding this line to your shell configuration file (.bashrc or .zshrc)
```bash
export PATH=$PATH:/wherever/you/have/saved/xournalpptotelegrampdf
```
After this, restart your terminal or run `source ~/.bashrc`/`source ~/.zshrc` for the changes to take effect.

Get a Telegram bot token by following the prompts given by [BotFather](https://t.me/BotFather). Don't worry about the bot's name, it is irrelevant. Just remember to save the token somewhere!

## Usage

Run the script using `xournalpptotelegrampdf.py <your xournal file>` in the same directory where the Xournal++ file you want to convert to PDF and send to telegram is in. The PDF and the config.txt file will be stored in that same directory. Just follow the prompts!

### IMPORTANT: FOR PRIVATE CHANNELS

To send your files to a private channel, you will have to input the channel's id manually. Get it using either of these methods:

1. Forwarding any message sent in that channel to [Json Dump Bot](https://t.me/JsonDumpBot). It is found in either the 'id' field inside the 'chat' field of the 'forward_origin' field of the response, or the 'id' field of the 'forward_from_chat' field. It always starts with -100.

2. Access your private channel using Telegram Web. The url should be of a form very similar to https://web.telegram.org/k/#-XXXXXXXXXX. Your id would be **-100XXXXXXXXXX**.