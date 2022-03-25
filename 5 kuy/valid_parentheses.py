def valid_parentheses(string):
    dictionary = []
    for i in string:
        if i == '(':
            dictionary.append(i)
        elif i == ')':
            try:
                dictionary.pop()
            except Exception:
                return False
    if len(dictionary) == 0:
        return True
    else:
        return False
