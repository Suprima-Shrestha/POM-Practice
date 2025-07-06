from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
class AddToCart:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    def filter(self):
        dropdown=Select(self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"product_sort_container"))))
        dropdown.select_by_value("lohi")
    def addItems(self):
        self.wait.until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-fleece-jacket"))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie"))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    def clickCart(self):
        self.wait.until(EC.element_to_be_clickable((By.ID,"shopping_cart_container"))).click()