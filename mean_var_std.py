import numpy as np

# Create a function that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
listinha=[0,1,2,3,4,5,6,7,8]
def calculate(lista:list):
    if len(lista)!=9:
        raise ValueError("List must contain nine numbers.")
    
    arr=np.array(lista) # tranform a list into an array
    arr3x3=np.reshape(arr,(3,3)) #reshape an 1D array to an 3D array
    #print(arr3x3)
    
    result={
        'mean':[list(np.mean(arr3x3,axis=0)),list(np.mean(arr3x3,axis=1)),np.mean(arr3x3)], 
        'variance':[list(np.var(arr3x3,axis=0)),list(np.var(arr3x3,axis=1)),np.var(arr3x3)],
       'standard deviation':[list(np.std(arr3x3,axis=0)),list(np.std(arr3x3,axis=1)),np.std(arr3x3)],
       'max':[list(np.max(arr3x3,axis=0)),list(np.max(arr3x3,axis=1)),np.max(arr3x3)],
       'min':[list(np.min(arr3x3,axis=0)),list(np.min(arr3x3,axis=1)),np.min(arr3x3)],
       'sum':[list(np.sum(arr3x3,axis=0)),list(np.sum(arr3x3,axis=1)),np.sum(arr3x3)],
       
     }
    return result
calculate(listinha)    