import json, requests, time


while(True):
    response = requests.get("http://localhost:5000")
    time.sleep(300)
