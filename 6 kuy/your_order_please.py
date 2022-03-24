def order(sentence):
    words = sentence.split()
    numbers = range(1,10)
    result = []
    for number in numbers:
        str_number = str(number)
        for word in words:
            if str_number in word:
                result.append(word)
    return ' '.join(result)
