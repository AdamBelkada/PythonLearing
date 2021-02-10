
import sys
import os
import json
event_msg = json.loads(open(os.path.join(sys.path[0], "snsmsg.json"), "r").read())
print (event_msg["MessageAttributes"]["ProjectKey"]["Value"])
print (event_msg["MessageAttributes"]["AssetKey"]["Value"])

# with open(os.path.join(sys.path[0], "my_file.txt"), "r") as f:
#     print(f.read())