class ShopCart:

    def __init__(self, products = {}):
        self.products = products
 
    def addProduct(self, product):
        self.products[str(product['id'])] = product

    def delProduct(self, product_id):
        del(self.products[product_id])

    def getProducts(self):
        return self.products