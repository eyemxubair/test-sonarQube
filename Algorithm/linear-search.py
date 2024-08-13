def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    else:
        return -1

arr = [2, 5, 8, 10, 16, 22, 25]
target = 22
result = search(arr, target)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")