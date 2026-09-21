# Apresentação do Programa
print("Pesquisa de Consumo Sabesp 2026")

# Convertemos a entrada para minúsculas com .lower() para facilitar a busca
imovel_input = input("Qual é o tipo de imóvel? (Comercial, Casa ou Apartamento): ").strip().lower()

if "comercial" in imovel_input:
    print("Tarifa Comercial Aplicada - consulte o plano corporativo")

elif "casa" in imovel_input or "apartamento" in imovel_input:
    consumo_m3 = float(input("Qual o consumo em m3? "))

    if "apartamento" in imovel_input and consumo_m3 <= 10:
        print("Consumo Econômico - excelente controle de água!")
    elif consumo_m3 <= 25:
        print("Consumo Moderado - dentro do padrão residencial")
    else:
        print("Consumo excessivo - adote medidas de economia e verifique vazamento")

else:
    print("Tipo de imóvel inválido! Por favor, digite Comercial, Casa ou Apartamento.")