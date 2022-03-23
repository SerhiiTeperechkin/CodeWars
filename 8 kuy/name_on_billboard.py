def billboard(name, price=30):
    res = 0
    for i in name:
        res += price
    return res
