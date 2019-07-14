import json


class PackageMeta:

    attributes: dict = {
        "author": "",
        "description": "",
        "website": "",
        "git_url": ""
    }

    def __init__(self, name: str, author: str = "", website: str = "", git_url: str = "", description: str = ""):
        """ Create a meta for a given package. If the name contains a space, it will be truncated """
        
        self.attributes["name"] = name.split(" ")[0]
        self.attributes["author"] = author
        self.attributes["website"] = website
        self.attributes["git_url"] = git_url
        self.attributes["description"] = description

    def __str__(self):
        return json.dumps(self.attributes)

    def dirstr(self):
        """ Get the directory name string for this meta """

        # Name seporator
        seporator = ""

        # Check if a website was specified
        if self.attributes["website"]:
            # Set the seporator
            seporator = "."

        return self.attributes["website"] + seporator + self.attributes["name"]
