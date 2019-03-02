''' Exceptions lesson 13
Ask user for sentence: #   this is a sentence
Ask user for number:   #  2
# a  (is printed, since it's index 2)
- catch exception for non-number
- catch exception for bad index
 '''

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

