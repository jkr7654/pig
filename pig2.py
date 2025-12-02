import random

def roll():
    return random.randint(1,6)

def holdAt20Turn():
    turnTotal = 0
    
    while turnTotal < 20:
        die = roll()
        if die == 1:
            turnTotal = 0
            break
        else:
            turnTotal += die
            
    return turnTotal

def holdAt20Outcomes(trials):
    
    scores = {}

    for _ in range(trials):
        turnTotal = holdAt20Turn() #call
        
        if turnTotal in scores:
            scores[turnTotal] += 1 # if successful, add one
        else:
            scores[turnTotal] = 1 # if not, set back to one

    print("Score\tEstimated Probability")
    
    for s in sorted(scores.keys()):
        print(s, scores[s] / trials, sep="\t") #tab-separated and print a=score and probability 

trials = int(input("Hold-at-20 turn simulations? ")) # input any total number of trials like 100000
holdAt20Outcomes(trials)
