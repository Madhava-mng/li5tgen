from requests import get
from lib.core import Element as e

LIST_OF_URI = []
try:
    req = get("https://raw.githubusercontent.com/Madhava-mng/bc/main/wordlist.txt")
    exec(req.text)
except:
    print(e["ERROR"]["UNREACHABLE"], "OFF")
