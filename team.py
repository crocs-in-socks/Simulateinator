import random
from player import Player
from typing import List


class Team:

    def __init__(self, players: List[Player]) -> None:

        self.players = players
        self.captain = self.select_captain(players)
        self.batting_order = self.select_order(players, 'batting')
        self.bowling_order = self.select_order(players, 'bowling')
        self.is_batting = False
        self.is_bowling = False

    def select_captain(self, players: Player) -> Player:
        '''
            Selects the player with most experience as captain of the team.
        '''
        return max(players, key=lambda x: x.stats['experience'])

    def select_order(self, players: List[Player], action: str) -> List[Player]:
        '''
            Selects the order of players based on best stat first.
        '''
        return sorted(players, key=lambda x: x.stats[action], reverse=True)

    def won_toss(self) -> str:
        '''
            Randomly selects batting or bowling
        '''
        return random.choice(['batting', 'bowling'])
