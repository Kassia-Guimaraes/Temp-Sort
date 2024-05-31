import time
import random
import pandas as pd
import numpy as np
import ast

#Gera dataframes para alocar as informações das distribuições e tempos
samples = pd.DataFrame(columns=['Index','Distribution','Sample'])
temp_exerc = pd.DataFrame(columns=['Distribution','Ordenation','Array Length','Time'])


def selectionSort(V):

    for i in range(0, len(V)-1):
        min = i
        for j in range(i+1, len(V)):
            if (V[min] > V[j]):
                min = j
            V[min], V[j] = V[j], V[min]

def insertionSort (V):
    N = len(V)
    for j in range(1,N):
        key = V[j]
        i = j - 1
        while (i >= 0 and V[i] > key):
            V[i+1] = V[i]
            i -= 1
        V[i+1] = key

def shellSort (V, gaps):
    N = len(V)
    for h in gaps:
        for i in range(h, N):
            key = V[i]
            j = i
            while( j >= h and V[j - h] > key ):
                V[j] = V[j - h]
                j -= h
            V[j] = key
     
def quickSort (V, i, f):
    if(i < f):    
        pivot = partition(V,i,f)
        quickSort(V, i, pivot-1)
        quickSort(V, pivot+1, f)

# particao de Lomuto (mais simples)
def partition (V, i, f):
    # choose the rightmost element as pivot
    pivot = V[i]
 
    # pointer for greater element
    a = i
 
    # traverse through all elements
    # compare each element with pivot
    for b in range(i+1, f+1):
        if V[b] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            a = a + 1
 
            # Swapping element at a with element at b
            (V[a], V[b]) = (V[b], V[a])
 
    # Swap the pivot element with the greater element specified by a
    (V[a], V[i]) = (V[i], V[a])
 
    # Return the position from where partition is done
    return a 

def quickSort2(V, i, f):
    if(i < f):    
        pivot = partition2(V,i,f)
        quickSort2(V, i, pivot-1)
        quickSort2(V, pivot+1, f)

# tipicamente faz 3 x menos swaps que Lomuto...
def partition2(V, i, f):
    p = V[i]  # pivot no leftmost
    a = i
    b = f + 1
    # atravessar array e comparar com pivot
    while(True):
        while(True):
            a += 1
            if(a > f or V[a] >= p): break   # until
        while(True):
            b -= 1
            if(b < i or V[b] <= p): break  # until

        if(a >= b): break    # until
        V[a], V[b] = V[b], V[a]

    V[b], V[i] = V[i], V[b]
    return b      # retorna pos do pivot

def quickSort3(A, i, f):
	if(i >= f):
		return
	k = random.randint(i, f) # escolhe pivot
	A[k], A[i] = A[i], A[k]
	me, ma = partition3(A, i, f)
	quickSort3(A, i, me - 1)
	quickSort3(A, ma + 1, f)

def partition3(A, i, f):       # particao ideal para listas com poucos duplicados
    menors = i       # menores que pivot
    x = i
    maiors = f       # maiores que pivot
    pivot = A[i]     # pivot ccomo o primeiro do array (random na funcao QS3)
    while (x <= maiors):      # a comecar no primeiro elemento
        if(A[x] < pivot):
            A[menors], A[x] = A[x], A[menors]
            menors += 1
            x += 1
        elif(A[x] > pivot):
            A[x], A[maiors] = A[maiors], A[x]
            maiors -= 1
        else:
            x += 1	
    return menors, maiors         # agora retorna dois indices!

def countingSort(A, N, k):   # assume-se que A[1..N]
    # faz array B[]
    B = [0]
    for i in range(1,N+1):
        B += [0]
    C = [0]
    for i in range(1,k+1):
        C += [0]

    for i in range(1,N+1):
        C[A[i]] += 1
    for i in range(1,k+1):  # acumulado!
        C[i] += C[i-1]
    for j in range(N,0,-1):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1

    return B

def arrays(df): # gera as amostras de acordo com a distribuição
         
    for i in range(1, 21):

        V = []
        length = 750
        for j in range(1,length+1):
            V += [random.randrange(1,101)]
        new_row = pd.DataFrame({'Index':i, 'Distribution':'Random', 'Sample': [V]})
        df = pd.concat([df, new_row], ignore_index=True)

        # Distribuição de Poisson
        V = []
        for j in range(1,length+1):
            V += [np.random.poisson(100)]
        new_row = pd.DataFrame({'Index':i, 'Distribution':'Poisson', 'Sample': [V]})
        df = pd.concat([df, new_row], ignore_index=True)

        # Distribuição Binomial
        V = []
        for j in range(1,length+1):
            V += [np.random.binomial(200,0.5)]
        new_row = pd.DataFrame({'Index':i, 'Distribution':'Binomial', 'Sample': [V]})
        df = pd.concat([df, new_row], ignore_index=True)

        # Distribuição Geometrica
        V = []
        for j in range(1,length+1):
            V += [np.random.geometric(0.01)]
        new_row = pd.DataFrame({'Index':i, 'Distribution':'Geometric', 'Sample': [V]})
        df = pd.concat([df, new_row], ignore_index=True)

    df.to_csv('./samples.csv', sep=',',index = False)
    return df

