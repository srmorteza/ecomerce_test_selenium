
import queue
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
import random
from selenium.webdriver import ActionChains


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(2)

# open the website
driver.get("http://tutorialsninja.com/demo/")
# sleep(1)
# click on photo of menu and show
driver.find_element(By.XPATH, '//a[text()="Phones & PDAs"]').click()
# sleep(1)

# click on iphone and show
# driver.find_element(By.XPATH, '//a[text()="iPhone"]').click()

# sleep(1)


# driver.find_element(By.XPATH, '//ul[@class="thumbnails"]/li[6]').click()
# sleep(1)
# driver.save_screenshot('screenshot# ' + str(random.randint(0, 101)) + '.png')
# driver.find_element(By.XPATH, '//button[@title="Close (Esc)"]').click()


# quantity = driver.find_element(By.XPATH, '//input[@name="quantity"]').click()
# # quantity.click()
# sleep(0.5)
# quantity.clear()
# sleep(0.5)
# quantity.send_keys(2)
# sleep(0.5)
# quantity = driver.find_element(
#     By.XPATH, '//button[@id="button-cart"]').click()
# sleep(0.5)


laptop = driver.find_element(
    By.XPATH, '//a[text()="Laptops & Notebooks"]')

action = ActionChains(driver)
action.move_to_element(laptop).perform()


laptops_2 = driver.find_element(
    By.XPATH, '//a[text()="Show All Laptops & Notebooks"]').click()


hp = driver.find_element(
    By.XPATH, '//a[text()="HP LP3065"]').click()


add_2_bbutton2 = driver.find_element(
    By.XPATH, '//button[@id="button-cart"]')
add_2_bbutton2.location_once_scrolled_into_view
sleep(1)
