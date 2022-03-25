def pig_it(text):
    pig_text = ' '
    for word in text.split(' '):
        if word in '!.%&?':
            pig_text = pig_text + word
        else:
            pig_word = word[1:] + word[0] + 'ay'
            pig_text = pig_text + pig_word + ' '
    return pig_text.strip(' ')
