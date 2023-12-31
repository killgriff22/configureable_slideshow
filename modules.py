import os
import random
import json
import subprocess
import sys
import random
import time
from typing import *
args = sys.argv
def load_config():
    with open("config.json", "r") as file:
        config = eval(file.read())
    return config
def clear_images():
    for file in os.listdir("."):
        if file.endswith(".jpg") or file.endswith(".png"):
            os.remove("images/" + file)
