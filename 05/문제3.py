def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = day
    for i in range(0, month - 1, 1):
        total = total + month_list[i]
    return total

def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total
    
start_month1 = 1
start_day1 = 2
end_month1 = 2
end_day1 = 2
ret1 = solution(start_month1, start_day1, end_month1, end_day1)
print(ret1)

start_month2 = 5
start_day2 = 8
end_month2 = 11
end_day2 = 26
ret2 = solution(start_month2, start_day2, end_month2, end_day2)
print(ret2)