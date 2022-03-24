def persistence(n):
    answer = 0
    str_n = str(n)
    while len(str_n) !=1:
        result = 1
        for str_number in str_n:
            result *= int(str_number)
        str_n = str(result)
        answer += 1
    return answer
