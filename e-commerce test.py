from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def reg_user (driver):
    driver.get("https://qa-practice.netlify.app/register")
    driver.find_element(By.ID, "first-name").send_keys("Nuraini")
    driver.find_element(By.ID, "last-name").send_keys("Razali")
    driver.find_element(By.ID, "phone").send_keys("0123456789")
    dropdown = Select(driver.find_element(By.ID, "countries_dropdown_menu"))
    dropdown.select_by_visible_text("Malaysia")
    driver.find_element(By.ID, "emailAddress").send_keys("nuraini.razali@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Test1234")
    checkbox = driver.find_element(By.ID, "exampleCheck1")

    if not checkbox.is_selected():
        checkbox.click()
    driver.find_element(By.CSS_SELECTOR, "button[type='registerBtn']").click()
    time.sleep(2)

def login_user (driver):
    driver.get("https://qa-practice.netlify.app/auth_ecommerce")
    driver.find_element(By.ID, "email").send_keys("nuraini.razali@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Test1234")
    driver.find_element(By.CSS_SELECTOR, "button[type='submitLoginBtn']").click()
    time.sleep(2)

def add_product_to_cart(driver):
    driver.get("https://qa-practice.netlify.app/auth_ecommerce")
    driver.find_element(By.CLASS_NAME, "btn btn-primary-shop-item-button").click()
    time.sleep(2)

def checkout(driver):
    driver.get("https://qa-practice.netlify.app/auth_ecommerce")
    driver.find_element(By.CLASS_NAME, "btn-btn-primary-btn-purchase").click()
    time.sleep(2)

def logout_user(driver):
    driver.find_element(By.LINK_TEXT, "Logout").click()
    time.sleep(2)

def run_tests():
    driver = webdriver.Chrome()  
    try:
        reg_user(driver)
        login_user(driver)
        add_product_to_cart(driver)
        checkout(driver)
        logout_user(driver)
    finally:
        driver.quit()

if __name__ == "__main__":
    run_tests()