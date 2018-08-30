import requests


request = requests.get(
    "https://api.telegram.org/botRemovedForSecurityReasons/getUpdates")

chats = request.json()["result"]

for chat in chats:
    print(chat["message"]["text"])
