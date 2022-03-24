def find_it(seq):
    numb_seq = len(seq)
    for x in range(0, numb_seq):
        count = 0
        for y in range(0, numb_seq):
            if seq[x] == seq[y]:
                count += 1
        if count % 2 == 1:
            return seq[x]
