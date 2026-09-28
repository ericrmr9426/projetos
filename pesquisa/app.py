print("Pesquisa de Satisfação 2026")

# Inicializa os contadores, para deixar o código mais limpo sem o locals
excelente = 0
bom = 0
ruim = 0

# Repetição

for i in range(1, 11):
    print(f"\nEntrevistado nº {i}:")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    while True:
        print("Opinião sobre o atendimento:")
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")
        
        try:

            # Condicionais

            opcao = int(input("Escolha uma opção (1, 2 ou 3): "))
            if opcao == 1:
                excelente += 1
                break
            elif opcao == 2:
                bom += 1
                break
            elif opcao == 3:
                ruim += 1
                break
            else:
                print("Opção inválida! Digite 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

# Exibição dos resultados
print("\n" + "="*35) # Digita 35 vezes =
print("     RESULTADO DA PESQUISA     ")
print("="*35)
print(f"a) Quantidade de respostas 'EXCELENTE': {excelente}")
print(f"b) Quantidade de respostas 'BOM': {bom}")
print(f"c) Quantidade de respostas 'RUIM': {ruim}")