import random

def roll():
    return random.randint(1,6)


def holdAt20OrGoalTurn(score):
    
    turnTotal = 0

    while turnTotal < 20 and turnTotal + score < 100:
        die = roll()

        if die == 1:
            turnTotal = 0
            break
        else:
            turnTotal += die

    return turnTotal


def solitaireGame():

    score = 0
    turns = 0

    while score < 100:
        turn = holdAt20OrGoalTurn(score)
        score += turn
        turns += 1

    return turns


def averagePigTurns(games):

    totalTurns = 0

    for _ in range(games): #this will run the number of games specified
        totalTurns += solitaireGame()

    average = totalTurns / games
    return average

games = int(input("Games? ")) # input like 10000 for average calculation
avg = averagePigTurns(games)

print("Average turns:", avg)
