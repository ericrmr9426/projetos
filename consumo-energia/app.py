nome_aparelho = str
potencia_aparelho = float
tempo_medio = int
consumoMensal = float
custoEstimado = float

print("Utilitário de Consumo Elétrico")
nome_aparelho = input("Informe o aparelho:\n")
potencia_aparelho = float(input("Informe a potência do aparelho em kW\n"))
tempo_medio = int(input("Informe o tempo médio de uso diário em horas\n"))
consumoMensal = float((potencia_aparelho * tempo_medio * 30 / 1000))
print("Aparelho:, \n", nome_aparelho)
print(f"Consumo estimado do/a {nome_aparelho}: {consumoMensal:.2f} kWh/mês")
custoEstimado = consumoMensal * 0.75
print(f"Custo estimado:{custoEstimado:.2f} R$/mês")