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
