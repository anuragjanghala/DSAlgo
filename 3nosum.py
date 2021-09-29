arr = [2,4,3,1,7,11]
arr.sort()
# 1 2 3 4 7 11
target = 13

for i,val in enumerate(arr):
    checksum = target-val;
    start=i+1
    end=len(arr)-1
    while (start<end):
        summ = arr[start]+arr[end]
        if(summ == checksum):
            print(val,arr[start],arr[end])
            break
        elif (summ>checksum):
            end -=1
        else:
            start +=1
