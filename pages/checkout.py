from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Checkout:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    def checkoutClick(self):
        self.wait.until(EC.element_to_be_clickable((By.ID,"checkout"))).click()
    def checkoutDetails(self,firstname,lastname,postal):
        self.wait.until(EC.element_to_be_clickable((By.ID, "first-name"))).send_keys(firstname)
        self.wait.until(EC.element_to_be_clickable((By.ID, "last-name"))).send_keys(lastname)
        self.wait.until(EC.element_to_be_clickable((By.ID, "postal-code"))).send_keys(postal)
    def checkoutContinue(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()