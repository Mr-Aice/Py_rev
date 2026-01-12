from typing import Final


#Powers
BLACK_WIDOW_POWER: Final[int] = 100
SPIDER_MAN_POWER: Final[int] = 150
CAPTIAN_AMERICA_POWER: Final[int] = 200
IRON_MAN_POWER: Final[int] = 250
THOR_POWER: Final[int] = 300
SUPER_MAN_POWER: Final[int] = 350


#Villian Power
Thanos_Power = 1000

#Message
MSG = print(
    f"""
    Thanos must be defeated.
    
    Please choose your pair to attack.

    1. Black Widow & Spiderman
    2. SpiderMan & Captain America
    3. Captain America & IRON Man
    4. Iron Man & Thor
    5. Thor & Superman
    
    """
)

WIN_MSG: Final[str] = "\n\nCongrats! You defeated Thanos!\n\n"
LOSS_MSG: Final[str] = "\n\nYour Maximum chances gone and Thanos Still standing!\n\n"

#Attack_Power Combined
def combined_power(ch):

    match ch:
        case 1:
            print("\n\nBlack Widow & Spiderman Attacking....")
            return int(BLACK_WIDOW_POWER + SPIDER_MAN_POWER)
        case 2:
            print("\n\nSpiderMan & Captain America Attacking....")
            return int(SPIDER_MAN_POWER + CAPTIAN_AMERICA_POWER)
        case 3:
            print("\n\nCaptain America & IRON Man Attacking....")
            return int(CAPTIAN_AMERICA_POWER + IRON_MAN_POWER)
        case 4:
            print("\n\nIron Man & Thor Attacking....")
            return int(IRON_MAN_POWER + THOR_POWER)
        case 5:
            print("\n\nThor & Superman Attacking....")
            return int(Thanos_Power + SUPER_MAN_POWER)
        case _:
            print("\n\nWrong Choice. Please try again.")
            return 0


#constraints
MAX_ATTACK = 3
attack_num = 0

choice = 0


while True:
    try:
        choice = int(input("Enter your pair Number: "))
    except:
        print("Wrong pair Entered. \n\nPlease try again...\n\n")
        continue
    Attack_power = combined_power(choice)
    Thanos_Power -= Attack_power
    attack_num += 1
    
    #logic



    if Thanos_Power <= 0 and attack_num <= MAX_ATTACK:
        #win
        print(WIN_MSG)
        break
    elif attack_num >= MAX_ATTACK:
        #Attempts 
        print(LOSS_MSG)
        break
    elif Attack_power == 0:
        attack_num -= 1
    else:
        print("\n\nThanos is injured... \n keep going...\n\n")

