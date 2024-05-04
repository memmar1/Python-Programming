arr = [67,12,23,1,5,56,34]
sorted = False

while sorted == False:
    sorted = True
    for i in range(len(arr)-1):
         if arr[i]>arr[i+1]:
            a = arr[i+1]
            arr[i+1]= arr[i]
            arr[i]= a
            sorted =False
print (arr)