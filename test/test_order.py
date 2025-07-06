import time
import traceback
from faker import Faker
from selenium import webdriver
from pages.login import Login
from pages.addtocart import AddToCart
from pages.removeItem import RemoveItem
from pages.checkout import Checkout
from pages.finish import Finish
def test_order():
    driver=webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    try:
        #login
        login=Login(driver)
        login.login("standard_user","secret_sauce")
        login.click()
        #add
        addItem=AddToCart(driver)
        addItem.filter()
        addItem.addItems()
        addItem.clickCart()
        #remove
        remove=RemoveItem(driver)
        remove.removeItems()
        #checkout
        faker=Faker()
        checkout=Checkout(driver)
        checkout.checkoutClick()
        checkout.checkoutDetails(faker.first_name(),faker.last_name(),faker.postalcode())
        checkout.checkoutContinue()
        #finish
        finish=Finish(driver)
        time.sleep(3)

    except Exception as e:
        print(f"Test failed due to {e}")
        traceback.print_exc()
