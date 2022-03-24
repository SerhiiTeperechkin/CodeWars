def get_count(sentence):
    count = 0
    for a in sentence.lower():
        if a in "aeiou":
            count +=1
    return count
