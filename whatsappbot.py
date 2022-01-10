from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)


contatos = ['Mae']
mensagem = 'Teste Robô'

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    #enviar_mensagem(mensagem)





