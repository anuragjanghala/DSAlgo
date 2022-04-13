arr = [5,3,2,1,3]
operations = [[0, 1], [1, 3]]

def performOperations(arr, operations):
    for s,e in operations:
    
        while s<e:
            arr[s], arr[e] = arr[e], arr[s]
            s+=1
            e-=1
            
    return arr
    
res = performOperations(arr, operations)
print(res)