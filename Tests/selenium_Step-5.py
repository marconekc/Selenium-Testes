from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Inicialização do WebDriver (Ou o chorme ou o Edge)
path_do_chormedriver = 'Webdriver\chromedriver.exe' # Talvez trocar o path de acordo com o pc
path_do_edgedriver = 'Webdriver\msedgedriver.exe'

#driver = webdriver.Chrome(executable_path=path_do_chormedriver)
driver = webdriver.Edge()
driver.set_window_size(1366, 768)
# URL do formulário de contato
url = "https://mapfitt.netlify.app/mapfit/inicio"
driver.get(url)
print("OK 1")
time.sleep(4)
hoverlogin = driver.find_element('id', "login1")
action = ActionChains(driver)
action.move_to_element(hoverlogin).perform()
time.sleep(2)
buttoncadastro = driver.find_element('id', "cadastro")
buttoncadastro.click()

#Preenchendo o form de cadastro
nome_input = driver.find_element('name', "name")
nome_input.send_keys("Alceu Paiva Valença")
time.sleep(3)

# Preenchendo o campo CREF
cref_input = driver.find_element('name', "cref")
cref_input.send_keys("123456-G/PE")
time.sleep(3)

# Preenchendo o campo Email
email_input = driver.find_element('name', "email")
email_input.send_keys("valenca.alceu@gmail.com")
time.sleep(3)

# Preenchendo o campo Senha
senha_input = driver.find_element('name', "senha")
senha_input.send_keys("12345678")
time.sleep(3)

# Preenchendo o campo Data
data_input = driver.find_element('name', "dataNascimento")
data_input.send_keys("01/01/2000")
time.sleep(3)

# Preenchendo o campo Número de telefone
telefone_input = driver.find_element('name', "telefone")
telefone_input.send_keys("81900000000")
time.sleep(3)

# Preenchendo o campo Gênero
genero_input = driver.find_element('name', "genero")
genero_input.send_keys("Masculino")
time.sleep(3)

# Preenchendo o campo Atuação
atuacao_input = driver.find_element('name', "atuacao")
atuacao_input.send_keys("Personal Trainer")
time.sleep(3)

# Preenchendo o campo de IMG
img_input = driver.find_element('name', "img")
img_input.send_keys("https://c.pxhere.com/photos/be/0e/photo-16530.jpg!d")
time.sleep(4)

#campo de ciência de termos
checkbox_input = driver.find_element('id', "confirme")
checkbox_input.click()

time.sleep(2)

#envio
button_cadastro = driver.find_element('id', "sendcadastro") 
button_cadastro.click()

print("Enviado com sucesso!")
# Aguardar alguns segundos para ver o resultado
time.sleep(3)

# Fechar o navegador
driver.quit()

