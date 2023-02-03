import requests
import json
import os
import time
import sys

BLUE = '\033[94m'
GREEN = '\033[92m'
WHITE = '\033[97m'


def menu():
    os.system("cls")
    print(GREEN, ''',--------.            ,--.     ,------.                 ,--.   
 '--.  .--',---.  ,---.|  ,---. |  .-.  \  ,---.  ,---.,-'  '-. 
    |  |  | .-. :| .--'|  .-.  ||  |  \  :| .-. :| .--''-.  .-'     [*]   @Author:''' + WHITE + ''' w4rf0t''' + GREEN + '''
    |  |  \   --.\ `--.|  | |  ||  '--'  /\   --.\ `--.  |  |       [*]   use -h or --help for help 
    `--'   `----' `---'`--' `--'`-------'  `----' `---'  `--'       [*]   example:''' + BLUE + ''' python3 techDetect.py example.com''', end='\n')


try:
    domain = sys.argv[1]
    if (domain == '-h' or domain == '--help'):
        raise Exception
except:
    menu()
    domain = input(" Enter URL: ")
    while domain == "":
        print("Invalid URL", end="\r")
        time.sleep(0.5)
        domain = input(" Enter URL: ")
if not domain.startswith("http://") and not domain.startswith("https://"):
    domain = "http://" + domain
# Thanks to https://chuyencuadev.com
url = "https://chuyencuadev.com/command/stack"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "url": domain
}

start = time.time()
print(BLUE, "Running...", end="\r")
response = requests.post(url, headers=headers, data=data)
filename = domain.replace(
    "http://", "").replace("https://", "").replace("/", "_")
try:
    response_json = response.json()
    with open(filename+".json", "w") as f:
        f.write(json.dumps(response_json, indent=4))
except:
    with open(filename+".txt", "w") as f:
        f.write(response.text)
print(BLUE, "Time of running: ", time.time()-start)
print(GREEN, "Done! Check "+filename+".json or "+filename+".txt file")
