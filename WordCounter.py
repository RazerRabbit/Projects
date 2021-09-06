# James Mueller
# Word Counter

def cleaner2(s):
    """cleaner2 parses a string input into a list of words without spaces, symbols, numbers or punctuation
    input: any string
    output: formatted lowercase words as list"""
    string = []
    Q = ""
    for t in s: # screening out of non-letters
        if str(t).isalpha()== True:
            string.append(t)
        elif str(t).isalpha() == False: # addition of space for indexing
            string.append(" ")
    for t in string: # lower case formatting
        Q += str(t).lower()
    Q = Q.split(" ") # separation into words
    while '' in Q:
        Q.remove('') # removal of empty list items       
    return(Q)
def wordCounter(tupl,file):
    """wordCounter counts the number of chosen words from a selected text file
    input: tupl - the list of words to check for/count (in tuple format)
           file - the filename string of the text file to be checked
    output: dict1 - a dictionary with the counted words as keys and their number of
                    instances as values"""
    text = open(file)
    string = text.read()
    word_list = cleaner2(string)
    dict1 = {} # new dictionary allotment 
    for key in tupl: # creation of keys with empty values 
        dict1[key] = 0    
    for word in word_list: # counter for dictionary values
        if word in dict1.keys():
            dict1[word] += 1
    return dict1
def dictionaryPrinter(d,file_name):
    """dictionaryPrinter prints an output statement for the number of instances of a given word from a text file
    input: d - a dictionary with words as keys and instances as values
           file_name - the string name of the text file being referenced 
    output: a print statement displaying the dictionary and its source"""
    key = []
    value = []
    for t in d: # extracts the keys from the dictionary and adds to list
        key.append(t)
    for t in d.values(): # extracts the values from dictionary and adds to list
        value.append(t)
    for t in range(0,len(d)): # print statement including key and corresponding value
        print("%s has %g instance(s) of the word '%s'." %((file_name), value[t], key[t]))
# Test Cases
check1 = ('and','at','my','with')
file1 = 'sonnet29.txt'
dictionaryPrinter(wordCounter(check1,file1),file1)
print('\n\n')
check2 = ('a','if','test','you')
file2 = 'tmbg.txt'
dictionaryPrinter(wordCounter(check2,file2),file2)




