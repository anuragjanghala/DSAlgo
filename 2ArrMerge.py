arr1 = [3,6,7,10,12,15]
arr2 = [1,4,8,9,11,]

s1 = 0
s2 = 0

arrMerged = []
i=0
while ( i < len(arr1) + len(arr2) ):
    if(s1==len(arr1) and s2<len(arr2)):
        arrMerged.append(arr2[s2])
        i+=1
        s2+=1
    elif(s1<len(arr1) and s2==len(arr2)):
        arrMerged.append(arr1[s1])
        i += 1
        s1 += 1
    else:
        if(arr1[s1]<arr2[s2]):
            arrMerged.append(arr1[s1])
            i+=1
            s1+=1
        else:
            arrMerged.append(arr2[s2])
            i+=1
            s2+=1

print(arrMerged)