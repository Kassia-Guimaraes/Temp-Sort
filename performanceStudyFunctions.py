import numpy as np
import time
from timeit import default_timer as timer
import random
from sortingAlgorithms import *

#TODO:
#add default case or Use empty array as error code 

def createArray(distribution,length):
    V = []

    for j in range(1,length+1):
        if (distribution == "random"):
            V += [random.randrange(1,101)]
        if (distribution == "poisson"):
            V += [np.random.poisson(100)]
        if (distribution == "binomial"):
            V += [np.random.binomial(100,0.5)]
        if (distribution == "geometric"):
            V += [np.random.geometric(0.01)]
            
    return V
  
def calcExecutionTime(algorithm, array,output, gaps = []):
    tot = 0.0
    #st = time.time_ns() / (10 ** 6)
    st = time.process_time()
    if(algorithm == "selectionSort"):  
        selectionSort(array)
    if(algorithm == "insertionSort"):  
        insertionSort(array)
    if(algorithm == "shellSort"):  
        shellSort(array, gaps)
    if(algorithm == "quickSort"):  
        quickSort(array,0,len(array)-1)
    if(algorithm == "countingSort"):  
        countingSort(array,len(array)-1, max(array))
    #en = time.time_ns() / (10**6)
    en = time.process_time()
    tot += (en-st)
    if output == True:
        print(algorithm + " execution time = "+str(tot)+" ms")
    return tot
    

