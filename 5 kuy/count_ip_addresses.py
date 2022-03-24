def ips_between(start, end):
    start_list = [int(s) for s in start.split('.')]
    end_list = [int(e) for e in end.split('.')]
    pwr = [3, 2, 1, 0]
    res = 0
    for i in range(4):
        res += (end_list[i] - start_list[i]) * (256 ** pwr[i])
    return res


# ips_between("10.0.0.0", "10.0.0.50")
