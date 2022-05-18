from time import sleep
from selenium import webdriver
import string
import random
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.fullscreen_window
driver.get('https://www.pccomponentes.com/recovery-password')
input_email= driver.find_element(By.XPATH,'//*[@id="email"]')
a=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))+"@gmail.com"
input_email.send_keys(a)
sleep(2) 
imput_TYC= driver.find_element(By.XPATH,'//*[@id="g-recaptcha"]/div/div/iframe')

imput_TYC.click()

sleep(4)   
input_buton= driver.find_element(By.XPATH,'//*[@id="root"]/main/section/form/button')
input_buton.click()

sleep(10)