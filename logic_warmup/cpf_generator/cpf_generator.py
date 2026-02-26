import pandas as pd

"""

Esse sistema foi feito para auxiliar no aprendizado de pandas.
    
"""

# A primeira fase é obter e tratar dados
# Obtemos dados manualmente, com um grande dicionário - contendo dados viáveis e dados "poluídos"
dados_brutos = {
    'Sensor': ['S-01', 'S-02', 'S-03', 'S-04', 'S-05'],
    'Umidade_Percentual': [45, 120, 38, -10, 60], # aqui, 120 e -10 são erros (a umidade deve ir de 0 a 100, nunca negativa)
    'Nivel_pH': [6.5, 7.2, 15.0, 6.8, 5.5]        # 15.0 também é um erro (o limite de pH é 14.0)
}

# Transformando o dicionário em Dataframe (uma tabela)
df_sensores = pd.DataFrame(dados_brutos)


# A segunda fase envolve entender quais dados são úteis ou não. Aqui, crio uma coluna extra (um resultado boolean) indicando se os dados são íntegros. Se atender a todos os 'ands', recebe True, do contrário, recebe False.
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


# A última fase envolve um relatório mais visível. 
# TODO: Escreva aqui como o Pandas consegue somar os valores True automaticamente para criar nossos contadores, sem precisarmos fazer isso manualmente.
contador_aprovados = df_sensores['Status_Valido'].sum()
contador_reprovados = len(df_sensores) - contador_aprovados

# TODO: Escreva aqui sobre como filtramos o DataFrame original para gerar duas "sub-tabelas" focadas no que precisamos reportar.
df_aprovados = df_sensores[df_sensores['Status_Valido'] == True]
df_reprovados = df_sensores[df_sensores['Status_Valido'] == False]


print("=" * 60)
print("RELATÓRIO DE STATUS DOS SENSORES 📊")
print("=" * 60)

# TODO: Escreva aqui sobre a decisão de exibir diretamente as colunas da tabela filtrada ao invés de iterar linha por linha para formar frases.
print("✅ SENSORES APROVADOS (Leituras Íntegras):")
print(df_aprovados[['Sensor', 'Umidade_Percentual', 'Nivel_pH']])

print("\n[Alerta] - SENSORES FORA DO LIMITE (Necessitam Calibração):")
print(df_reprovados[['Sensor', 'Umidade_Percentual', 'Nivel_pH']])

print("-" * 60)
print(f"Processamento concluído: {contador_aprovados} leituras aproveitadas com sucesso! {contador_reprovados} sensores precisam de calibração.")

print("=" * 60)