class Product:
    def __init__(self, price, id, qty):
        self.price = price
        self.id = id
        self.qty = qty

    def update_qty(self, no_of_items, method='add'):
        if no_of_items <= 0:
            print('Invalid quantity..')
            return
        elif method == 'add':
            self.qty += no_of_items
        else:
            self.qty -= no_of_items


class Inventory:
    def __init__(self):
        self.products = []

    def add_prod_to_inv(self, product):
        self.products.append(product)

    def print_inv(self):
        print("ID ", "Qty", "Price")
        for item in self.products:
            print(item.id, item.qty, item.price)


p1 = Product(3.5, "P1", 2)
p2 = Product(2, "P2", 10)
p3 = Product(1.75, "P3", 20)
i1 = Inventory()
i1.add_prod_to_inv(p1)
p2.update_qty(2, "add")
i1.add_prod_to_inv(p2)
i1.print_inv()
