def move_zeros(array):
    if len(array) == 0:
        return []
    c = 0 
    for i in range(len(array)):
        if array[i] != 0:
            array[c] = array[i]
            c += 1
    for j in range(c, len(array)):
        array[j] = 0
    return array
