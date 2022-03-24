from math import sqrt, pow

def find_next_square(sq):
    if sq % sq ** 0.5 == 0:
        return pow((sqrt(sq) + 1), 2)
    else:
        return -1
