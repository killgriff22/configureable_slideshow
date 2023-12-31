from classes import *
config = load_config()
masterPath = config['Master Folder Path']
for file in os.listdir("./metadata"):
    if file.endswith(".tags"):
        if open("./metadata/" + file, "r").read() in ["['']","[]",'[""]']:
            os.remove("./metadata/" + file)
