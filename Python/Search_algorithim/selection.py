
def selectionsort(arr):
    sorted_arr = []
    while len(arr)>0:
        min_ = float("inf")
        for i in arr:
            if i < min_:
                min_ = 1
        sorted_arr.append(min_)
        arr.remove(min_)
    return sorted_arr

arr = [67,12,23,1,5,56,34]
print(selectionsort(arr))