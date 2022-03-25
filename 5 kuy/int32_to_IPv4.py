def int32_to_ip(int32):
    bin_string = f'{int32:b}'.rjust(32, '0')
    return '.'.join([str(int(bin_string[idx:idx + 8], 2)) for idx in range(0, len(bin_string), 8)])
