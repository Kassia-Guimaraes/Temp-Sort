from performanceStudyFunctions import *
import pandas as pd
import matplotlib.pyplot as plt

#TODO:
#Encasulate

#Average test
executionTimes = []
averageExecutionTimes = 0
averageExecutionTimes = []
numberOfExecutions = 20 #MIN 10
arrayLengths = range(50,751,50)
distributions = ["poisson","random","binomial","geometric"]
algorithms = ["quickSort","selectionSort","insertionSort","shellSort","countingSort"]
df = pd.DataFrame()

for algorithm in algorithms:
    for distribution in distributions:
        for length in arrayLengths:
            for execution in range(0,numberOfExecutions):
                dataSet = createArray(distribution,length)
                executionTime = calcExecutionTime(algorithm,dataSet,False,[701,301,132,57,23,10,4,1])
                executionTimes += [executionTime]
            
            averageExecutionTime = sum(executionTimes)/numberOfExecutions
            executionTimes = []
            averageExecutionTimes += [averageExecutionTime]
            new_row = pd.DataFrame({'Distribution':[distribution],'Ordenation':[algorithm], 'Array Length':[length], 'Time':[averageExecutionTime]})
            df = pd.concat([df, new_row], ignore_index=True)
            print("Algorithm: " + algorithm + "|Distribution: " + distribution + 
                  "|length: " + str(length) + "|Avg Exec Time = " 
                  + str(averageExecutionTime) + " s")
        
        
        #Create and save graphs with average execution times in Y axis and length in x axis
        #Clear Y axis data after creating graph since we want new Y datapoints 
        
    averageExecutionTimes = []
    
df.to_csv('./executionTimes.csv', sep=',', index=False)
    
 # Plotagem dos gráficos
for algorithm in algorithms:
    plt.figure(figsize=(12, 8))
    for distribution in distributions:
        subset = df[(df['Ordenation'] == algorithm) & (df['Distribution'] == distribution)]
        plt.plot(subset['Array Length'], subset['Time'], label= distribution)
    
    plt.title(f'Tempos Médios de Execução para {algorithm}')
    plt.xlabel('Tamanho do Array')
    plt.ylabel('Tempo Médio de Execução (s)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Plotagem dos gráficos
for distribution in distributions:
    plt.figure(figsize=(12, 8))
    for algorithm in algorithms:
        subset = df[(df['Distribution'] == distribution) & (df['Ordenation'] == algorithm)]
        plt.plot(subset['Array Length'], subset['Time'], label= algorithm)
    
    plt.title(f'Tempos Médios de Execução para {distribution}')
    plt.xlabel('Tamanho do Array')
    plt.ylabel('Tempo Médio de Execução (s)')
    plt.legend()
    plt.grid(True)
    plt.show()
    

# Função para calcular a frequência dos valores
def calculate_frequencies(data):
    rounded_data = np.round(data, decimals=2)  # Arredondar os valores
    return Counter(rounded_data)  # Contar a frequência dos valores

# Função para plotar os histogramas das frequências
def plot_frequencies(frequencies, distribution):
    values = list(frequencies.keys())
    counts = list(frequencies.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(values, counts, width=0.1 if distribution != 'poisson' else 0.5)
    plt.title(f'Frequência dos Valores - Distribuição {distribution.capitalize()}')
    plt.xlabel('Valores')
    plt.ylabel('Frequência')
    plt.show()
    
# Parâmetros
length = 750  # Tamanho do dataset
distributions = ["gaussian", "uniform", "poisson", "beta"]

# Gerar dados para cada distribuição
data_sets = {dist: generate_data(dist, length) for dist in distributions}

# Calcular a frequência dos valores para cada distribuição
frequencies = {dist: calculate_frequencies(data) for dist, data in data_sets.items()}

# Exibir as frequências e plotar os histogramas
for dist, freq in frequencies.items():
    print(f"\nFrequências para a distribuição {dist}:")
    for value, count in freq.items():
        print(f"Valor: {value}, Frequência: {count}")
    plot_frequencies(freq, dist)