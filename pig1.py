import random

def roll():
    return random.randint(1, 6)

def holdAt20Turn():
    turnTotal = 0
    
    while turnTotal < 20:
        die = roll()
        print("Roll:", die)
        
        if die == 1:            # Pig roll
            turnTotal = 0
            break
        else:
            turnTotal += die

    print("Turn total:", turnTotal)

# Run one automated turn
holdAt20Turn()
