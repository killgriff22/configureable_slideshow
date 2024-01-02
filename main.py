from classes import *
config = load_config()
masterPath = config['Master Folder Path']
#delay = input("delay between images (seconds): ")
images = []
for file in os.listdir(masterPath):
    img=file
    if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".jpeg") or img.endswith(".gif") or img.endswith(".webp") or img.endswith(".mp4"):
        images.append(image(file))
p = subprocess.Popen(["python3","./slideshow.py"])#,stdout=subprocess.DEVNULL)
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