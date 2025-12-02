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


# ----- Human turn (user chooses Roll or Hold) -----
def humanTurn(score):

    turnTotal = 0

    while True:

        die = roll()
        print("Roll:", die)

        if die == 1:
            turnTotal = 0
            break
        else:
            turnTotal += die

        # Prompt human after each non-pig roll
        decision = input(f"Turn total: {turnTotal}\tRoll/Hold? ")

        if decision != "":
            break

        # stop automatically if goal reached
        if turnTotal + score >= 100:
            break

    print("Turn total:", turnTotal)
    print("New score:", score + turnTotal)

    return turnTotal



# Randomlychoose the user's player number
userPlayer = random.randint(1,2)

print("You will be player", userPlayer, ".")
print("Enter nothing to roll; enter anything to hold.")

p1Score = 0
p2Score = 0
currentPlayer = 1


while p1Score < 100 and p2Score < 100:

    print("Player 1 score:", p1Score)
    print("Player 2 score:", p2Score)
    print("It is player", currentPlayer, "'s turn.")

    if currentPlayer == 1:
        if userPlayer == 1:
            turn = humanTurn(p1Score)
        else:
            turn = holdAt20OrGoalTurn(p1Score)

        p1Score += turn
        currentPlayer = 2

    else:
        if userPlayer == 2:
            turn = humanTurn(p2Score)
        else:
            turn = holdAt20OrGoalTurn(p2Score)

        p2Score += turn
        currentPlayer = 1
