def rotateLeft(d, arr):
    # print("Original array:",arr)
    for i in range(1,d+1):
        # print("Rotation - ",i,":")
        first_element = arr[0]
        for j in range(0,len(arr)-1):
           arr[j] = arr[j+1]
        arr[len(arr)-1] = first_element
        # print("new:")
        # print(arr)
        # print()
    return arr

rotation = 4
a = [1,2,3,4,5]
print(rotateLeft(rotation,a))