def solution(shirt_size):
    answer = [0] * 6
    for ss in shirt_size:
        if ss == 'XS':
            answer[0] += 1
        elif ss == 'S':
            answer[1] += 1
        elif ss == 'M':
            answer[2] += 1
        elif ss == 'L':
            answer[3] += 1
        elif ss == 'XL':
            answer[4] += 1
        elif ss == 'XXL':
            answer[5] += 1
            
    return answer

shirt_size = ['XS', 'S', 'L', 'L', 'XL', 'S']
ret = solution(shirt_size)

print(ret)
