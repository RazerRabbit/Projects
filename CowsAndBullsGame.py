# James Mueller
# Bulls and Cows Game

import random
code = [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)] # random digits for code
print("Let's play 'Bulls and Cows'!\n\nA secret 4-digit code stands between you and everything you've ever wanted.\nCan you crack the code?\n\nA BULL means you guessed a digit correctly!\nA COW means the digit is correct, but in the wrong place.\n\nGuess the code or press <Q> to quit.")
x = 0 # key for loop
tries = 0 # counter for number of tries 
while x == 0: # enter loop
    guess = [] # list holding code guess 
    y = input('\nGuess the 4-digit code: ') # user prompt for code
    print('\n')
    if str(y.lower()) == 'q': # loop termination by user
        print("\nThank you for playing 'Bulls and Cows'.\nMay bulls and cows be with you always.\n\nGoodbye.")
        x += 1 # exit loop
        break
    else:
        z = str(y) # user input converted to string for checking
        if len(z) != 4: # length check
            print('You must guess four digits - no more and no less. Try again.')
        for dig in z: # letter/symbol check
            if dig.isdigit() == False:
                print('You must enter integers between 0 and 9 only. Try again.')
            else: # user input converted back to integer and stored in list
                dig = int(dig)
                guess.append(dig)       
        tries += 1 # attempt logged
        digt = 0 # counter for indexing because conventional method was problematic 
        bulls = 0 # counter for correct digits to track win
        for t in range(0,len(guess)):
            digt +=1
            if (code[t]-guess[t]) == 0: # check each digit for match
                print('Excellent! You have a BULL at position %g!' %(digt))
                bulls += 1
            elif guess[t] in code: # check for occurrence in code
                print("Just so you know, you've got a COW at position %g." %(digt))
        if bulls < 4: # no win yet
            print('Keep trying!')
        else: # win
            print('\nCongratulations! You guessed the secret code! \nWith a little bovine providence you were able to guess it in only '+str(tries)+' tries, too!') 
            print("You may now have everything you ever wanted.") # close joke loop
            x += 1 # exit loop




