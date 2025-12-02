import random

def roll():
    return random.randint(1, 6)


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


# ------------ Main Program ------------

p1Score = 0
p2Score = 0
currentPlayer = 1

while p1Score < 100 and p2Score < 100:
    
    # Display scores
    print("Player 1 score:", p1Score)
    print("Player 2 score:", p2Score)
    print("It is player", currentPlayer, "s turn.")

    # Run current player's turn
    if currentPlayer == 1:
        turn = holdAt20OrGoalTurn(p1Score)
        p1Score += turn
        currentPlayer = 2
    else:
        turn = holdAt20OrGoalTurn(p2Score)
        p2Score += turn
        currentPlayer = 1
