#!/usr/bin/env python2

from unittest import main, TestCase

lines = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)


def minimax(board, player, depth=0):
    # Hack to avoid computing the best move on the start because it's slow.
    if not any(board):
        # The corners and the center.
        return 0, [0, 2, 4, 6, 8]

    # Check for the end of the game.
    if won(board):
        return -player, None
    if all(board):
        return 0, None  # Draw.

    moves = []
    scores = []

    for i, x in enumerate(board):
        if x != 0:
            continue
        board[i] = player
        score, _ = minimax(board, -player, depth=depth+1)
        # Hack to favour the winning move.
        if depth == 0 and won(board):
            score *= 2
        scores.append(score)
        moves.append(i)
        board[i] = 0

    opt = max if player == 1 else min
    best_score = opt(scores)

    # Return all of the moves that have the best score.
    return best_score, [
        moves[i]
        for i, x in enumerate(scores)
        if x == best_score
    ]


def won(b):
    return any(
        b[l[0]] == b[l[1]] == b[l[2]] and b[l[0]]
        for l in lines
    )


class Tests(TestCase):

    def test_0(self):
        self.assertTrue(won([
            -1, -1, -1,
            0, 0, 0,
            0, 0, 0,
        ]))

    def test_1(self):
        self.assertTrue(won([
            -1, 1, 1,
            0, -1, 0,
            0, 0, -1,
        ]))

    def test_2(self):
        self.assertTrue(won([
            -1, 1, 1,
            0, 1, 0,
            1, 0, 0,
        ]))

    def test_3(self):
        self.assertTrue(won([
            -1, 0, 1,
            0, 0, 0,
            1, 1, 1,
        ]))

    def test_4(self):
        self.assertFalse(won([
            -1, 0, -1,
            0, 1, 0,
            1, 0, 1,
        ]))

    def test_m0(self):
        self.assertEqual(minimax([
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
        ], 1), (0, [0, 2, 4, 6, 8]))

    def test_m1(self):
        self.assertEqual(minimax([
            1, 1, 0,
            -1, -1, 0,
            1, -1, 0,
        ], -1), (-2, [5]))

    def test_m2(self):
        self.assertEqual(minimax([
            1, 0, 0,
            0, 1, 0,
            0, 0, 0,
        ], 1), (2, [8]))

    def test_m3(self):
        self.assertEqual(minimax([
            1, 1, 0,
            -1, -1, 0,
            0, 0, 0,
        ], -1), (-2, [5]))

    def test_m4(self):
        self.assertEqual(minimax([
            1, 1, 0,
            0, 0, 0,
            0, 0, 0,
        ], -1), (1, [2, 3, 4, 5, 6, 7, 8]))


if __name__ == '__main__':
    main()
