import pandas as pd
import numpy as np
import ast
import matplotlib.pyplot as plt

samples = pd.read_csv('./samples.csv', sep=',')
temp_exec = pd.read_csv('./temp_exec.csv', sep=',')

# Colocando o tempo para segundos
temp_exec['Time'] = temp_exec['Time']*60

# Calcular a média dos tempos de execução por combinação de 'Distribution', 'Array Length' e 'Ordenation'
mean_times = temp_exec.groupby(['Distribution', 'Array Length', 'Ordenation'])['Time'].mean().reset_index()

# Renomear a coluna da média para 'Mean Time'
mean_times.rename(columns={'Time': 'Mean Time'}, inplace=True)

# Junta a média de cada tipo de ordenação ao dataframe original
mean_temp = pd.merge(temp_exec, mean_times, on=['Distribution', 'Array Length', 'Ordenation'], how='left')

mean_temp.to_csv('./mean_temp.csv', sep=',', index=False)


for distribution in mean_temp['Distribution'].drop_duplicates().to_list():
    for ordenation in ['Selection Sort','Insertion Sort']:

        df = mean_temp[(mean_temp['Distribution']==distribution) &
                       (mean_temp['Ordenation']==ordenation)]
        
        df = df.drop_duplicates('Array Length')

        mean = df['Mean Time'].to_list()


        plt.plot(df['Array Length'].to_list(), mean, label=ordenation, marker='o')

    plt.title(f'Distribuição {distribution}')
    plt.xlabel('Tamanho do Array')
    plt.ylabel('Tempo de execução em segundos')

    plt.legend()
    plt.show()

for distribution in mean_temp['Distribution'].drop_duplicates().to_list():
    for ordenation in ['Shell Sort', 'Quick Sort','Quick Sort 2','Quick Sort 3','Counting Sort']:

        df = mean_temp[(mean_temp['Distribution']==distribution) &
                       (mean_temp['Ordenation']==ordenation)]
        
        df = df.drop_duplicates('Array Length')

        mean = df['Mean Time'].to_list()


        plt.plot(df['Array Length'].to_list(), mean, label=ordenation, marker='o')

    plt.title(f'Distribuição {distribution}')
    plt.xlabel('Tamanho do Array')
    plt.ylabel('Tempo de execução em segundos')

    plt.legend()
    plt.show()

for distribution in mean_temp['Distribution'].drop_duplicates().to_list():

    for ordenation in mean_temp['Ordenation'].drop_duplicates().to_list():

        df = mean_temp[(mean_temp['Distribution']==distribution) &
                       (mean_temp['Ordenation']==ordenation)]
        
        df = df.drop_duplicates('Array Length')

        mean = df['Mean Time'].to_list()


        plt.plot(df['Array Length'].to_list(), mean, label=ordenation, marker='o')

    plt.title(f'Distribuição {distribution}')
    plt.xlabel('Tamanho do Array')
    plt.ylabel('Tempo de execução em segundos')

    plt.legend()
    plt.show()

def calcDuplicated(df): # calcula a quantidade de duplicados em cada distribuição
    for element in df['Distribution'].drop_duplicates().to_list():
        list_element = df[df['Distribution'] == element]['Sample']
        for row in list_element:
            array = ast.literal_eval(row)
            not_duplicated = list(set(array))
            duplicated = len(array) - len(not_duplicated)
            
            print(f"Distruição: {element} - duplicados: {duplicated}")


calcDuplicated(samples)