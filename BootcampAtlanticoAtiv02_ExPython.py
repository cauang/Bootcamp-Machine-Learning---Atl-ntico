# Questão 1: Função para retornar números ímpares de uma lista
def filtrar_impares(lista):
    
    lista_impares = []
    for num in lista:
        if num % 2 != 0: 
            lista_impares.append(num)
    return lista_impares


# Questão 2: Função para retornar números primos de uma lista
def eh_primo(num):

    if num <= 1:
        return False 
    for i in range(2, num):
        if num % i == 0:  
            return False
    return True 

def filtrar_primos(lista):

    lista_primos = []
    for num in lista:
        if eh_primo(num):
            lista_primos.append(num)
    return lista_primos  


# Questão 3: Função para retornar elementos exclusivos de duas listas
def elementos_exclusivos(lista1, lista2):

    exclusivos = []
    for item in lista1:
        if item not in lista2:  
            exclusivos.append(item)
    for item in lista2:
        if item not in lista1:  
            exclusivos.append(item)
    return exclusivos  


# Questão 4: Função para encontrar o segundo maior valor em uma lista
def segundo_maior(lista):

    lista_unica = list(set(lista))
    lista_unica.sort()  
    if len(lista_unica) < 2:
        return None  
    return lista_unica[-2]  


# Questão 5: Função para ordenar uma lista de tuplas por nome
def ordenar_por_nome(lista_tuplas):
    lista_tuplas.sort(key=lambda x: x[0])  
    return lista_tuplas 


# Questão 6: Completar código com Matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), layout="constrained")
for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
                               transform=axs[row, col].transAxes,
                               ha='center', va='center', fontsize=18,
                               color='darkgrey')
fig.suptitle('plt.subplots()')


# Questão 7: Completar código com NumPy e Matplotlib
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2 * np.pi, 2 * np.pi, 100)  
y = np.sin(x) 


fig, ax = plt.subplots()  
ax.plot(x, y)  
plt.show()  


# Questão 8: Leitura de um arquivo CSV com Pandas e exibição das primeiras linhas
import pandas as pd

def ler_csv(arquivo):

    df = pd.read_csv(arquivo) 
    print(df.head()) 

# Questão 9: Selecionar uma coluna específica e filtrar linhas com base em uma condição
def filtrar_coluna(arquivo, coluna_nome, condicao):

    df = pd.read_csv(arquivo)
    filtrado = df[df[coluna_nome] > condicao] 
    print(filtrado)  

# Questão 10: Lidando com valores ausentes (NaN) em um DataFrame
def tratar_nan(arquivo):

    df = pd.read_csv(arquivo)
    df.fillna(0, inplace=True)
    print(df)