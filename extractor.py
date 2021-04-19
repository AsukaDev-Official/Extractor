#!/usr/bin/env python3
#file : extractor.py
#author : Tegar Dev
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from colorama import init, Fore

# warna
init()
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET

logo = f"""
     .-"-.     {GREEN}                 __                        __{RESET}
    /_ _  \    {GREEN}  ____ ___  ____/  |_____________    _____/  |_{RESET}
    \{RED}@ {RED}@{RESET}  /    {GREEN}_/ __ \\  \/  /\   __\_  __ \__  \ _/ ___\   __\{RESET}
    (_> _)     {GREEN}\  ___/ >    <  |  |  |  | \// __ \\  \___|  |{RESET}
      `)(_     {GREEN} \___  >__/\_ \ |__|  |__|  (____  /\___  >__|{RESET}
      /((_`)_, {GREEN}     \/      \/                  \/     \/{RESET}
      \__(/-"               JS & CSS Extractor
     __|||__                 code : Tegar Dev
    ((__|__))           komunitas : AsukaDev Official
"""
print(logo)
url = input(f"Enter url: {GREEN}")

session = requests.Session()
session.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"

html = session.get(url).content

soup = bs(html, "html.parser")
script_files = []

for script in soup.find_all("script"):
    if script.attrs.get("src"):
        script_url = urljoin(url, script.attrs.get("src"))
        script_files.append(script_url)

css_files = []

for css in soup.find_all("link"):
    if css.attrs.get("href"):
        css_url = urljoin(url, css.attrs.get("href"))
        css_files.append(css_url)


print(f"{RESET}Total javascript files :{GREEN}", len(script_files))
print(f"{RESET}Total CSS files :{GREEN}", len(css_files))

with open("jS.txt", "w") as f:
    for js_file in script_files:
        print(js_file, file=f)

with open("css.txt", "w") as f:
    for css_file in css_files:
        print(css_file, file=f)
