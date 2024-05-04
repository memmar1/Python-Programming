my_list = [29,87,89,21,23,17,11,10,14]
my_target = 29
#in linear search we want to get 17, it checks the first index then lext until it reaches 17.
#then it returns the location if its not there it returns nul,
#it has a high time complexity

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    
    return -1



result = linear_search(my_list,my_target)

if result != -1:
    print(f"target {my_target} found at index {result}")
else:
    print(f"target {my_target} not found in the list")
