from performanceStudyFunctions import *

#TODO:
#Encasulate

#Average test
executionTimes = []
averageExecutionTimes = 0
averageExecutionTimes = []
numberOfExecutions = 20 #MIN 10
arrayLengths = [100,200,300,400,500,600,700,800,900,1000]
distributions = ["poisson","random","binomial","geometric"]
algorithms = ["quickSort","selectionSort","insertionSort","shellSort","countingSort"]
        
for algorithm in algorithms:
    for distribution in distributions:
        for length in arrayLengths:
            for execution in range(0,numberOfExecutions):
                dataSet = createArray(distribution,length)
                executionTime = calcExecutionTime(algorithm,dataSet,False)
                executionTimes += [executionTime]
            
            averageExecutionTime = sum(executionTimes)/len(executionTimes)  
            averageExecutionTimes += [sum(executionTimes)/len(executionTimes)]
            
            print("Algorithm: " + algorithm + "|Distribution: " + distribution + 
                  "|length: " + str(length) + "|Avg Exec Time = " 
                  + str(averageExecutionTime) + " ms")
            
        #Create and save graphs with average execution times in Y axis and length in x axis
        #Clear Y axis data after creating graph since we want new Y datapoints 
        
        averageExecutionTimes = []
    
