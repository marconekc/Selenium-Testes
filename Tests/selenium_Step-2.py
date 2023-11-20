from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Inicialização do WebDriver (Ou o chorme ou o Edge)
path_do_chormedriver = 'Webdriver\chromedriver.exe' #Talvez trocar o path de acordo com o pc
path_do_edgedriver = 'Webdriver\msedgedriver.exe'

#driver = webdriver.Chrome(executable_path=path_do_chormedriver)
driver = webdriver.Edge()
driver.set_window_size(1366, 768)
# URL do formulário de contato
url = "https://mapfitt.netlify.app/"
driver.get(url)
print("OK 1")
time.sleep(4)

#- Entrar na URL “https://mapfitt.netlify.app”
#- Selecionar na barra de menu “Início”
#- Clicar na opção “O que devemos fazer ao ar livre?”

inicio_select = driver.find_element('id', "inicio")
inicio_select.click()
print("OK 2")
time.sleep(5)

video_select = driver.find_element(By.CLASS_NAME, "btn-watch-video")
video_select.click()
print("OK 3")

time.sleep(5)

driver.quit()
