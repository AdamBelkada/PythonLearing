import pandas as pd
import requests
import json
from pandas.io.json import  json_normalize


def jasonprint (obj):
    text = json.dumps(obj,sort_keys=True,indent=5)
    print (text)


def main():
    ##access people data
    print ("\n==================View People in Space===============\n"
          + "\n================================================\n"
        )
    response = requests.get("http://api.open-notify.org/astros.json")
    print("\n=================print Jason Format===============")
    print(response.status_code)
    print("\n=================print response jason object ===============")
    print(response.json())
    df = pd.DataFrame(response.json())
    # n_df = json_normalize(data= response.json())
    print("\n=================print data frame ===============\n")
    print(df)
    print("\n=================print Jason Format===============\n")
    jasonprint(response.json())

    ##Access region data
    print ("\n==================View ISS Locations===============\n"
          + "\n================================================\n"
        )
    parameters = {
        "lat":40.71
       ,"lon":40.71
    }
    response = requests.get("http://api.open-notify.org/iss-pass.json",params=parameters)
    jasonprint(response.json())

    print("\n==================View Rise Time===============\n"
          + "\n================================================\n"
          )
    response = requests.get("http://api.open-notify.org/iss-pass.json?lat=45.0&lon=-122.3")
    pass_times = response.json()['response']
    jasonprint(pass_times)
if __name__ == "__main__":
    main()