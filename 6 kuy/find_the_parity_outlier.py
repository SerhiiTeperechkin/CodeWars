def find_outlier(integers):
    even_num = []
    odd_num = []
    for numb in integers:
        if numb % 2 > 0:
            odd_num.append(numb)
        elif numb % 2 == 0:
            even_num.append(numb)
    if len(even_num) > len(odd_num):
        return odd_num[0]
    else:
        return even_num[0]
