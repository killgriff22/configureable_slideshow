from classes import *
config = load_config()
masterPath = config['Master Folder Path']
ans = input("do you want to skip tagged pictures? (y/n): ")
ans = True if ans.lower() == "y" else False if "n" else exit()
for img in os.listdir(masterPath):
    if img.endswith(".jpg") or img.endswith(".png"):
        img_ = image(masterPath + ("/" if not masterPath[-1] == "/" else "") + img)
        open("path", "w").write(img_.path)
        view = subprocess.Popen(["/usr/bin/python3","./previewer.py"],stdout=subprocess.DEVNULL)
        if ans and img_.tags:
            view.kill()
            continue
        img_.tagging()
        view.kill()
