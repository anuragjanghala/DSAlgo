arr = [2, 4, 3, 1, 7, 11]
arr.sort()
# 1 2 3 4 7 11
target = 14

start = 0
end = len(arr)-1
while (start < end):
    summ = arr[start]+arr[end]
    if(summ == target):
        print(arr[start], arr[end])
        break
    elif (summ > target):
        end -= 1
    else:
        start += 1
