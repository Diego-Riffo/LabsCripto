from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.fullscreen_window
driver.get('https://www.pccomponentes.com/signup')


imput_user= driver.find_element(By.XPATH,'//*[@id="name"]')
imput_user.send_keys("Diegooooooooo")
sleep(3)
imput_email= driver.find_element(By.XPATH,'//*[@id="email"]')
imput_email.send_keys("sdadasdasdadasd@gmail.com")
sleep(3)
imput_pass= driver.find_element(By.XPATH,'//*[@id="password"]')
imput_pass.send_keys("jhodfoA4g%&hjs")

sleep(3)
imput_TYC= driver.find_element(By.XPATH,'//*[@id="policy"]')
imput_TYC.click()
sleep(3)
imput_pass2= driver.find_element(By.XPATH,'//*[@id="repeatPassword"]')
imput_pass2.send_keys("jhodfoA4g%&hjs")
sleep(300)

imput_send= driver.find_element(By.XPATH,'//*[@id="root"]/main/section[2]/form/button[2]')
imput_send.click()

sleep(600)