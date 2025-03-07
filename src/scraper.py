import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def configurar_driver():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver

def acessar_pagina(url, driver):

    driver.get(url)
    driver.implicitly_wait(10)  

def obter_noticias(driver):
 
    div = driver.find_element(By.ID, "bstn-rtcl-placeholder")
    noticias = div.find_elements(By.CSS_SELECTOR, "a")

    noticias_lista = []
    for noticia in noticias:
        titulo = noticia.text
        link = noticia.get_attribute('href')
        if titulo and link:
            noticias_lista.append({"titulo": titulo, "link": link})
    
    return noticias_lista

def salvar_noticias_json(noticias_lista, arquivo="noticias.json"):

    noticias_json = json.dumps(noticias_lista, ensure_ascii=False, indent=4)
    with open(arquivo, "w", encoding="utf-8") as json_file:
        json_file.write(noticias_json)
    print(f"Arquivo '{arquivo}' foi criado com sucesso!")

def executar_bot(url="https://g1.globo.com/"):

    driver = configurar_driver()
    acessar_pagina(url, driver)

    noticias_lista = obter_noticias(driver)

    salvar_noticias_json(noticias_lista)

    driver.quit()
