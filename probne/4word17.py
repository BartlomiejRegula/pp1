def licznik():
    word = 'You never get a second chance to make a first impression'
    count = 0
    for letter in word:
        if letter == 'e':
            count = count + 1
    print(count)
licznik()