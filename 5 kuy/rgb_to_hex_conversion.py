def rgb(r, g, b):
    def convert(num):
        map = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
        template = ''
        if num <= 0:
            return '00'
        elif num >= 255:
            return 'FF'
        while num > 0:
            num, mod = divmod(num, 16)
            template += map[mod]
        return template[::-1] if len(template) == 2 else '0' + template
    return convert(r) + convert(g) + convert(b)
