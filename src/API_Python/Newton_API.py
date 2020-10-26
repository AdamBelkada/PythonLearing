import pandas as pd
import requests
import json


def jasonprint (obj):
    text = json.dumps(obj,sort_keys=True,indent=5)
    print (text)

def main():
    response_simplify = requests.get("https://newton.now.sh/simplify/2^2+2(2)")
    print (response_simplify.status_code)
    jasonprint(response_simplify.json())

    response_Cosine = requests.get("https://newton.now.sh/cos/pi)")
    print (response_Cosine.status_code)
    jasonprint(response_Cosine.json())
if __name__ == "__main__":
   main()
