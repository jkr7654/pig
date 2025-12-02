import random

def roll():
    return random.randint(1,6)

def holdAt20OrGoalTurn(score):

    turnTotal = 0
    
    # Roll until:
    #  - we pig (roll a 1), OR
    #  - we reach 20 for this turn, OR
    #  - the new score will reach at least 100
    
    while turnTotal < 20 and turnTotal + score < 100:
        die = roll()
        print("Roll:", die)
        
        if die == 1:
            turnTotal = 0
            break
        else:
            turnTotal += die

    print("Turn total:", turnTotal)
    print("New score:", score + turnTotal)

score = int(input("Score? "))  # input between 0 and 99
holdAt20OrGoalTurn(score)
