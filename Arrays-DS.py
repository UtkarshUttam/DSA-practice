def reverseArray(a):
    newArr = []
    for i in range(0,len(a)):
        newArr.append(a[len(a)-(i+1)])
    return newArr   
        

Array1 = [1,4,3,2]
print(reverseArray(Array1))