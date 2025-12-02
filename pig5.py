import random

def roll():
    return random.randint(1,6)

def holdAt20OrGoalTurn(score):
    
    turnTotal = 0

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

    return turnTotal

score = 0

while score < 100:
    turn = holdAt20OrGoalTurn(score)
    score += turn
