# imports
import os
import sys
import datetime
import json

def create_div():
    print("-" * 100)

create_div()
# creates a file using the git actions compute - current time - content says this is a text file created and loaded at so and so time
exec_dir = os.getcwd()
print("This is the executable directory", exec_dir)

# RUN_TS environment - Injected from github actions
timestamp = os.getenv("RUN_TS")
if not timestamp:
    create_div()
    print("Exiting since there is no environment variable set for RUN_TS")
    sys.exit(0)

timestamp = timestamp.replace(" ","_").replace(".","_")

create_div()

if timestamp == os.getenv("RUN_TS"):
    print("GIT runtime timestamp matched ...")
else:
    print("Unmatched timestamp")

# create file in the executable space
filename = f"backup_poc_source_file_{timestamp}.json"

# create filecontent
filecontent = {}
filecontent["loaded_at"] = timestamp
filecontent["owner"] = "deexith"
filecontent["destination"] = "source storage account"
filecontent["cloud provider"] = "azure"
filecontent["message"] = "this file is just for backup vault poc"

create_div()

with open(filename, 'w') as fp:
    json.dump(filecontent, fp, indent=4)
    pass

print("File created and content loaded : ", filename)

create_div()

# az load the created file into the source storage account