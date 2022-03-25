def sum_pairs(ints, s):
    a = set()
    for i in ints:
        different = s - i
        if different in a:
            return [different, i]
        a.add(i)
