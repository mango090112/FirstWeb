def solution(price, grade):
    if grade == 'S':
        answer = price * 95 / 100
    elif grade == 'G':
        answer = price * 90 / 100
    elif grade == 'V':
        answer = price * 85 / 100
    return answer

price1 = 2500
grade1 = 'V'
ret1 = solution(price1, grade1)

print(ret1)

price2 = 96900
grade2 = 'S'
ret2 = solution(price2, grade2)

print(ret2)
