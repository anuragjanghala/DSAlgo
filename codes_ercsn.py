#days
dayslist = ['mon','tue','wed','thu','fri','sat','sun',]
day = 'mon'
n = 100
m = n%7
print(m)
for i,j in enumerate(dayslist):
    if j == day:
        ans = dayslist[(i+m)%7]
        print(ans)


#5
s = -15435

s_cpy = s
# print(s_cpy)

if s_cpy < 0:
    s_cpy*=-1
    
# print(s_cpy)
# print(s)

ans = []
temp = list(map(int, str(s_cpy)))
# print(temp)

for i in range(len(temp)):
    x = temp.copy()
    if temp[i] == 5:
        x.pop(i)
        substr = [str(i) for i in x]
        res = int(''.join(substr))*-1 if s < 0 else int(''.join(substr))
        # print(res)
        # print('         ')
        ans.append(int(res))
print(ans)


#-1 1
numArr = [5,6,12,-5,12,-13,-45,-66,-11]
x = 1
for i in numArr:
    x = x * i
print(x)


#+ -


#2*four

numlist = ['zero','one','two','three','four','five','six','seven','eight','nine']

x = "3*four"

num = int(x.split('*')[0])
letter = x.split("*")[1]
for i, j in enumerate(numlist):
    if letter == j:
        print(i*num)
