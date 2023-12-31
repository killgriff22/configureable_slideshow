from classes import *
config = load_config()
masterPath = config['Master Folder Path']
#delay = input("delay between images (seconds): ")
images = []
for file in os.listdir(masterPath):
    if file.endswith(".jpg") or file.endswith(".png"):
        images.append(image(file))
p = subprocess.Popen(["/usr/bin/python3","./slideshow.py"])#,stdout=subprocess.DEVNULL)
while True:
    try:
        tag = input("tag: ")
        Images_to_Write = []
        for image in images:
            if tag in image.tags:
                Images_to_Write.append(image.name)
        with open("env","w") as f:
            f.write(f"{Images_to_Write}")
    except KeyboardInterrupt:
        p.kill()
        break