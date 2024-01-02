from classes import *
config = load_config()
masterPath = config['Master Folder Path']
ans = input(f"Files in Dir: {len(os.listdir(masterPath))}\ndo you want to skip tagged pictures? (y/n): ")
ans = True if ans.lower() == "y" else False if "n" else None
for img in os.listdir(masterPath):
    print(img)
    if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".jpeg"):
        img_ = image(masterPath + ("/" if not masterPath[-1] == "/" else "") + img)
        if ans and img_.tags and not "retag" in img_.tags:
            continue
        open("path", "w").write(img_.path)
        view = subprocess.Popen(["python3","./previewer.py"],stdout=subprocess.DEVNULL)
            #view.kill()
        img_.tagging()
        view.kill()
