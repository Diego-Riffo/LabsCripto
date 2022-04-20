from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



driver = webdriver.Chrome(ChromeDriverManager().install())
driver.fullscreen_window
driver.get('https://pcmastergames.cl/mi-cuenta/edit-account/')
input_buton2 = driver.find_element(By.XPATH,'//*[@id="customer_login"]/div[3]/a')
input_buton2.click()

imput_user= driver.find_element(By.XPATH,'//*[@id="reg_email"]')
a="dsjiosajsdajklsdasjklasjkl@mail.udp"
imput_user.send_keys(a)
sleep(2)
input_buton3 = driver.find_element(By.XPATH,'//*[@id="customer_login"]/div[2]/form/p[3]/button')
input_buton3.click()

input_nombre = driver.find_element(By.XPATH,'//*[@id="account_first_name"]')
input_nombre.send_keys("Diegooooooooooooooooooooooooooooo")
sleep(2)

input_apellido = driver.find_element(By.XPATH,'//*[@id="account_last_name"]')
input_apellido.send_keys("Maradonaaaaaaaaaaaaaaaaaaaaaa")
sleep(2)

input_pass = driver.find_element(By.XPATH,'//*[@id="password_1"]')
input_pass.send_keys("Agsdj433hjsdjaGGH")
sleep(2)

input_cpass = driver.find_element(By.XPATH,'//*[@id="password_2"]')
input_cpass.send_keys("Agsdj433hjsdjaGGH")
sleep(2)

input_buton4 = driver.find_element(By.XPATH,'//*[@id="post-11"]/div/div/div/div[2]/form/p[5]/button')
input_buton4.click()

sleep(2)



