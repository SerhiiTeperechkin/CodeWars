def next_bigger(n):
    if str(n) == ''.join(sorted(str(n))[::-1]):
        return -1
    new_n = n
    while True:
        new_n += 1
        if sorted(str(new_n)) == sorted(str(n)):
            return new_n
