import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


url = "https://instagram.com"
driver: WebDriver = webdriver.Chrome(
    executable_path="C:\\Users\\ASUS\\PycharmProjects\\selenium\\chromedriver\\chromedriver.exe")

try:
    driver.get(url=url)
    time.sleep(5)

    email_field = driver.find_element(By.NAME, "username")
    email_field.clear()
    email_field.send_keys("Elena-test")
    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys("password")
    login_button = driver.find_element(By.CLASS_NAME, "_ab8w._ab94._ab99._ab9f._ab9m._ab9p._abcm")
    login_button.click()
    time.sleep(5)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()

