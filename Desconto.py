# Saudação do app
print("Calculadora de Desconto\n")

# Passando valores para a nova variável total
total = float(input("Informe o valor total da compra:\n"))

# Aninhamento condicional com declaração de mais variáveis 
if total <= 200:
	vlr_dsc = total * 0.05
	final = total - vlr_dsc
elif total <= 300:
	vlr_dsc = total * 0.10
	final = total - vlr_dsc

# O programa só chega aqui se as outras forem False	
else:
	vlr_dsc = total * 0.15
	final = total - vlr_dsc
	
# Resultado, com variável em texto	
print(f"O valor da compra com desconto é: R$ {final}")
