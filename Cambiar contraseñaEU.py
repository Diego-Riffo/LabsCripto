from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.fullscreen_window
driver.get('https://www.pccomponentes.com/usuarios/panel/mis-datos')


imput_user= driver.find_element(By.XPATH,'//*[@id="userPassword_password"]')
imput_user.send_keys("jhodfoA4g%&hjs")
sleep(3)

imput_user= driver.find_element(By.XPATH,'//*[@id="userPassword_passwordConfirm"]')
imput_user.send_keys("dfasjklJKsdo56")
sleep(3)
imput_user= driver.find_element(By.XPATH,'//*[@id="userPassword_passwordConfirm2"]')
imput_user.send_keys("dfasjklJKsdo56")
sleep(3)
imput_user= driver.find_element(By.XPATH,'//*[@id="user_password_create"]')
imput_user.click()


sleep(600)