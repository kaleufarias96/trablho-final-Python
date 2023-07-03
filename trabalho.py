from bs4 import BeautifulSoup
import requests
import re

""" Kabum """
# ------------------------------------------------------------- Lojas KABUM
url_kabum = "https://www.kabum.com.br/celular-smartphone/smartphones/iphone"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

site = requests.get(url_kabum, headers=headers)
soup = BeautifulSoup(site.content, "html.parser")

iphone_kabum = soup.find("main", {"class": "gMPwCZ"})

tr_tel_kabum = iphone_kabum.find_all("div", recursive=False)

proKabum = []

for tr in tr_tel_kabum:
    td = tr.find_all("td")
    td = tr.find_all("span")
    proKabum.append(
        {
            "modelo": td[0].get_text().strip(),
            "valor": td[2].get_text().strip(),
        }
    )


""" AMERICANAS """
# ------------------------------------------------------------- Lojas AMERICANAS
url_americanas = "https://www.americanas.com.br/busca/iphone"

site1 = requests.get(url_americanas, headers=headers)
soup1 = BeautifulSoup(site1.content, "html.parser")

pro_ameri = soup1.find(
    "div",
    {"class": "grid__StyledGrid-sc-1man2hx-0 iFeuoP src__GridItem-sc-122lblh-0 gGJHBq"},
)

tr_tel_americana = pro_ameri.find_all("div", recursive=False)

proAmeri = []

for tr in tr_tel_americana:
    td1 = tr.find_all("h3")
    td = tr.find_all("span")
    proAmeri.append(
        {
            "modelo": td1[0].get_text().strip(),
            "valor": td[1].get_text().strip(),
        }
    )


def titulo(msg, traco="-"):
    print()
    print(msg)
    print(traco * 50)


def lista_kabum():
    titulo("Tabela de preços dos Telefones da Kabum")
    print("Modelo dos aparelhos --- Valor:")

    for pro in proKabum:
        print("-" * 150)
        print(f"{pro['modelo']:40s}  {pro['valor']} ")


def lista_americanas():
    titulo("Tabela de preços dos Telefones da Americanas")
    print("Modelo dos aparelhos --- Valor:")

    for tel in proAmeri:
        print("-" * 150)
        print(f"{tel['modelo']:40s}   {tel['valor']} ")


def lista_todos():
    todos = set()

    for tel in proKabum:
        todos.add(tel["modelo"])

    for tel in proAmeri:
        todos.add(tel["modelo"])

    lista = list(todos)

    lista2 = sorted(lista)

    titulo("Todos os Telefones disponíveis")

    for tel in lista2:
        print(tel)


def apenas_kabum():
    set_kabum = set()
    set_americanas = set()

    for tel in proKabum:
        set_kabum.add(tel["modelo"])

    for tel in proAmeri:
        set_americanas.add(tel["modelo"])

    tel_loja_kabum = set_kabum.difference(set_americanas)
    titulo("Telefones disponíveis apenas na loja Kabum")

    if len(tel_loja_kabum) == 0:
        print("Obs.: * Não tem esse modelo de telefone na loja Kabum")
    else:
        for tel in tel_loja_kabum:
            print(tel)


def apenas_americanas():
    set_kabum = set()
    set_americanas = set()

    for tel in proAmeri:
        set_kabum.add(tel["modelo"])

    for tel in proKabum:
        set_americanas.add(tel["modelo"])

    tr_tel_americanas = set_americanas.difference(set_kabum)

    titulo("telefones disponíveis apenas na loja Americanas")

    if len(tr_tel_americanas) == 0:
        print("Obs.: * Não tem esse modelo de telefone na loja Americanas")
    else:
        for tel in tr_tel_americanas:
            print(tel)


def lista_usados():
    set_kabum = set()
    set_americanas = set()

    for tel in proKabum:
        set_kabum.add(tel["modelo"])

    for tel in proAmeri:
        set_americanas.add(tel["modelo"])

    tel_americana = set_americanas.union(set_kabum)

    titulo("Telefones usados nas duas lojas")

    for ola in tel_americana:
        if "Usado" in ola:
            print(ola)
        if "USADO" in ola:
            print(ola)


def lista_novos():
    set_kabum = set()
    set_americanas = set()

    for tel in proKabum:
        set_kabum.add(tel["modelo"])

    for tel in proAmeri:
        set_americanas.add(tel["modelo"])

    tel_americana = set_americanas.union(set_kabum)
    tel_americana2 = [tel_americana.capitalize() for tel_americana in tel_americana]

    titulo("Telefones usados nas duas lojas")

    for novo in tel_americana2:
        if not "Usado" in novo:
            print(novo)


while True:
    titulo("Comparativo de Modelo entre kabum e Americanas")
    titulo("Escolha uma das opções abaixo: ")
    print("1. Telefones Kabum")
    print("2. Telefones Americanas")
    print("3. Todos os Telefones")
    print("4. Apenas Telefones Kabum")
    print("5. Apenas Telefones Americanas")
    print("6. Telefones Usados ")
    print("7. Telefones Novos ")
    print("0. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        lista_kabum()
    elif opcao == 2:
        lista_americanas()
    elif opcao == 3:
        lista_todos()
    elif opcao == 4:
        apenas_kabum()
    elif opcao == 5:
        apenas_americanas()
    elif opcao == 6:
        lista_usados()
    elif opcao == 7:
        lista_novos()
    else:
        break
