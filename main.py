from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import datetime


# Inicializar o driver do Selenium
driver = webdriver.Chrome(executable_path=r"./chromedriver.exe")

# Navegar até a página de login
driver.get('https://expert.brasil.adp.com/ipclogin/1/loginform.html?TYPE=33554433&REALMOID=06-000a1470-e058-1656-b22f-441e0bf0d04d&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-WO5eIxD%2b8kIdnTAl%2b0hJ%2be%2f1NKnuhX0pcbFgNGlVHp9VuDW92mCKK4XQjDcqUnWo&TARGET=-SM-https%3a%2f%2fexpert%2ebrasil%2eadp%2ecom%2fexpert%2f')


username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'USER')))
username_input.send_keys('felipe.barreira')


password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'PASSWORD')))
password_input.send_keys('Qualquer10@;')


#Enviar o formulário de login
password_input.send_keys(Keys.RETURN)

hora_atual = datetime.datetime.now()
print(hora_atual)

botao = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="clock"]/button')))
#botao.send_keys(Keys.SPACE)
print(botao)

sleep(10)

# Realizar outras ações após o login, se necessário
# ...


