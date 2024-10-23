from AppName.models import Product


class ProductViewModel:
    def __init__(self):
        self.products = []

    # def load_products(self):
    #     """Загружает все продукты из базы данных."""
    #     self.products = Product.objects.all()
