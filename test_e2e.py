from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import unittest

GUI_MODE = False
SLEEP_SECONDS = 2

class ShopCartWebTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = False if GUI_MODE else True
        # create a new Firefox session
        self.browser = webdriver.Firefox(options=options)
        # navigate to the application home page
        self.browser.get('http://127.0.0.1:5000/')
        # sleep
        time.sleep(SLEEP_SECONDS if GUI_MODE else 0)

    def testAddProduct(self):   
        # Buy button
        buy_button = self.browser.find_element(By.CSS_SELECTOR, '.btn-buy')
        # Click buy button
        buy_button.click()
        time.sleep(1)
        # Products list
        products_in_cart = self.browser.find_elements(By.XPATH, "//ul[@id='product-list']/li")
        # Test product added to cart
        self.assertEqual(len(products_in_cart), 1)
        # sleep
        time.sleep(SLEEP_SECONDS if GUI_MODE else 0)

    def testRemoveProduct(self):   
        # Buy button
        buy_button = self.browser.find_element(By.CSS_SELECTOR, '.btn-buy')
        # Click buy button
        buy_button.click()
        # Wait ajax request
        time.sleep(1)
        # Products list
        products_in_cart = self.browser.find_elements(By.XPATH, "//ul[@id='product-list']/li")
        # Test product added to cart
        self.assertEqual(len(products_in_cart), 1)
        # sleep
        time.sleep(SLEEP_SECONDS if GUI_MODE else 0)
        # Remove button
        remove_button = self.browser.find_element(By.CSS_SELECTOR, '.btn-remove')
        # Click remove button
        remove_button.click()
        # Wait ajax request
        time.sleep(1)
        # Products list
        products_in_cart = self.browser.find_elements(By.XPATH, "//ul[@id='product-list']/li")        
        # Test product added to cart
        self.assertEqual(len(products_in_cart), 0)
        # sleep
        time.sleep(SLEEP_SECONDS if GUI_MODE else 0)

    def tearDown(self):
        # close the browser window
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()