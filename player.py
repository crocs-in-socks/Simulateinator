from typing import TypedDict


class playerStats(TypedDict):
    name: str
    bowling: float
    batting: float
    fielding: float
    running: float
    experience: float


class Player:

    def __init__(self, stats: playerStats) -> None:
        self.stats = {
            'name': stats['name'],
            'bowling': stats['bowling'],
            'batting': stats['batting'],
            'fielding': stats['fielding'],
            'running': stats['running'],
            'experience': stats['experience']
        }

    def does_action(self, action: str) -> float:
        '''
            Calculates the score of a player's play instance based on the given
            action.
        '''
        # TODO : Choose a function to calculate score
        score = self.stats[action]
        return score
