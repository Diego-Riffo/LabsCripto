from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



User= [""]
Pass= [""]
data=[""]
data.clear()
User.clear()
Pass.clear()
filepath = 'User.txt'
contador=0
with open(filepath) as fp:
    line=fp.readline()
    while line:
        data = line.split("|")
        User.append(data[0].strip('\n')) 
        Pass.append(data[1].strip('\n'))
        line = fp.readline()
        contador+=1
print(contador)
print(User,"\n") 
print(Pass,"\n")


driver = webdriver.Chrome(ChromeDriverManager().install())
for x in range(contador):
    driver.fullscreen_window
    driver.get('https://pcmastergames.cl/mi-cuenta/edit-account/')
    imput_user= driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[1]/div[1]/article/div[1]/div[1]/div[2]/div[1]/div[1]/form/p/input')
    imput_pass= driver.find_element(By.XPATH,'//*[@id="password"]')
    imput_buton= driver.find_element(By.XPATH,'//*[@id="customer_login"]/div[1]/form/p[3]/button')

    imput_user.send_keys(User[x])
    sleep(2)

    imput_pass.send_keys(Pass[x])
    sleep(2)
    imput_buton.click()

    sleep(2)

