from .character import Character
from .character_type import CharacterType
class SuperHero(Character):
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.HERO

    def __repr__(self) -> str:
        return f"class <SuperHero>"
    
    def __str__(self) -> str:
        return f"Name: {self.name} Attack Power: {self.attack_power} Life: {self.life} Role: {self.role}"
    