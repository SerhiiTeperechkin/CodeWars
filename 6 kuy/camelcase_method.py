def camel_case(string):
    res = string.replace('-', ' ').replace('_', ' ')
    res = res.split()
    if len(string) == 0:
        return string
    return res[0].capitalize() + ''.join(i.capitalize() for i in res[1:])
