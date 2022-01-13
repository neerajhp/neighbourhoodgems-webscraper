from typing import Dict, List


class Landmark:

    def __init__(self, type: str, location: Dict[float, float], name: str, rating: int, images, description: str, tags: List[str]):
        self.type = type
        self.location = location
        self.name = name
        self.rating = rating
        self.image = images
        self.description = description
        self.tags = tags
