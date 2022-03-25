times = [('year', 365 * 24 * 60 * 60),
     ('day', 24 * 60 * 60),
     ('hour', 60 * 60),
     ('minute', 60),
     ('second', 1)]

def format_duration(seconds):
    if not seconds:
        return 'now'
    chks = []
    for name, secs in times:
        quantity = seconds // secs
        if quantity:
            if quantity > 1:
                name += 's'
            chks.append(f"{str(quantity)} {name}")
        seconds = seconds % secs 
    return ', '.join(chks[:-1]) + ' and ' + chks[-1] if len(chks) > 1 else chks[0]
