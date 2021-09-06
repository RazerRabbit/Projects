# James Mueller
# Rock, Paper, Scissors

import random
def rps(a,b):
    """rps is a function that computes the winner of a rock, paper, scissors game
    Inputs: a,b - both inputs must be formatted as 'r', 'p', or 's'
    Output: returns the winner - 'a', 'b', or 'd' for draw."""   
    c = a+b # variable to derive missing weapon
    ro = 0 # weight of rock
    pa = 0 # weight of paper
    sc = 0 # weight of scissors
    if 'r' not in c: # paper and scissors match 
        sc += 1
    elif 'p' not in c: # rock and scissors match
        ro += 1
    elif 's' not in c: # rock and paper match
        pa += 1
    if a == 'r': # assigns weighted variable by identity 
        a = ro
    elif a == 'p':
        a = pa
    else:
        a = sc
    if b == 'r': # assigns weighted variable by identity 
        b = ro
    elif b == 'p':
        b = pa
    else:
        b = sc
    if a > b: # determines/returns winner or draw status
        return 'a'
    elif a < b:
        return 'b'
    else:
        return 'd'
p1_weapons = ['ROCK', 'PAPER', 'SCISSORS'] # list of valid user inputs/game outputs
npc_weapons = ['r','p','s'] # npc weapons choice codes for function
lose = ['As you stoop to pet a kitten, it hisses. You LOSE, warrior.','You realize too late that the green handle is diesel. You LOSE, warrior.','Smoke rises from the clearing: Fire Nation soldiers. You LOSE, warrior.','It is too early for bed, and too late for coffee. You LOSE, warrior.',"The giant spider that you didn't kill is nowhere to be seen. You LOSE, warrior.",'You wake up surrounded by golden fields. Do you remember who you were? You were a warrior, and you LOST.']
win = ["A pretty girl you don't know smiles at you. You WIN!",'You remembered to save your work before the blue screen. You WIN!','Only one left in stock. You WIN!',"Your neighbors' angry teenager decided not to buy the drumset. You WIN!",'Daylight savings starts tonight, and this time you gain an hour. You WIN!',"The Jehova's Wittnesses have just arrived at your old address. You WIN!",'You were wearing shoes when you stepped on the LEGO. You WIN!']
draw = ["Neither you, nor the co-worker who sometimes parks in your spot got the promotion. It's a DRAW.","Your coffee is on the house, but it tastes like Folgers. It's a DRAW.","You buy the healthiest item from the fast food menu. It's a DRAW.","The person ahead of you in line at the grocery store has only a single item to pay for, but then gets out a checkbook. It's a DRAW.","You finally get to sleep in on the same day the lanscaping company decides to do your yard. It's a DRAW."]
print("Welcome to 'Rock, Paper, Scissors for Windows 95'!") 
match = 1 # match count
scores = {'p1_score':0,'npc_score':0,'draws':0} # score dictionary 
t = 0 # loop open
while t < 1:
    npc = random.choice(npc_weapons) # random npc weapon choice
    if npc == 'r':
        np = p1_weapons[0] # npc full weapon name
    elif npc == 'p':
        np = p1_weapons[1]
    else:
        np = p1_weapons[2]
    p1 = input('\nChoose your weapon!\n') # user prompt for weapon choice
    if p1.upper() not in p1_weapons: # check for validity 
        print('You must choose <rock>, <paper>, or <scissors>. Choose wisely, warrior.')
    else:
        print('Prepare for battle, mortal!')
        print('\n\n...........................Ready..................')
        print('\n\n................................................Aim.........................')
        print('\n\n............................................................................GO!!')
        if p1.upper() == 'ROCK': # user weapon choice convert to code for function
            p = 'r'
        elif p1.upper() == 'PAPER':
            p = 'p'
        elif p1.upper() == 'SCISSORS':
            p = 's'
        x = rps(p,npc) # function call to solve for winner/draw
        print('\n   ****** You chose ' + p1.upper() + ', and your enemy chose ' + np + '. ******\n') # weapon reveal  
        if x == 'a':
            print(random.choice(win)) # random win statement
            scores['p1_score'] += 1 # user win score update
        elif x == 'b':
            print(random.choice(lose)) # random loss statement
            scores['npc_score'] += 1 # npc win score update
        elif x == 'd':
            print(random.choice(draw)) # random draw statement
            scores['draws'] += 1 # draw score update
        print('-----------------------------------------------------------------------------------------')
        print('\n\nYour noble enemy wishes to engage in another battle. Will you accept the challenge?')
        q = input('\nIf you are brave, press <y>, but if you are cowardly, consider pressing <n>: ') # user prompt to play again
        if q == 'n': # end game and display stats
            t += 1 # loop close
            print('\nYou may spare yourself the battle now, warrior, but battles may not always spare you.\n')
            print('\n**** Out of %g battle(s), you were victorious in %g and failureious in %g, with a total of %g tie(s). ****' %(match,scores['p1_score'],scores['npc_score'],scores['draws']))  
            if scores['p1_score'] > scores['npc_score']:
                print('You have won the war, brave warrior.\nMore battles may lie ahead, but for now, treat yourself to some ice cream.')
            else:
                print('You fought bravely, warrior, but you have lost.\nYour name will be forgotten, your deeds struck from history, and you will die alone.')
                break
            break
        elif q == 'y': # play another game
            print('Your bravery has not gone unnoticed, warrior. Heroes and gods alike watch from Valhalla.')
            match += 1 # match count update

            
        
        
            
        
    
