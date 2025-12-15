arr=[]
arr1=[]
arr2=[]
for i in range(0,10):
    arr.append(i)
print(arr)
for i in range(0,9):
    if(arr[i]%2==0):
        arr1.append(arr[i])
print(arr1)
for i in range(0,9):
    if(arr[i]%2!=0):
        arr2.append(arr[i])
print(arr2)