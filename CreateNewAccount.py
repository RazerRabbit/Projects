# James Mueller
# Login Routine

import string
lc_letters = list(string.ascii_lowercase) # list of lower case letters
up_letters = list(string.ascii_uppercase) # list of upper case letters
characters = ['$','#','@','&','!','*'] # list of valid special characters 
users = {'kax2021','py_rocks','TAsRcool','thecakeisaLIE','AgentSmith'} # list of invalid usernames
c = 2 # counter to prevent re-entry into exited loop
print('Choose a login username. Your username should be unique and at least 6 characters long.')
while c > 0: # while loop for password prompt/check
    while c > 1: # while loop for username prompt/check
        newuser = input('\nNew username: ') # user prompt for username
        if newuser in users: # error message for duplicate username
            print('\nERROR: The username you entered is already taken. Please choose a different username.\n')
        elif len(newuser) < 6: # error message for short username
            print('\nERROR: The username you entered does not meet the 6 character minimum required length.\nPlease choose a different username.\n')
        else: # while loop exit for valid username
            users.add(newuser) # username added to invalid usernames
            new_account = [newuser] # archive created for new account
            c -= 1
            print('\nYour username has been accepted. \nWelcome %s!\n' %(newuser))
            print('\nChoose a login password. Your password must meet the requirements listed below:\n')
            break
    print('   - At least 1 lower case [a-z] and 1 upper case [A-Z] letter')
    print('   - At least 1 number [0-9]')
    print('   - At least 1 character [$ # @ & * !]')
    print('   - Minimum length 6 characters')
    print('   - Maximum length 16 characters\n')
    password = input('\nNew password: ') # user prompt for password
    lc = 0 # log for required elements 
    uc = 0
    dig = 0
    char = 0
    for x in password: # check/log inclusions of required elements 
        if x in lc_letters:
            lc += 1
        elif x in up_letters:
            uc += 1
        elif x.isdigit() == True:
            dig += 1
        elif x in characters:
            char += 1
    if len(password)<6 or len(password)>16: # error message for invalid length
        print('\nERROR: The password you entered does not meet the length requirements. \nPlease choose a different password.\n')
    elif lc==0 or uc==0 or dig==0 or char==0: # error message for missing element
        print('\nERROR: The password you entered does not meet the complexity requirements. \nPlease choose a different password.\n')
    else: # while loop exit for valid password
        new_account.append(password) # password added to account archive
        print('\nYour password has been accepted.')
        c -= 1
        break
print('\nYour registration is complete!')
print('You may now log in using the username "%s" and password "%s".' %(new_account[0],new_account[1]))






