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

# original de Hoare. produz melhores particoes (mais estaveis).
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
