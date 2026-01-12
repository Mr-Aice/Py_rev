class Character:
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        self.name = name
        self.attack_power = attack_power
        self.life = life

    def __repr__(self) -> str:
        return f"class <Character>"
    
    def __str__(self) -> str:
        return f"Name: {self.name} Attack Power: {self.attack_power} Life: {self.life}"
