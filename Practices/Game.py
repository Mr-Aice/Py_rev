from enum import Enum, auto
from random import randint
from typing import final

class CharacterType(Enum):
    HERO = auto()
    VILLIAN = auto()


class Character:
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        self.name = name
        self.attack_power = attack_power
        self.life = life

    def __repr__(self) -> str:
        return f"class <Character>"
    
    def __str__(self) -> str:
        return f"Name: {self.name} Attack Power: {self.attack_power} Life: {self.life}"

@final
class SuperHero(Character):
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.HERO

    def __repr__(self) -> str:
        return f"class <SuperHero>"
    
    def __str__(self) -> str:
        return f"Name: {self.name} Attack Power: {self.attack_power} Life: {self.life} Role: {self.role}"
    
@final
class SuperVillian(Character):
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.VILLIAN
        
    def __repr__(self) -> str:
        return f"class <SuperVillian>"
    
    def __str__(self) -> str:
        return f"Name: {self.name} Attack Power: {self.attack_power} Life: {self.life} Role: {self.role}"
    
class LIFE:
    hero_life: int = 0
    Villian_life: int = 0

    @staticmethod
    def increment_hero_life(life: int):
        LIFE.hero_life += life
    
    @staticmethod
    def increment_villian_life(life: int):
        LIFE.Villian_life += life

    @staticmethod
    def decrement_hero_life(life: int):
        LIFE.hero_life -= life
    
    @staticmethod
    def decrement_villian_life(life: int):
        LIFE.Villian_life -= life


def get_all_SuperHeros() -> list[SuperHero]:
    ironman = SuperHero(name="Iron Man",attack_power=250,life=1000)
    BlackWidow = SuperHero(name="Black Widow",attack_power=180,life=800)
    Spiderman = SuperHero(name="SPIDER MAN",attack_power=190,life=700)
    Hulk = SuperHero(name="HULK",attack_power=300,life=1100)
    superheros: list[SuperHero] = [ironman, BlackWidow,Spiderman, Hulk]
    return superheros

def get_SuperHero(index: int) -> SuperHero | None:
    superheros = get_all_SuperHeros()
    if index < len(superheros):
        return superheros[index]
    else:
        return None

    
def get_all_SuperVillians() -> list[SuperVillian]:
    thanos = SuperVillian(name="Thanos",attack_power= 400, life=1500)
    redskull = SuperVillian(name="RedSkull",attack_power= 300, life=800)
    proxima = SuperVillian(name="Proxima",attack_power= 320, life=800)
    supervillians: list[SuperVillian] = [thanos, redskull, proxima]
    return supervillians

def get_SuperVillian(index: int) -> SuperVillian | None:
    supervillians = get_all_SuperVillians()
    if index < len(supervillians):
        return supervillians[index]
    else:
        return None

def stimulate_attack(hero: SuperHero, villian: SuperVillian):
    print(f"{hero.name} is fighting {villian.name}.....")
    LIFE.increment_hero_life(hero.life)
    LIFE.increment_villian_life(villian.life)
    LIFE.decrement_hero_life(villian.attack_power)
    LIFE.decrement_villian_life(hero.attack_power)



def check_results() -> None:
        WINMSG: str = "Congrats!!! Heros Defeated villians...."
        STALEMATE: str = "Fight results in Draw...."
        LOSTMSG: str = "Villians Defeated Heros!!!!!"
        print("\n\n")
        if LIFE.hero_life > LIFE.Villian_life:
            print(WINMSG)
        elif LIFE.hero_life == LIFE.Villian_life:
            print(STALEMATE)
        else:
            print(LOSTMSG)

def attack() -> None:

    for attack in range(3):
        hero_index = randint(0,3)
        villian_index = randint(0,2)

        current_superHero = get_SuperHero(hero_index)
        current_superVillian = get_SuperVillian(villian_index)

        if current_superHero and current_superVillian:
            stimulate_attack(current_superHero, current_superVillian)
        else:
            print("Error Detected!!! No superHero or villians to fight.")

    check_results()
    
def main():
    attack()


main()