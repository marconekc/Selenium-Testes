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

pesquisa_input = driver.find_element('id', "search-input")
pesquisa_input.send_keys("Parque da Jaqueira")
print("OK 2")

time.sleep(2)

pesquisa_resultados = driver.find_element('id', "search-results")
pesquisa_lista = pesquisa_resultados.find_elements(By.TAG_NAME, "li")
print("OK 3")

time.sleep(2)

lista_selecao = pesquisa_resultados.find_element(By.XPATH, "//li[contains(text(), 'Parque da Jaqueira')]")
lista_selecao.click()
print("OK 4")

time.sleep(5)

driver.quit()