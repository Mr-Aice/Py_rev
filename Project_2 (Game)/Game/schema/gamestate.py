from enum import Enum, auto

class GameState(Enum):
    INITIALIZING = auto()
    PROGRESS = auto()
    WIN = auto()
    STALEMATE = auto()
    LOST = auto()