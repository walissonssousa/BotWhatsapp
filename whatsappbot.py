import time
from selenium.webdriver.common.by import By
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib


contatos_df = pd.read_excel("Enviar.xlsx")



navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")
time.sleep(10)


for i, mensagem in enumerate(contatos_df['Mensagem']):
    numero = contatos_df.loc[i,"Número"]
    texto = urllib.parse.quote( f" olá! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    time.sleep(5)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)








