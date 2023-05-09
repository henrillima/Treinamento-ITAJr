import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Comando para entrar no site
driver.get("https://orteil.dashnet.org/cookieclicker/")

"""
Selecionar o idioma português:
    Encontrar o elemento (botão) que indica a seleção do idioma - comando find_element ('xpath', 'xpath_do_elemento')
    Para encontrar o xpath do elemento: inspecionar; selecionar o elemento com mouse e usar o botão direito para copiar o xpath
"""

time.sleep(5)

driver.find_element('xpath', '//*[@id="langSelect-PT-BR"]').click()

time.sleep(6)

while True:
    try:
        driver.find_element('xpath', '//*[@id="bigCookie"]').click()

        try:
            driver.find_element('xpath', '//*[@id="product0"]').click()
        except NoSuchElementException:
            continue

    except NoSuchElementException:
        break

# Comando para manter o navegador aberto
input("Pressione Enter para encerrar o programa.")

# Comando para fechar o navegador
driver.quit()