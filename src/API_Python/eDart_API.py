import json
import requests
import  datetime

def get_reclassified_events(api_route, start, end, project_codes=[], iec_category_ids=[], iec_eqpt_codes=[],iso_country_code=None, equipment_techno=None):
    url = EDART_API['endpoint'] + api_route
    start_str = start.isoformat()
    end_str = end.isoformat()
    body = {
        "project_codes": project_codes,         # ["AUM3", "ALL1"]
        "iec_category_ids": iec_category_ids,   # [10101010, 10]
        "iec_eqpt_codes": iec_eqpt_codes,       # ["AUM3-xxx-xxxx", "ALL1-yyy-yyyy"]
        "iso_country_code": iso_country_code,   # String or None
        "equipment_techno": equipment_techno,   # String or None
        "start_time_utc": start_str,            # "2019-10-12T20:29:05.017Z",
        "end_time_utc": end_str                 # "2019-12-12T20:29:05.017Z"
    }
    r = requests.post(url, data=json.dumps(body), headers=EDART_API['headers'])
    if not r.ok:
        raise Exception(f"eDART API error: [{r.status_code}] {r.reason} during POST on {url} feeding {body}")
    else:
        res = r.json()
        df = API.json_2_dataframe(res, EDART_API['schemas'][api_route])
        return df