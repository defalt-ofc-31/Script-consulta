import os
import time
os.system('sleep 1')
os.system('clear')
os.system('cd Banners && cat defalt.txt | lolcat')
os.system('cd Banners && cat defalt2.txt | lolcat')

os.system('cd Banners && cat teste.txt | lolcat')

escolha = False

while escolha == False:
    nivel = int(input("Qual a sua escolha: "))
    if (nivel == 1):
       os.system('python3 cpf.py')
        
    elif (nivel == 2):
         os.system('python3 CNPJ.py')
         
    elif (nivel == 3):
         os.system('python3 gmail.py')