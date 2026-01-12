from .schema import Player, GameState, LIFE, SuperHero, SuperVillian
from .models import SuperHeroModel, SuperVillianModel
from .constants import NUM_ATTACK, WINMSG, STALEMATE, LOSTMSG
from random import randint

class Game:
    def __init__(self, player: Player):
        self.player = player
        self.state = GameState.INITIALIZING
        self.superheros = SuperHeroModel()
        self.supervillians = SuperVillianModel()

    def __repr__(self) -> str:
        return f"<class 'Game'>"
    
    def __str__(self) -> str:
        return f"Name: {self.player.fname} {self.player.lname}\nGame: {self.state}\nSuper Heros: {self.superheros}\nVillians: {self.supervillians}"
    

    
    def __do_attack(self, hero: SuperHero, villian: SuperVillian):
        self.state = GameState.PROGRESS
        print(f"{self.state}")
        print(f"{hero.name} is fighting {villian.name}.....")
        LIFE.increment_hero_life(hero.life)
        LIFE.increment_villian_life(villian.life)
        LIFE.decrement_hero_life(villian.attack_power)
        LIFE.decrement_villian_life(hero.attack_power)



    def check_results(self) -> None:
            
            print("\n\n")
            if LIFE.hero_life > LIFE.Villian_life:
                print(WINMSG)
                self.state = GameState.WIN
                print(f"{self.state}")
            elif LIFE.hero_life == LIFE.Villian_life:
                print(STALEMATE)
                self.state = GameState.STALEMATE
                print(f"{self.state}")
            else:
                print(LOSTMSG)
                self.state = GameState.LOST
                print(f"{self.state}")

    def attack(self) -> None:

        for attack in range(NUM_ATTACK):
            hero_index = randint(0, len(self.superheros.all) - 1)
            villian_index = randint(0,len(self.supervillians.all) - 1)

            current_superHero = self.superheros.get_SuperHero(hero_index)
            current_superVillian = self.supervillians.get_SuperVillian(villian_index)

            if current_superHero and current_superVillian:
                self.__do_attack(current_superHero, current_superVillian)
            else:
                print("Error Detected!!! No superHero or villians to fight.")

        self.check_results()