from modules import *
autofavorite_artists = ["ahegaokami","nradiowave"]
autofavorite_fetishes = []
class image:
    def __init__(self,path:str or os.PathLike,tags:List[str] = []) -> None:
        self.tags = []
        self.path = path.replace("\\", "/")
        self.name = os.path.basename(path)
        if os.path.isfile("metadata/" + self.name + ".tags"):
            self.load_tags_from_metadata()
        else:
            with open("metadata/" + self.name + ".tags", "w") as file:
                file.write(str(self.tags))
    def load_tags_from_metadata(self):
        if os.path.isfile("metadata/" + self.name + ".tags"):
            with open("metadata/" + self.name + ".tags", "r") as file:
                self.tags = eval(file.read())
    def add_tags(self,tags:list):
        if any(tag in tags and not tag in self.tags for tag in autofavorite_artists):
            self.tags.append("favorites")
        if any("fetish" in tag and not "fetish" == tag and (not "fetish" in self.tags or not "fetish" in tags) for tag in tags):
            self.tags.append("fetish")
        if any(subtag in tags and not subtag in self.tags for subtag in ["enf","exhibitionsim","exhibtion"]):
            self.tags.append("exhibitionism") if (not "exhibitionism" in self.tags and not "exhibitionism" in tags) else None
            self.tags.append("enf") if (not "enf" in self.tags and not "enf" in tags) else None
            self.tags.append("exhbition") if (not "exhibition" in self.tags and not "exhibition" in tags) else None
        if any(subtag in tags for subtag in ["natsuki","yuri_(ddlc)","sayori","monika","ddlc","doki_doki_literature_club"]):
            self.tags.append("ddlc") if (not "ddlc" in self.tags and not "ddlc" in tags) else None
            self.tags.append("doki_doki_literature_club") if (not "doki_doki_literature_club" in self.tags and not "doki_doki_literature_club" in tags) else None
        if any(subtag in tags for subtag in ["callie","marie","agent_3","pearl","marina","agent_8","splatoon","shiver","frye"]):
            self.tags.append("splatoon") if (not "splatoon" in self.tags and not "splatoon" in tags) else None
            if any(subtag_ in tags for subtag_ in ["marina","agent_8","shiver","frye"]):
                self.tags.append("octoling") if (not "octoling" in self.tags and not "octoling" in tags) else None
            elif any(subtag_ in tags for subtag_ in ["callie","marie","agent_3","pearl"]):
                self.tags.append("inkling") if (not "inkling" in self.tags and not "inkling" in tags) else None
        for tag in tags:
            if tag not in self.tags:
                if "+" in tag and tag.replace("+","") not in self.tags:
                    self.tags.append(tag.replace("+",""))
                self.tags.append(tag)
        with open("metadata/" + self.name + ".tags", "w") as file:
            file.write(str(self.tags))
    def remove_tags(self,tags:List[str]):
        if "*" in tags:
            self.tags=[]
        for tag in tags:
            if tag in self.tags:
                self.tags.remove(tag)
        with open("metadata/" + self.name + ".tags", "w") as file:
            file.write(str(self.tags))
    def tagging(self):
        print("type tags to add or remove, or type 'done' to finish\n (format: [add/remove/done] [tags*])")
        while True:
            print("tags: " + str(self.tags))
            tags = input("tags: ").split(" ")
            if tags[0] == "done" or tags == [""]:
                break
            elif tags[0] == "add" or (tags and not tags[0] == "remove"):
                tags.append("tagme") if not "tagme" in tags else None
                self.add_tags(tags[1:] if tags[0] == "add" else tags)
            elif tags[0] == "remove":
                self.remove_tags(tags[1:])
            else:
                print("invalid command")
class folder:
    def __init__(self,path:str or os.PathLike) -> None:
        self.path = path.replace("\\", "/")
        self.images = []
        self.tags = []
        if os.path.isfile("metadata/folders/" + self.name + ".tags"):
            self.load_tags_from_metadata()
        else:
            with open("metadata/folders/" + self.name + ".tags", "w") as file:
                file.write(str(self.tags))
    def find_images(self):
        for file in os.listdir(self.path):
            if file.endswith(".jpg") or file.endswith(".png"):
                self.images.append(image(file))
    def add_tags(self,tags:List[str]):
        for tag in tags:
            if tag not in self.tags:
                self.tags.append(tag)
        with open("metadata/folders/" + self.name + ".tags", "w") as file:
            file.write(str(self.tags))
    def remove_tags(self,tags:List[str]):
        for tag in tags:
            if tag in self.tags:
                self.tags.remove(tag)
        with open("metadata/folders/" + self.name + ".tags", "w") as file:
            file.write(str(self.tags))
    def load_tags_from_metadata(self):
        if os.path.isfile("metadata/folders/" + self.name + ".tags"):
            with open("metadata/folders/" + self.name + ".tags", "r") as file:
                self.tags = file.read()
    def tagging(self):
        print("tags: " + str(self.tags))
        print("type tags to add or remove, or type 'done' to finish\n (format: [add/remove/done] [tags*])")
        while True:
            tags = input("tags: ").split(" ")
            if tags[0] == "done":
                break
            elif tags[0] == "add":
                self.add_tags(tags[1:])
            elif tags[0] == "remove":
                self.remove_tags(tags[1:])
            else:
                print("invalid command")
    def ready_images(self):
        for image in self.images:
            with open(image.path, "rb") as file:
                image_data = file.read()
            with open(f"./{image.name}", "wb") as file:
                file.write(image_data)