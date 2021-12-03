import unittest
from shop_cart import ShopCart

class ShopCartTest(unittest.TestCase):

    def setUp(self):
        self.product = {
            'id': '1',
            'title': 'Book',
            'price': 15
        }

    def testAddProduct(self):
        cart = ShopCart()
        cart.addProduct(self.product)
        self.assertEqual(len(cart.getProducts()), 1)

    def testRemoveProduct(self):
        cart = ShopCart()
        cart.addProduct(self.product)
        cart.delProduct(self.product['id'])
        self.assertEqual(len(cart.getProducts()), 0)

if __name__ == '__main__':
    unittest.main()