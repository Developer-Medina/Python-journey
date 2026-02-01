# Quizz

perguntas = [
    {
        'Pergunta': 'Qual linguagem é mais usada para desenvolvimento web no frontend?',
        'Opções': ['Python', 'Java', 'JavaScript', 'C++'],
        'Resposta': 'JavaScript'
    },
    {
        'Pergunta': 'Qual é o maior oceano do mundo?',
        'Opções': ['Atlântico', 'Índico', 'Pacífico', 'Ártico'],
        'Resposta': 'Pacífico'  
    },
    {
        'Pergunta': 'Qual é o maior museu do mundo em área total?',
        'Opções': ['Louvre', 'British Museum', 'Metropolitan Museum of Art', 'Museu do Vaticano'],
        'Resposta': 'Louvre'  
    }, 
    {
        'Pergunta': 'Quanto é 2 elevado a 5?',
        'Opções': ['10', '25', '32', '64'],
        'Resposta': '32'   
    }, 
    {
        'Pergunta': 'O que significa a sigla CPU?',
        'Opções': ['Central Process Unit', 'Computer Personal Unit', 'Central Processing Unit', 'Control Processing Utility'],
        'Resposta': 'Central Processing Unit'           
    }
]

contador_acertos = 0

for pergunta in perguntas:
    
    print('Pergunta: ', pergunta['Pergunta'])
    print()
    
    # Listando (formato de índice) alternativa):
    for indice, alternativa in enumerate(pergunta['Opções']):
        print(f'{indice}) {alternativa}')
    
    print()
        
    # Coletando resposta do usuário:
    while True:
        resposta = input('Escolha uma opção: ')
        resposta_int = None
        
        try:
            resposta_int = int(resposta)
            if resposta_int > len(pergunta['Opções']) - 1 or resposta_int < 0:
                print('Ops! Essa não parece ser uma opção... Tente novamente!')
                continue
            break
        except ValueError:
            print('Apenas números são aceitos...')
            continue
     
    
    # Aqui, estamos pegando o valor na posição que o usuário inseriu
    valor_resposta = pergunta['Opções'][resposta_int]
    
    # Conferindo acertos e erros + aumentando contador (se for o caso)
    if(valor_resposta == pergunta['Resposta']):
        print('Você acertou! ✅')
        contador_acertos += 1
    else: 
        print('Você errou! ❌')
        
    # Fazendo divisão do terminal
    print('=' * 45)
    
print(f'Você acertou a resposta de {contador_acertos} perguntas, parabéns!')
print('=' * 45)