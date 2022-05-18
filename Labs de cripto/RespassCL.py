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
driver.get('https://pcmastergames.cl/mi-cuenta/lost-password/')
input_email= driver.find_element(By.XPATH,'//*[@id="user_login"]')
a=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))+"@gmail.com"
input_email.send_keys(a)
    
input_buton= driver.find_element(By.XPATH,'//*[@id="post-11"]/div/div/form/p[3]/button')
input_buton.click()

sleep(2)
