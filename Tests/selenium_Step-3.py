from selenium import webdriver
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

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
#- Na barra de menu selecione a opção “Esportes”
#- Filtre por “Compaz”
#- Selecione o link no campo “Basquete”

esportes_select = driver.find_element('id', "esportes")
esportes_select.click()
print("OK 2")
time.sleep(4)

#driver.find_element(By.XPATH, "//a[contains(text(), 'MFIT')]")

opcao_select = driver.find_element(By.XPATH, "//li[contains(text(), 'COMPAZ')]")
ActionChains(driver)\
        .move_to_element(opcao_select)\
        .perform()
time.sleep(1)
opcao_select.click()
print("OK 3")

time.sleep(1)

esporte_select = driver.find_element(By.XPATH, "//h4[contains(text(), 'Basquete')]")
ActionChains(driver)\
        .move_to_element(esporte_select)\
        .perform()
time.sleep(1)
print("OK 4")

time.sleep(1)
esporte_link = driver.find_element(By.XPATH, "//a[contains(@href, '/mapfit/basquete')]")
esporte_link.click()
print("OK 5")
time.sleep(5)

driver.quit()

