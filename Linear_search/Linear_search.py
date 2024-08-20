def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  
arr=list(map(int,input("Enter the elements of the list: ").split()))
print(arr)
target = int(input("Enter the element you want to search for: "))
result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the list")
