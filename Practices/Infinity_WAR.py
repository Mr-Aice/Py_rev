from typing import Final
from random import randint


Character = dict[str, str | int]

#Heros
Black : Final[Character] = { 
    'name' : "Black Widow",
    "ATTACK_POWER" : 1000,
    "life" : 1000
}

Spider : Final[Character] = {
    'name' : "Spider Man",
    "ATTACK_POWER" : 1500,
    "life" : 1500
}

Captain : Final[Character] = {
    'name' : "Captain America",
    "ATTACK_POWER" : 2000,
    "life" : 2000
}

Iron : Final[Character] = {
    'name' : "Iron Man",
    "ATTACK_POWER" : 250,
    "life" : 250
}

Thor : Final[Character] = {
    'name' : "Thor",
    "ATTACK_POWER" : 300,
    "life" : 300
}

Super : Final[Character] = {
    'name' : "Super Man",
    "ATTACK_POWER" : 350,
    "life" : 350
}

#Villians

Thanos : Final[Character] = { 
    'name' : "Thanos",
    "ATTACK_POWER" : 1500,
    "life" : 1000
}

REDSKULL : Final[Character] = {
    'name' : "REDSKULL",
    "ATTACK_POWER" : 300,
    "life" : 800
}

PROXIMA : Final[Character] = {
    'name' : "PROXIMA",
    "ATTACK_POWER" : 320,
    "life" : 600
}


#Heros list

Super_Heros: list[Character] = [Black, Spider, Captain, Iron, Thor, Super]

#Villians

Villians : list[Character] = [ Thanos, REDSKULL, PROXIMA]


WIN_MSG: Final[str] = "\n\nCongrats! You defeated Thanos!\n\n"
LOSS_MSG: Final[str] = "\n\nYour Maximum chances gone and Thanos Still standing!\n\n"


#constraints
MAX_ATTACK = 3

hero_life = 0
villian_life = 0


for attack in range(MAX_ATTACK):
    hero_index = randint(0, (len(Super_Heros)-1))
    villian_index = randint(0, (len(Villians)-1))

    #current hero & villian
    current_hero = Super_Heros[hero_index]
    current_villian = Villians[villian_index]
    #lives
    hero_life += current_hero['life']
    villian_life += current_villian['life']
    
    print(f"Attack {attack + 1} => {current_hero['name']} is going to fight with {current_villian['name']}.")
    
    #attack
    hero_life -= current_villian['ATTACK_POWER']
    villian_life -= current_hero['ATTACK_POWER']


print('=' * 70)

if hero_life > villian_life:
    print(WIN_MSG)
elif hero_life == villian_life:
    print("Stalemate")
else:
    print(LOSS_MSG)