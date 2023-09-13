import requests
import os
os.system('sleep 1')
os.system('clear')
os.system('cd Banners && cat defalt.txt | lolcat')

def consultar_cnpj(cnpj):
    # URL da API para consulta de CNPJ
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"

    try:
        # Faz a solicitação GET para a API
        response = requests.get(url)

        # Verifica se a solicitação foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Converte a resposta JSON em um dicionário Python
            data = response.json()

            # Exibe os dados da consulta
            print("ㅤ")
            print("informação do CNPJ:")
            print("==========SOBRE A EMPRESA===============")
            print("ㅤ")
            print("Nome da empresa:", data["fantasia"])
            print("Situação da empresa:", data["situacao"])
            print("Tipo de empresa:", data["porte"])
            print("ㅤ")
            print("==========SOBRE O PROPRIETÁRIO===============")
            print("ㅤ")
            print(f"Nome do proprietário: {data['nome']}")
            print(f"Tipo de pessoa: {data['natureza_juridica']}")
            print("ㅤ")
            print("==========ENDEREÇO===============")
            print("ㅤ")
            print("Logradouro:", data["logradouro"])
            print("Numero:", data["numero"])
            print("Município:", data["municipio"])
            print("Bairro:", data["bairro"])
            print("Cep:", data["cep"])
            print("ㅤ")
            print("==========INFORMAÇÕES DE CONTATO===============")
            print("ㅤ")
            print("Email:", data["email"])
            print("Telefone:", data["telefone"])
            print("ㅤ")
            print("ㅤ")
        else:
            print("Erro na consulta. Código de status:", response.status_code)
    except Exception as e:
        print("Erro na consulta:", str(e))

if __name__ == "__main__":
    cnpj = input("Digite o CNPJ | Apenas número: ")
    consultar_cnpj(cnpj)

os.system("sleep 6")
os.system("python3 defalt.py")