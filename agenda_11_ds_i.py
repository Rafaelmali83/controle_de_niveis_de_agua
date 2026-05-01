from colorama import Fore, Style
nivel = ['Nível 1', 'Nível 2', 'Nível 3', 'Nível 4', 'Nível 5']

print("Qual a situação do reservatório?\nInforme umas das opções.")
print(Fore.RED + "Digite 1 para Muito Baixo (crítico)")
print(Fore.YELLOW + "Digite 2 para baixo")
print(Fore.GREEN + "Digite 3 para Médio")
print(Fore.CYAN + "Digite 4 para Alto")
print(Fore.BLUE + "Digite 5 Muito alto (alerta)")
def nivel_reservatorio(cod_nivel):
        if cod_nivel == '1':
          print(Fore.RED + f"A situação é {nivel[0]} " )
        elif cod_nivel == '2':
          print(Fore.YELLOW + f"A situação é {nivel[1]} ")               
        elif cod_nivel == '3':
          print(Fore.GREEN + f"A situação é {nivel[2]} ")    
        elif cod_nivel == '4':
          print(Fore.CYAN + f"A situação é {nivel[3]} ")
        elif cod_nivel == '5':
          print(Fore.BLUE + f"A situação é {nivel[4]} ")
        else:
          print('Opção errada')
print(Style.RESET_ALL)          
cod_nivel = input("Digite a opção desejada: ")
while cod_nivel not in ['1','2','3','4','5']:
          print("Esse nível não existe")
          cod_nivel = input("Qual nível está o reservatório: ")   
nivel = nivel_reservatorio(cod_nivel)
print(Style.RESET_ALL)  