# Exercício guiado: calculadora

while True:
    
    # o programa
    
    # inputs
    valor_1 = input('Digite o primeiro valor: ')
    valor_2 = input('Digite o segundo valor: ')
    operador = input('Digite o operador [+] [-] [/] [*] ')
    
    # inicializando variaveis
    valor_1_float = 0.0
    valor_2_float = 0.0
    
    # flag
    numeros_validos = None
    
    # convertendo valores e checando se estoura exception    
    try:
        valor_1_float = float(valor_1)
        valor_2_float = float(valor_2)
        numeros_validos = True        
        
    except:
        numeros_validos = None # vamos garantir que volte a ser None
    
    # uma outra checagem para validar se nossa flag segue como None
    if numeros_validos is None:
        print('Alguns números digitados são inválidos. Reiniciando programa...')
        continue
    
    # checagem de operadores permitidos
    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido. Reiniciando programa...')
        continue
    
    # checagem se operadores ultrapassam de len 1
    if len(operador) > 1:
        print('Digite apenas um operador. Reiniciando programa...')
        continue
    
    
    # continhas!
    print('Realizando a operação...')
    if(operador == '+'):
        print(f'A soma dos valores resulta em {valor_1_float + valor_2_float:.2f}.')
    elif(operador == '-'):
        print(f'O resultado da subtração é de {valor_1_float - valor_2_float:.2f}.')
    elif(operador == '/'):
        if(valor_2_float == 0):
            print('Não é possível dividir por 0.')
            continue
        else:
            print(f'A divisão do primeiro valor pelo segundo resulta em {valor_1_float/valor_2_float}.')
    elif(operador == '*'):
        print(f'O resultado da multiplicação é de {valor_1_float * valor_2_float}.')
    else:
        print('Essa parte não deveria aparecer...')
    
    
    # opcao para sair
    
    sair = input('Deseja encerrar o programa? [s]/[n] ').lower().startswith('s')  
    
    if(sair is True):
        print('Encerrando o programa...')
        break
    
    