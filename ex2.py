def is_triangular_array(arr):
    if len(arr) < 3:
        return False
    arr.sort()
    for i in range(len(arr) - 2):
        if arr[i] + arr[i+1] > arr[i+2]:
            return True
    return False

arr = list(map(int, input("Enter Numbers: ").split()))
print(is_triangular_array(arr))
# שאלה 2