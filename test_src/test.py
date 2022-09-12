
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get('https://www.google.com/')
sleep(3)
