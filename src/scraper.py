import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def configurar_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://g1.globo.com/")
    driver.implicitly_wait(10)
    return driver

def pegar_noticias_categoria(driver, categoria):
    noticias_lista = []
    noticias = []  

    try:
        if categoria == "assuntos_em_alta":
            noticias = driver.find_elements(By.CSS_SELECTOR, ".post-agrupador-horizontal-g1 > div > div > a")
        elif categoria == "mais_lidas":
            div = driver.find_element(By.CSS_SELECTOR, ".post-mais-lidas")
            noticias = div.find_elements(By.CSS_SELECTOR, "a")
        elif categoria == "fato_ou_fake":
            div = driver.find_element(By.CSS_SELECTOR, ".post-agrupador-materia")
            noticias = div.find_elements(By.CSS_SELECTOR, "a")
        elif categoria == "destaques":
            div = driver.find_element(By.CSS_SELECTOR, '[data-mrf-recirculation="Home - Destaques Desktop"]')
            noticias = div.find_elements(By.CSS_SELECTOR, "a")
        elif categoria == "noticias_principal":
            div = driver.find_element(By.CSS_SELECTOR, ".areatemplate-esquerda")
            noticias = div.find_elements(By.CSS_SELECTOR, "a")
        elif categoria == "todas":
            categorias = ["assuntos_em_alta", "mais_lidas", "fato_ou_fake", "destaques", "noticias_principal"]
            for cat in categorias:
                noticias_lista.extend(pegar_noticias_categoria(driver, cat))
            return noticias_lista

    except Exception as e:
        print(f"erro ao buscar notícias da categoria '{categoria}': {e}")
    
    print(f" notícias para a categoria: {categoria}")
    for noticia in noticias:
        titulo = noticia.text
        link = noticia.get_attribute('href')
        if titulo and link:
            noticia_dict = {"titulo": titulo, "link": link}
            noticias_lista.append(noticia_dict)
            print(f"Título: {titulo}\nLink: {link}\n")
    
    return noticias_lista

def salvar_json(noticias):
    noticias_json = json.dumps(noticias, ensure_ascii=False, indent=4)
    with open("noticias.json", "w", encoding="utf-8") as json_file:
        json_file.write(noticias_json)

def executar_bot(categoria_selecionada):
    driver = configurar_driver()
    noticias = pegar_noticias_categoria(driver, categoria_selecionada)
    
    if noticias: 
        salvar_json(noticias)
        print("arquivo 'noticias.json' foi criado.")
    else:
        print(f"não foram encontradas notícias na categoria: {categoria_selecionada}.")
    
    driver.quit()
