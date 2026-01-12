from Game.schema import SuperVillian
class SuperVillianModel:
    def __init__(self) -> None:
        self.all: list[SuperVillian] = self.get_all_SuperVillians()
    
    def __repr__(self) -> str:
        return f"class <SuperVillianModel>"
    
    def __str__(self) -> str:
        name: list = []
        for n in self.all:
            name.append(n.name)
        return f"Name: {name}"
    
    def get_all_SuperVillians(self) -> list[SuperVillian]:
        thanos = SuperVillian(name="Thanos",attack_power= 400, life=1500)
        redskull = SuperVillian(name="RedSkull",attack_power= 300, life=800)
        proxima = SuperVillian(name="Proxima",attack_power= 320, life=800)
        supervillians: list[SuperVillian] = [thanos, redskull, proxima]
        return supervillians

    def get_SuperVillian(self, index: int) -> SuperVillian | None:
        supervillians = self.get_all_SuperVillians()
        if index < len(self.all):
            return self.all[index]
        else:
            return None