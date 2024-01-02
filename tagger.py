from classes import *
config = load_config()
masterPath = config['Master Folder Path']
def about_tagging():
    skip_retag = None
    skip_tagged = None
    while skip_tagged==None:
        skip_tagged = input(f"do you want to skip tagged pictures? (y/n): ")
        skip_tagged = True if skip_tagged.lower() == "y" else False if "n" else None
    while skip_retag==None:
        skip_retag = input("do you want to skip retagging pictures? (y/n): ")
        skip_retag = True if skip_retag.lower() == "y" else False if "n" else None
    return skip_tagged, skip_retag
skip_tagged,skip_retag = about_tagging()
for img in os.listdir(masterPath):
    print(img)
    if img.endswith(".jpg") or img.endswith(".png") or img.endswith(".jpeg") or img.endswith(".gif") or img.endswith(".webp") or img.endswith(".mp4"):
        img_ = image(masterPath + ("/" if not masterPath[-1] == "/" else "") + img)
        if skip_tagged and img_.tags and (not "retag" in img_.tags or skip_retag):
            continue
        open("path", "w").write(img_.path)
        view = subprocess.Popen(["python3","./previewer.py"],stdout=subprocess.DEVNULL)
            #view.kill()
        img_.tagging()
        view.kill()
