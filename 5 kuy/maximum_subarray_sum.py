def max_sequence(arr):
    sums = []
    for a, b in enumerate(arr):
        sums.append(b)
        for i in range(a + 1, len(arr)):
            b += arr[i]
            sums.append(b)
    if all(i < 0 for i in arr) or not sums:
        return 0
    else:
        return max(sums)
