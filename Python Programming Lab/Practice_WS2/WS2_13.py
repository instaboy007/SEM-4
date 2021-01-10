word = "PARANORMAL"
guessed = "_" * len(word)
word = list(word)
guessed = list(guessed)
listGuessed = []
guessLetter= input("GUESS LETTER :")
while True:
    if guessLetter.upper() in listGuessed:
        guessLetter = ''
        print("ALREADY GUESSED!")
    elif guessLetter.upper() in word:
        index = word.index(guessLetter.upper())
        guessed[index] = guessLetter.upper()
        word[index] = '_'
    else:
        print(''.join(guessed))
        if guessLetter!='':
            listGuessed.append(guessLetter.upper())
        guessLetter= input("GUESS LETTER :")

    if '_' not in guessed:
        print("YOUR GUESS IS CORRECT")
        break