import pandas as pd

"""

Esse sistema foi feito pensando no aprendizado de pandas e por inspiração de uma entrevista que fiz hoje.
    
"""

# A primeira fase é obter e tratar dados - e aqui obtemos dados manualmente, com um grande (não tão grande) dicionário contendo dados viáveis e dados "poluídos"
dados_brutos = {
    'Sensor': ['S-01', 'S-02', 'S-03', 'S-04', 'S-05'],
    'Umidade_Percentual': [45, 120, 38, -10, 60], # aqui, 120 e -10 são erros (a umidade deve ir de 0 a 100, nunca negativa)
    'Nivel_pH': [6.5, 7.2, 15.0, 6.8, 5.5]        # 15 também é um erro (o limite de pH é 14)
}
 
# Transformando o dicionário em Dataframe (uma tabela)
df_sensores = pd.DataFrame(dados_brutos)
# print(df_sensores)


# A segunda fase envolve entender quais dados são úteis ou não
# Esse bloco é a criação uma coluna extra com valor booleano, indicando se os dados são íntegros. Se atender as condições, recebe True, do contrário, recebe False
df_sensores['Status_Valido'] = (
    (df_sensores['Umidade_Percentual'] >= 0) & 
    (df_sensores['Umidade_Percentual'] <= 100) & 
    (df_sensores['Nivel_pH'] >= 0) & 
    (df_sensores['Nivel_pH'] <= 14)
)

print("-" * 60)
print("Base de Dados:")
print("-" * 60)
print(df_sensores)
print()


# A última fase envolve criar um relatório mais visível
# No Python, True == 1 ou mais, enquanto False == 0. Usando .sum(), garantimos que o contador de aprovados está somando esses 1s
# O contador de leituras reprovadas tá pegando o tamanho total a coluna e subtraindo do contador de aprovados. É mais pratico assim - mas deve ter outra forma de fazer...
contador_aprovados = df_sensores['Status_Valido'].sum()
contador_reprovados = len(df_sensores) - contador_aprovados

# Aqui estamos criando dois dataframes pra melhor exibição
# Um deles exibe as leituras íntegras de sensores, enquanto o outro aponta as falhas com base nas condições que definimos mais cedo
df_aprovados = df_sensores[df_sensores['Status_Valido'] == True]
df_reprovados = df_sensores[df_sensores['Status_Valido'] == False]


print("=" * 60)
print("RELATÓRIO DE STATUS DOS SENSORES 📊")
print("=" * 60)

# Ao invés de exibir tudo num for depois de converter para lista, estou usando um recurso que permite que pandas desenhe a tabela com os nomes que quero exibir nas posições de cada valor.  Ele ainda mostra a posição, mas verei como omitir isso com calma depois.
print("✅ SENSORES APROVADOS (Leituras Íntegras):")
print(df_aprovados[['Sensor', 'Umidade_Percentual', 'Nivel_pH']])

print()

print("⚠️  [Alerta] - Dados não-íntegros (Sensor apresenta falha):") # um espaço tava deixando o emoji colado com o [Alerta]
print(df_reprovados[['Sensor', 'Umidade_Percentual', 'Nivel_pH']])

print("-" * 60)
print(f"Processamento concluído: {contador_aprovados} leituras são íntegras, enquanto {contador_reprovados} sensores precisam de calibração.")

print("=" * 60)