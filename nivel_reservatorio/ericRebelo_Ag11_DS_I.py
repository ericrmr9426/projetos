#Bem-vindo ao código da agenda 11 de DS.

#Importando funções da biblioteca colorama
from colorama import Fore, Style
import random

#Lista dos níveis:
nivel_agua = ["niv1", "niv2", "niv3", "niv4", "niv5"]

#Lista das mensagens:
mensagens = [
	"Muito baixo (crítico)",
	"Baixo",
	"Médio",
	"Alto",
	"Muito alto (alerta)"
]

#Código da função do alerta
def aviso(nivel):
	if nivel == "niv1":
		print(Fore.RED + "Muito baixo (crítico)" + Style.RESET_ALL)
	elif nivel == "niv2":
		print(Fore.YELLOW + "Baixo" + Style.RESET_ALL)
	elif nivel == "niv3":
		print("Volume de Água\n" + Fore.GREEN + "Médio" + Style.RESET_ALL)
	elif nivel == "niv4":
		print(Fore.CYAN + "Alto" + Style.RESET_ALL)
	elif nivel == "niv5":
		print(Fore.BLUE + "Muito alto (Alerta)" + Style.RESET_ALL)

#Rodando avisos
aviso("niv3")

#Gerador de avisos
while True:
	input("\nPressione ENTER para gerar outro aviso...")
	nivel = random.choice(nivel_agua)
	#Sorteia um dos itens da lista nivel_agua
	aviso(nivel)
	#Chama a função para printar o aviso correspondente



