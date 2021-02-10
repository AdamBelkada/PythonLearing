import json
import DataFrame_Create_Options as dfs
def lambda_handler(event, context):
    #print ("Received event:" + json.dumps(event))
    
    #this is working
    # event_body =json.loads(event['Records'][0]["body"])
    # print (event_body["MessageAttributes"]["iec_eqpt_code"]["Value"])
    # print (event_body["MessageAttributes"]["start_time_utc"]["Value"])
    # print (event_body["MessageAttributes"]["end_time_utc"]["Value"])

    dfs.get_data_frame
event = None
context= None
lambda_handler(event ,context)