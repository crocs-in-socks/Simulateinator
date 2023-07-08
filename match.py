import random
from team import Team
from player import Player
from typing import List


class Match:

    def __init__(self, teams: List[Team], overs: int) -> None:
        self.team_A = teams[0]
        self.team_B = teams[1]
        self.overs = overs

    def toss(self) -> None:
        '''
            Toss. Team that wins chooses to bat/bowl.
        '''
        toss = random.randint(0, 1)

        if toss:

            choice = self.team_A.won_toss()

            if choice == 'batting':
                self.team_A.is_batting = True
                self.team_B.is_bowling = True

            elif choice == 'bowling':
                self.team_A.is_bowling = True
                self.team_B.is_batting = True

        else:

            if choice == 'batting':
                self.team_B.is_batting = True
                self.team_A.is_bowling = True

            elif choice == 'bowling':
                self.team_B.is_bowling = True
                self.team_A.is_batting = True

    def over(self) -> None:
        '''
            Play an over in the innings.
        '''

    def innings(self) -> None:
        '''
            Play innings.
        '''
        for over in range(self.overs):
            self.over

    def play(self) -> None:
        '''
            Start the match.
        '''
        self.toss()
        self.innings()

        self.team_A.is_batting = not self.team_A.is_batting
        self.team_A.is_bowling = not self.team_A.is_bowling
        self.team_B.is_batting = not self.team_B.is_batting
        self.team_B.is_bowling = not self.team_B.is_bowling

        self.innings()


if __name__ == '__main__':

    player1 = Player({
        'name': 'Dhruv Bajaj',
        'bowling': 0.69,
        'batting': 0.42,
        'fielding': 0.88,
        'running': 0.5,
        'experience': 0.9
    })

    player2 = Player({
        'name': 'Sanjit Mittapalli',
        'bowling': 0.42,
        'batting': 0.69,
        'fielding': 0.88,
        'running': 0.5,
        'experience': 0.8
    })

    player3 = Player({
        'name': 'Good Music',
        'bowling': 0.7,
        'batting': 0.43,
        'fielding': 0.89,
        'running': 0.51,
        'experience': 0.91
    })

    player4 = Player({
        'name': 'Common Sense',
        'bowling': 0.43,
        'batting': 0.70,
        'fielding': 0.89,
        'running': 0.51,
        'experience': 0.81
    })

    teamA = Team([player1, player2])
    teamB = Team([player3, player4])
    match = Match([teamA, teamB], 1)
