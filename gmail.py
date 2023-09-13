import requests
import os
os.system('sleep 1')
os.system('clear')
os.system('cd Banners && cat defalt.txt | lolcat')

def consultar_gmail(gmail):
    # URL da API para consulta de CNPJ
    url = f"https://beta.snusbase.com/v2/combo/{gmail}"

    try:
        # Faz a solicitação GET para a API
        response = requests.get(url)

        # Verifica se a solicitação foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Converte a resposta JSON em um dicionário Python
            data = response.json()

            # Exibe os dados da consulta
            print("ㅤ")
            print("vazamentos do gmail:")
            print("==========VAZAMENTOS===============")
            print("ㅤ")
            print("Resultado:", data["result"])
  
        else:
            print("Erro na consulta. Código de status:", response.status_code)
    except Exception as e:
        print("Erro na consulta:", str(e))

if __name__ == "__main__":
    gmail = input("Digite o gmail: ")
    consultar_gmail(gmail)

os.system("sleep 6")
os.system("python3 defalt.py")