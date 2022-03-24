def printer_error(s):
    good = 'abcdefghijklmn'
    errors = 0
    total_letters = len(s)
    for letter in s:
        if letter not in good:
            errors += 1
    return f"{errors}/{total_letters}"
