from typing import Dict, List


class Landmark:

    def __init__(self, type: str, coords: Dict[float, float], location: str, name: str, rating: int, images, description: str, tags: List[str], source: str):
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
        print("\n\n====== Landmark ======\n")
        print("type:\t\t %s" % self.type)
        print("source:\t\t %s" % self.source)
        print("name:\t\t %s" % self.name)
        print("location:\t\t %s" % self.location)
        print("rating:\t\t %s" % self.rating)
        print("tags:\t\t %s" % self.tags)
