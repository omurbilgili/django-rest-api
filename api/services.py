from .models import ProductData, CategoryData

def get_static_data():
    category1 = CategoryData(name="Electronics")
    category2 = CategoryData(name="Office Supplies")

    product = ProductData(name="Laptop", count=1200, categories=[category1, category2])

    return product
