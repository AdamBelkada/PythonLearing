import requests
import pandas as pd
import json
def jasonprint (obj):
    text = json.dumps(obj,sort_keys=True,indent=5)
    print (text)

def main():
    response = requests.get("https://api.spacexdata.com/v3/launches/latest")
    response = requests.get("https://edart.com/events/ManualClassificationsGet?")
    # print((response.status_code))
    # print (response.json())
    jasonprint(response.json())



if __name__ == "__main__":
    main()