from Game.schema import SuperHero
class SuperHeroModel:
    def __init__(self) -> None:
        self.all: list[SuperHero] = self.get_all_SuperHeros()
    
    def __repr__(self) -> str:
        return f"class <SuperHeroModel>"
    
    def __str__(self) -> str:
        name: list = []
        for n in self.all:
            name.append(n.name)
        return f"Name: {name}"
    
    def get_all_SuperHeros(self) -> list[SuperHero]:
        ironman = SuperHero(name="Iron Man",attack_power=250,life=1000)
        BlackWidow = SuperHero(name="Black Widow",attack_power=180,life=800)
        Spiderman = SuperHero(name="SPIDER MAN",attack_power=190,life=700)
        Hulk = SuperHero(name="HULK",attack_power=300,life=1100)
        superheros: list[SuperHero] = [ironman, BlackWidow,Spiderman, Hulk]
        return superheros

    def get_SuperHero(self, index: int) -> SuperHero | None:
        if index < len(self.all):
            return self.all[index]
        else:
            return None
        
