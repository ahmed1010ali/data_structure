def binary_search(arr, value):
    arr.sort()
    first = 0
    last = len(arr) - 1 
    
    while first <= last:
        middle = (first + last) // 2 

        if arr[middle] == value:
            return True  
        elif arr[middle] < value:
            first = middle + 1  
        else:
            last = middle - 1 

    return False  


arr = [1, 5, 6, 9, 8, 7]
print(binary_search(arr, 5))  
print(binary_search(arr, 10))  
