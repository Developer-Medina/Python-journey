import random

"""

    GERADOR DE CPF
    feito para embasar lógica e sintaxe de Python
    
"""

# fase I - gerando os 9 primeiros digitos + 2 digitos finais
# 1 passo - geramos os 9 primeiros dígitos com radint
nove_digitos = ""

for i in range(9):
    nove_digitos += str(random.randint(0, 9)) # intervalo do num gerado

# 2 passo - calculamos o primeiro dígito verificador
contador_regressivo_1 = 10
resultado_1_digito = 0

# estamos multiplicando os valores por 10 regressivo e somando eles numa variável
for digito in nove_digitos:
    resultado_1_digito += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

# estamos agora multiplicando o resultado por 10 e obtendo o resto da divisão por 11
digito_1 = (resultado_1_digito * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# print(digito_1) # debug

# 3 passo - calcular o segundo dígito verificador
dez_digitos = nove_digitos + str(digito_1)

contador_regressivo_2 = 11
resultado_2_digito = 0

for digito in dez_digitos:
    resultado_2_digito += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_2_digito * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

# print(digito_2) # debug

# fase II - montando tudo
# 4 passo - montando os 9 números + 2 dígitos em uma string única
cpf = f"{nove_digitos}{digito_1}{digito_2}"

# 5 passo - printando o CPF de duas formas
# esse primeiro print é só pra separar tudo
print("-" * 45)
print("CPF gerado (sem máscara):", cpf)
print("CPF gerado (com máscara):", f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
