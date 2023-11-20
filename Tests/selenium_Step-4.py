from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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


pagfaq = driver.find_element('id', "faq")
pagfaq.click()

# Preenchendo os campos do formulário 
nome_input = driver.find_element('id', "name")
nome_input.send_keys("Ariano Suassuna")
print("OK 2")
email_input = driver.find_element('id', "email")
email_input.send_keys("suassuna.ar@gmail.com")

assunto_input = driver.find_element('id', "subject")
assunto_input.send_keys("Qualidade do Software")

mensagem_input = driver.find_element('name', "message")
mensagem_input.send_keys("Sempre tive meu tempo limitado no dia a dia. Com a rotina de trabalho e pós graduação acabo não conseguindo encontrar um local próximo a mim para realizar atividades físicas. Mas com o Mapfit esse problema foi resolvido, agradeço muito a equipe pelo apoio.")

time.sleep(4)

# Clicar no botão de enviar
enviar_button = driver.find_element('id','buttonsend')
enviar_button.click()
print("Enviado com sucesso!")
# Aguardar alguns segundos para ver o resultado
time.sleep(5)

# Fechar o navegador
driver.quit()

