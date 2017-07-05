from random import choice

from brain import minimax
from noughtsandcrosses import NoughtsAndCrossesClient


class PauBot(NoughtsAndCrossesClient):

    def play_turn(self, state):
        board = [{'X': 1, 'O': -1, '': 0}[x] for x in sum(state['board'], [])]
        mark = 1 if state['marks']['X'] == self.bot_id else -1
        _, moves = minimax(board, mark)
        move = choice(moves)
        return {'space': [move / 3, move % 3], 'mark': {1: 'X', -1: 'O'}[mark]}


if __name__ == '__main__':
    PauBot()
