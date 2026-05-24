Trabalho_Estacio_2026


from google.colab import drive
drive.mount('/content/drive')

# ============================================================
# 1) Importações
# ============================================================
import pandas as pd
import numpy as np

# ============================================================
# 3) Ler o CSV do Drive
# ============================================================
caminho = "/content/drive/MyDrive/pico_web.csv"
df = pd.read_csv(caminho, sep=';', engine='python', encoding='utf-8')

# ============================================================
# 4) Verificar dados importados
# ============================================================
print("=== Informações gerais ===")
print(df.info())

print("\n=== Primeiras linhas ===")
print(df.head())

print("\n=== Últimas linhas ===")
print(df.tail())

# ============================================================
# 5) Criar uma cópia do DataFrame
# ============================================================
df2 = df.copy()

# ============================================================
# 6) Substituir valores nulos de Calories por 0
# ============================================================
df2['Calories'] = df2['Calories'].fillna(0)

print("\n=== Após substituir Calories nulos ===")
print(df2)

# ============================================================
# 7) Substituir valores nulos de Date por '1900/01/01'
# ============================================================
df2['Date'] = df2['Date'].fillna('1900/01/01')

print("\n=== Após substituir Date nulos ===")
print(df2)

# ============================================================
# 8) Tentar converter Date para datetime (gera erro previsto)
# ============================================================
print("\n>>> Tentando converter para datetime (vai dar erro previsto)...")
try:
    df2['Date'] = pd.to_datetime(df2['Date'], format='%Y/%m/%d')
except Exception as e:
    print("Erro ocorrido conforme esperado:")
    print(e)

# ============================================================
# 9) Substituir '1900/01/01' por NaN
# ============================================================
df2['Date'] = df2['Date'].replace('1900/01/01', np.nan)

print("\n=== Após remover 1900/01/01 ===")
print(df2)

# ============================================================
# 10) Tentar converter novamente (erro do 20201226 previsto)
# ============================================================
print("\n>>> Tentando converter novamente (deve dar erro do formato 20201226)...")
try:
    df2['Date'] = pd.to_datetime(df2['Date'], format='%Y/%m/%d')
except Exception as e:
    print("Erro previsto (20201226 sem formato):")
    print(e)

# ============================================================
# 11) Resolver erro do valor 20201226
# ============================================================

# Localizar valores com problema
mask = df2['Date'] == "20201226"
print("\nLinhas com problema 20201226:")
print(df2[mask])

# Converter esse valor manualmente
df2.loc[mask, 'Date'] = pd.to_datetime("2020/12/26", format='%Y/%m/%d')

# ============================================================
# 12) Agora converter toda coluna de uma vez
# ============================================================
df2['Date'] = pd.to_datetime(df2['Date'], format='%Y/%m/%d', errors='coerce')

print("\n=== Após conversão final da coluna Date ===")
print(df2)

# ============================================================
# 13) Remover valores nulos (somente a linha 22)
# ============================================================
df2 = df2.dropna()

print("\n=== DataFrame FINAL após remover nulos ===")
print(df2)
print("\n=== Informações finais ===")
print(df2.info())