def ordenationTimes(V, temp_exerc, length, distr): #gera o tempo de execucação de cada algoritmo
    # benchmark
    tot = 0.0
    for i in range(1,100):
        A = V.copy()
        st = time.process_time()
        selectionSort(A)
        en = time.process_time()
        tot += (en-st)
    new_row = pd.DataFrame({'Distribution':[distr],'Ordenation':['Selection Sort'], 'Array Length':[length], 'Time':[tot]})
    temp_exerc = pd.concat([temp_exerc, new_row], ignore_index=True)
    print("Insertion Sort  time="+str(tot))

    tot = 0.0
    for i in range(1,100):
        A = V.copy()
        st = time.process_time()
        insertionSort(A)
        en = time.process_time()
        tot += (en-st)
    new_row = pd.DataFrame({'Distribution':[distr],'Ordenation':['Insertion Sort'], 'Array Length':[length], 'Time':[tot]})
    temp_exerc = pd.concat([temp_exerc, new_row], ignore_index=True)
    print("Insertion Sort  time="+str(tot))

    tot = 0.0
    for i in range(1,100):
        A = V.copy()
        st = time.process_time()
        shellSort(A, gaps=[701,301,132,57,23,10,4,1])
        en = time.process_time()
        tot += (en-st)
    new_row = pd.DataFrame({'Distribution':[distr],'Ordenation':['Shell Sort'], 'Array Length':[length], 'Time':[tot]})
    temp_exerc = pd.concat([temp_exerc, new_row], ignore_index=True)
    print("Shell Sort  time="+str(tot))

    tot = 0.0
    for i in range(1,100):
        A = V.copy()
        st = time.process_time()
        quickSort(A, 0, len(A)-1)
        en = time.process_time()
        tot += (en-st)
    new_row = pd.DataFrame({'Distribution':[distr],'Ordenation':['Quick Sort'], 'Array Length':[length], 'Time':[tot]})
    temp_exerc = pd.concat([temp_exerc, new_row], ignore_index=True)
    print("Quick Sort  time="+str(tot))

    tot = 0.0
    for i in range(1,100):
        A = V.copy()
        st = time.process_time()
        quickSort2(A, 0, len(A)-1)
        en = time.process_time()
        tot += (en-st)
    new_row = pd.DataFrame({'Distribution':[distr],'Ordenation':['Quick Sort 2'], 'Array Length':[length], 'Time':[tot]})
    temp_exerc = pd.concat([temp_exerc, new_row], ignore_index=True)
    print("Quick Sort2  time="+str(tot))

    tot = 0.0
    for i in range(1,100):
        A = V.copy()
        st = time.process_time()
        quickSort3(A, 0, len(A)-1)
        en = time.process_time()
        tot += (en-st)
    new_row = pd.DataFrame({'Distribution':[distr],'Ordenation':['Quick Sort 3'], 'Array Length':[length], 'Time':[tot]})
    temp_exerc = pd.concat([temp_exerc, new_row], ignore_index=True)
    print("Quick Sort3  time="+str(tot))

    tot = 0.0
    for i in range(1,100):
        A = V.copy()
        st = time.process_time()
        countingSort(A, len(A)-1, max(A))
        en = time.process_time()
        tot += (en-st)
    new_row = pd.DataFrame({'Distribution':[distr],'Ordenation':['Counting Sort'], 'Array Length':[length], 'Time':[tot]})
    temp_exerc = pd.concat([temp_exerc, new_row], ignore_index=True)
    print("Counting Sort  time="+str(tot))

    temp_exerc.to_csv('./temp_exec.csv', sep=',', index=False)
    return temp_exerc

def createTemp(df): # adiciona ao CSV os tempos de excecução
    df1 = pd.DataFrame()

    for element in df['Distribution'].drop_duplicates().to_list(): #Dá o nome da distribuição utilizado

        list_element = df[df['Distribution']==element]['Sample'].to_list() #gera lista 

        for array in list_element:
            for i in range(49,750,50):
                to_order = array[0:i]
                df2 = ordenationTimes(to_order, temp_exerc, i+1,element)
                df1 = pd.concat([df1, df2], ignore_index=True)

    df1.to_csv('./temp_exec.csv', sep=',', index=False)
    return df1

#Para gerar as amostras de acordo com as distribuições
distributions = arrays(samples)

#Para calcular o tempo de cada ordenação 
createTemp(distributions)