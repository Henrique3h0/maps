import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import init, Fore, Style
from tqdm import tqdm
import time
import sys
import re
import threading
import os
import pyfiglet
import random

class GoogleMapsScraper:
    def __init__(self):
        logging.basicConfig(level=logging.ERROR)
        init()

        self.print_credits()

        print("Carregando Modulos\n")
        for _ in tqdm(range(10), desc="Carregando Scraper", ascii=True):
            time.sleep(random.randint(1, 3))

        num_threads = os.cpu_count()

        for _ in tqdm(range(num_threads), desc="Verificando Threads", ascii=True):
            thread = threading.Thread(target=self.test_thread)
            thread.start()

            if thread.is_alive():
                None
            else:
                None

            thread.join()

        print(f"Verificado, todas {num_threads} estão operando")

        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver_wait = WebDriverWait(self.driver, 30)

    def print_credits(self):
        credits_text = pyfiglet.figlet_format("Google Maps Scraper", font="slant")
        print("\n" + credits_text)
        print("Desenvolvido por: LIMA\n")
        print("Github: https://github.com/Henrique3h0\n")

    def print_final_credits(self):
        credits_text = pyfiglet.figlet_format("FIM DO SCRIPT", font="slant")
        print("\n" + credits_text)
        print("Desenvolvido por: LIMA\n")
        print("Github: https://github.com/Henrique3h0\n")

    def test_thread(self):
        time.sleep(0.1)

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_line(self):
        print(Fore.YELLOW + "-" * 50 + Style.RESET_ALL)

    def search_google_maps(self, termo):
        url = f"https://www.google.com/maps/search/{termo}"
        self.driver.get(url)

        self.clear_terminal()
        print("\nBuscando resultados:")
        for _ in tqdm(range(10), desc="Progresso", ascii=True):
            self.driver.execute_script('''
                    var elementos = document.querySelectorAll('*');
                    for (var i = 0; i < elementos.length; i++) {
                        var elemento = elementos[i];
                        elemento.scrollTop += 100;
                    }
                ''')
            time.sleep(1)

    def scrape_results(self):

        divs_pizzarias = self.driver.find_elements(By.CLASS_NAME, 'Nv2PK.THOPZb.CpccDe')
        resultados = []

        if not divs_pizzarias:
            print("\n" + Fore.RED + Style.BRIGHT + "Nenhum resultado encontrado para a busca." + Style.RESET_ALL)
            sys.exit()

        threads = []
        for index, div_pizzaria in enumerate(divs_pizzarias, start=1):
            thread = threading.Thread(target=self.scrape_website, args=(div_pizzaria, resultados))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return resultados

    def scrape_website(self, div_pizzaria, resultados):
        a_tag = div_pizzaria.find_element(By.TAG_NAME, 'a')
        endereco_div = div_pizzaria.find_elements(By.CLASS_NAME, 'W4Efsd')[2]
        endereco_span = endereco_div.find_elements(By.TAG_NAME, 'span')[4]
        endereco = endereco_span.text
        nome = a_tag.get_attribute('aria-label')
        extra_data_url = a_tag.get_attribute('href')

        try:
            extra_data_driver = webdriver.Chrome(options=self.options)
            extra_data_driver.get(extra_data_url)
            time.sleep(10)
            extra_data_driver.execute_script('''
                var elementos = document.querySelectorAll('*');
                for (var i = 0; i < elementos.length; i++) {
                    var elemento = elementos[i];
                    elemento.scrollTop += 400;
                }
            ''')

            texto_website = "N/A"
            contato = "N/A"
            elementos_filhos = extra_data_driver.find_elements(By.TAG_NAME, 'div')
            can_stop = False
            for elemento in elementos_filhos:
                texto = elemento.text
                match_website = re.search(r'\S*\.com\S*', texto)
                match_telefone = re.search(r'.*\(.*\).*-.*', texto)
                if match_website:
                    texto_website = match_website.group()
                    can_stop = True
                if match_telefone:
                    contato = match_telefone.group()
                    can_stop = True
                if can_stop:
                    break


            resultados.append({
                "Nome": nome,
                "Endereço": endereco,
                "Maps_url": extra_data_url,
                "Website": texto_website,
                "Contato": contato
            })
            extra_data_driver.quit()

        except Exception as e:
            print("Não foi possível encontrar o elemento com o seletor fornecido:", e)
            resultados.append({
                "Nome": nome,
                "Endereço": endereco,
                "Maps_url": extra_data_url,
                "Website": texto_website,
                "Contato": contato
            })
            extra_data_driver.quit()

        self.print_line()

    def close_driver(self):
        self.driver.quit()