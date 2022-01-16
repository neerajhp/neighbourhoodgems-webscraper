from re import I
from typing import Dict, List


class Landmark:
    # TODO Complete Docstring
    """"Represents Map Landmark 

    Attributes: 
        type:
        coords:
        location:
        name:
        rating:
        images:
        description:
        tags:
        source:
    """

    def __init__(self, type: str, coords: Dict[float, float], location: str, name: str, rating: int, images, description: str, tags: List[str], source: Dict[str, str]):
        self.type = type
        self.coords = coords
        self.location = location
        self.name = name
        self.rating = rating
        self.image = images
        self.description = description
        self.tags = tags
        self.source = source

    def printLandmark(self):

        imageSetExist = "Image set is empty"
        if self.image != []:
            imageSetExist = "Images exist"

        descriptionExist = "There is no description"
        if self.image != []:
            descriptionExist = "Description exists"

        print("\n\n====== Landmark ======\n")
        print("type:\t\t %s" % self.type)
        print("source:\t\t %s" % self.source)
        print("name:\t\t %s" % self.name)
        print("location:\t %s" % self.location)
        print("rating:\t\t %s" % self.rating)
        print("tags:\t\t %s" % self.tags)
        print("outlet:\t\t %s" % self.source["outlet"])
        print("url:\t\t %s" % self.source["url"])
        print("images:\t\t %s" % imageSetExist)
        print("description:\t %s" % descriptionExist)
