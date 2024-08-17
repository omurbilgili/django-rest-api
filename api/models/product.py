from typing import List
from api.models.category import CategoryData

class ProductData():
    def __init__(self, name: str, count: str, categories: List[CategoryData]):
        self.name = name
        self.count = count
        self.categories = categories