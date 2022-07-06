def func_a(arr):
    counter = [0] * 1000
    for i in arr:
        counter[i] += 1
    return counter

def func_b(counter):
    max = 0
    for i in counter:
        if i > max:
            max = i
    return max

def func_c(counter):
    min = 1001
    for i in counter:
        if i !=0 and i < min:
            min = i
    return min

def solution(arr):
    counter = func_a(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt



def count(arr):
    counter = [0] * 1000
    max_cnt = 0
    min_cnt = 1000
    for i in arr:
        counter[i] = counter[i] + 1

    for j in counter:
        if j > max_cnt:
            max_cnt = j

    for k in counter:
        if k != 0 and k < min_cnt:
            min_cnt = k
    a = max_cnt // min_cnt
    return a

arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)
print(ret)

arr = [1, 2, 3, 3, 1, 7, 8, 6, 2, 5, 6, 8, 5, 7, 4, 7, 3, 7, 9, 7, 3]
ret = solution(arr)
print(ret)