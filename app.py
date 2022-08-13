import random

def dice_roller():
    roll = random.randint(1,6)
    while roll <= 6 and roll >= 0:
       option = input((str(roll) + " is your number. Would you like to reroll? (y/n)"))
       if option == "y":
            return dice_roller()
       else:
            break
        



    

    
        

dice_roller()


