import random

def roll():
    return random.randint(1,6)

def holdAtXTurn(limit): #this function will simulate a hold-at-X turn
    turnTotal = 0
    
    while turnTotal < limit:
        die = roll()
        
        if die == 1:
            turnTotal = 0
            break
        else:
            turnTotal += die
            
    return turnTotal


def holdAtXOutcomes(trials, limit): #they will simulate how many times each score occurs

    scores = {}

    for _ in range(trials):
        turnTotal = holdAtXTurn(limit)
        
        if turnTotal in scores:
            scores[turnTotal] += 1
        else:
            scores[turnTotal] = 1

    print("Score\tEstimated Probability")

    for s in sorted(scores.keys()):
        print(s, scores[s] / trials, sep="\t") #then this will print the score and probability

trials = int(input("How many Hold-at-X turn simulations? ")) #input like 100000
limit = int(input("Hold-at what value? ")) #input like 20 for hold 

holdAtXOutcomes(trials, limit)

