import requests
import os
os.system('sleep 1')
os.system('clear')
os.system('cd Banners && cat defalt.txt | lolcat')

def consultar_cpf(cpf):
    # URL da API para consulta de CNPJ
    url = f"http://fightinsta.online/Catholic-Data-cpf/index.php/consulta?cpf={cpf}"

    try:
        # Faz a solicitação GET para a API
        response = requests.get(url)

        # Verifica se a solicitação foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Converte a resposta JSON em um dicionário Python
            data = response.json()

            # Exibe os dados da consulta
            print("ㅤ")
            print("informação do cpf:")
            print("==========SOBRE A PESSOA===============")
            print("ㅤ")
            print("Nome:", data["nome"])
            print("Cpf", data["cpf"])
            print("Telefone:", data["telefone"])
            print("Data de nascimento:", data["dataNascimento"])
            print("Sexo:", data["sexo"])
            print("ㅤ")
            print("==========SOBRE OS PAIS===============")
            print("ㅤ")
            print(f"Nome do pai: {data['nomePai']}")
            print(f"Nome da mãe: {data['nomeMae']}")
            print("ㅤ")
            print("==========ENDEREÇO===============")
            print("Endereco:", data["endereco"])
            print("ㅤ")
            print("ㅤ")
        else:
            print("Erro na consulta. Código de status:", response.status_code)
    except Exception as e:
        print("Erro na consulta:", str(e))

if __name__ == "__main__":
    cpf = input("Digite o Cpf | Apenas número: ")
    consultar_cpf(cpf)

os.system("sleep 6")
os.system("python3 defalt.py")