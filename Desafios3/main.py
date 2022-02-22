#O código foi escrito No Colaab.research.google
#Por isso o comando ! pip no primeira linha
#Para executar em qualquer outro editor é só retirar ou comentar a primeira linha do código.

! pip install beautifulsoup4 Unidecode
import os.path
import time
from collections  import Counter

import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
def obtem_as_palavras_possiveis(primeira_letra: str, numero_de_letras: int) -> list:
    def verifica_se_arquivo_existe(nome_do_arquivo: str) -> bool:
        return os.path.isfile(nome_do_arquivo)

    def leia_o_arquivo(nome_do_arquivo: str) -> str:
        with open(nome_do_arquivo, "r") as file_in:
            texto = file_in.read()
        return texto

    def escreva_o_arquivo(nome_do_arquivo: str, conteudo: str) -> None:
        with open(nome_do_arquivo, "w") as file_out:
            file_out.write(conteudo)

    palavras_alvo = f"palavras-comecam-{primeira_letra}-com-{numero_de_letras}-letras"
    arquivo_backup = palavras_alvo + ".txt"

    # Se o arquivo existe, carregue do disco
    if verifica_se_arquivo_existe(arquivo_backup):
        lista_de_palavras = leia_o_arquivo(arquivo_backup)
    # Senão, obtenha as palavras e salve o arquivo para o disco
    # para que possa ser utilizado da próxima vez
    else:
        page = requests.get(f"https://www.dicio.com.br/{palavras_alvo}/")
        soup = BeautifulSoup(page.content, "html.parser")
        lista_de_palavras = soup.find_all("p")[1].get_text(separator=" ").strip()
        escreva_o_arquivo(arquivo_backup, lista_de_palavras)
        time.sleep(2)

    return map(normalizar_palavra, lista_de_palavras.split())

def procurar_anagrama(palavra_referencia: str) -> list:
    def compara_contra_alvo(palavra_alvo: str) -> bool:
        return testa_se_anagrama(
            referencia_inspecionada, inspecionar_palavra(palavra_alvo),
        )

    referencia_inspecionada = inspecionar_palavra(palavra_referencia)
    letras_na_referencia = referencia_inspecionada.keys()
    len_referencia = sum(referencia_inspecionada.values())

    lista_possibilidades = []
    for letra in letras_na_referencia:
        lista_possibilidades.extend(obtem_as_palavras_possiveis(letra, len_referencia))

    print(f"Testando anagrama contra {len(lista_possibilidades)} possibilidades")
    return list(filter(compara_contra_alvo, lista_possibilidades))

#Exemplos de testes

procurar_anagram("Brasil")

procurar_anagrama("Roma")

procurar_anagrama("Valéria")

procurar_anagrama("Santos")