#client program

#!/usr/bin/env python
import time
import sys
import requests

#code to read and send data to server
def main():
    while True:
        URL = "https://192.168.178.62:4997/access"
        RFIDtag = input()
        PARAMS = {"tag_id": RFIDtag, "door": "A"}
        r = requests.get(url=URL, params=PARAMS, verify=False)
        print(r.text)

main()

