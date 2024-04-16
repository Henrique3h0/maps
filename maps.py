import os
from selenium.webdriver.support import expected_conditions as EC
from colorama import init, Fore, Style
from tqdm import tqdm
import os
import datetime
import webbrowser
from scraper import GoogleMapsScraper



if __name__ == "__main__":
    print("\n" + Fore.CYAN + Style.BRIGHT + "Digite um local e um tipo de estabelecimento")
    print("Exemplo: Pizzaria perto de São Paulo, SP" + Style.RESET_ALL)
    termo = input("\nDigite aqui: ")

    scraper = GoogleMapsScraper()
    scraper.search_google_maps(termo)
    resultados = scraper.scrape_results()
    scraper.close_driver()

    scraper.clear_terminal()

    if resultados:
        print("\n" + Fore.GREEN + Style.BRIGHT + "Resultados encontrados:\n" + Style.RESET_ALL)
        for resultado in tqdm(resultados, desc="Criando HTMLs", unit="HTML"):
            nome = resultado['Nome']
            endereço = resultado['Endereço']
            website = resultado['Website']
            url_extra_data = resultado['Maps_url']
            contato = resultado['Contato']

            data_atual = datetime.datetime.now().strftime("%Y-%m-%d")

            if not os.path.exists("captações"):
                os.makedirs("captações")
            if not os.path.exists(f"captações/{data_atual}"):
                os.makedirs(f"captações/{data_atual}")

            with open("base.html", "r", encoding="utf-8") as arquivo_base:
                conteudo_base = arquivo_base.read()

            conteudo_final = conteudo_base.replace("NAME_URL", f"{nome}") \
                                          .replace("ADDRESS_URL", f"{endereço}") \
                                          .replace("WEBSITE_URL", f"{website}") \
                                          .replace("MAPS_URL", f"{url_extra_data}") \
                                          .replace("CONTACT_URL", f"{contato}")

            nome_arquivo = f"{nome}.html"

            with open(os.path.join("captações", data_atual, nome_arquivo), "w", encoding="utf-8") as arquivo_final:
                arquivo_final.write(conteudo_final)

            #print(f"\nRelatório Salvo: {nome_arquivo}")
            arquivo_html = os.path.join("captações", data_atual, nome_arquivo)
            webbrowser.open(f"file://{os.path.realpath(arquivo_html)}")
    else:
        print("\n" + Fore.RED + Style.BRIGHT + "Nenhum resultado encontrado para a busca." + Style.RESET_ALL)
    print("==FIM DO SCRIPT==")
    scraper.print_final_credits()