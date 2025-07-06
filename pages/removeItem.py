from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class RemoveItem:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    def removeItems(self):
        self.wait.until(EC.element_to_be_clickable((By.ID,"remove-sauce-labs-onesie"))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID,"remove-test.allthethings()-t-shirt-(red)"))).click()
