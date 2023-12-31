from time import sleep
import shutil
import os
from modules import load_config
config = load_config()
masterPath = config['Master Folder Path']
oldconfig=[]
while True:
    #print("reasding config")
    try:
        config = eval(open("env","r").read())
    except:
        print("slideshow could not read config")
        continue

    if config != oldconfig or not any(file in os.listdir("flood") for file in config):
        print("slideshow refresh")
        for file in os.listdir("./flood"):
            if file not in config:
                os.remove(f"flood/{file}") if file.endswith(".jpg") or file.endswith(".png") else None
        for filename in config:
            #print(f"{masterPath}{('/' if not masterPath.endswith('/') else '')}{filename}")
            shutil.copy(f"{masterPath}{('/' if not masterPath.endswith('/') else '')}{filename}","./flood")
    oldconfig = config