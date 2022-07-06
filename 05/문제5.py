def solution(arr):
    l = len(arr)
    a = [0] * l
    for i in range(0, l, 1):
        a[i] = arr[l-1-i]
    return a

def solution2(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [1, 4, 2, 3]
ret = solution(arr)
print(ret)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ret = solution(arr)
print(ret)

arr = [1, 4, 2, 3]
ret = solution2(arr)
print(ret)
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ret = solution2(arr)
print(ret)