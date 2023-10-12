class Product:
    """
    class Product with params product_name, price and product_info
    """
    def __init__(self, product_name, price, product_info):
        self.product_name = product_name
        self.price = price
        self.product_info = product_info

    def __str__(self):
        return f"продукт= {self.product_name}\nціна= {self.price}\nопис= {self.product_info}"




class Cart:
    """
    class Cart with custom method add_items
    """
    def __init__(self, username):
        self.username = username
        self.in_cart = {}

    def add_items(self, item: Product):
        if isinstance(item, Product) and item not in self.in_cart:
                self.in_cart[item.product_name] = item.price


    def __str__(self):
        return f"покупець= {self.username}\nтовар= {self.in_cart}\n"

mrgr = Cart("Petya")
mrgr.add_items(Product("Musly", "25", "lololo"))
mrgr.add_items(Product("Juice", "15", "lflflslfs"))
print(mrgr)