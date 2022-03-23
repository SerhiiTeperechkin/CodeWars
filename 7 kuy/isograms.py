def is_isogram(string):
    word = string.lower()
    return True if word and len(set(word)) == len(word) or len(word) == 0 else False
