# Exceptions lesson 13

while True:
    sent = input ("Enter a sentance: ")
    if sent == '': # empty input
        break

    print (sent)
    try:
        ind = int(input("Enter the word index 0..n:")) # expect and integer
    except (ValueError) as e:
        print("(Error due to non integer)", e)
    else:
        try:
            word_selected = sent.split(' ')[ind]
        except (IndexError) as e:
            print("(Error due to wrong index)", e)
        else:
            print ("Selected word is ", word_selected)

