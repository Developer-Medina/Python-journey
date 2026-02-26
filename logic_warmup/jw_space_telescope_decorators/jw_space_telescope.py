def checagem_temperatura(temp):
    if not isinstance(temp, (float, int)):
        print('Erro: a temperatura precisa ser um número inteiro ou em ponto flutuante.')
        return False
        
    elif 0 <= temp <= 100:
        return True
    
    # Último caso
    print('Erro: a temperatura está fora de intervalo válido.')
    return False
        


def monitor_missao(funcao):
    total_leituras = 0
    
    def interna(*args, **kwargs):
        nonlocal total_leituras 
        temp = args[0]
        
        if checagem_temperatura(temp):
            total_leituras += 1
            print(f'Telemetria: leitura {total_leituras} capturada com sucesso.')
            return funcao(*args, **kwargs)
        else: 
            print('Comando abortado: sensor com falha.')
            
    return interna

@monitor_missao
def registrar_miri(temp):
    print(f'Registrando {temp}K no banco de dados.')
    
# ========== Área de Execução ==========
while True:
    entrada = input("Digite a temperatura do sensor (ou 'sair'): ").strip().lower()
    
    if entrada == 'sair':
        print("Encerrando monitoramento...")
        break
        
    try:
        valor_digitado = float(entrada)
        registrar_miri(valor_digitado)
        
    except ValueError:
        print("Erro de entrada: Por favor, digite um número válido.")
        
    print()