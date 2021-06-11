import chess
import math
from os import system
from time import sleep


def main():
    playing = 1
    board = chess.Board()
    print(board)
    print('Who play first?')
    print('0 - Human')
    print('1- AI')
    choice = int(input('Chose: '))

    while playing:
        print(board)
        # Check if is finisihed
        if choice:
            # bestmove(board, chess.WHITE)
            human_play(board)
        else:
            human_play(board)
            # bestmove(board, chess.BLACK)
        system('clear')


def human_play(board):
    human_move = input('Human move: ')
    move = chess.Move.from_uci(human_move)
    if board.is_legal(move):
        board.push(move)
    else:
        print('Invalid move!')
        sleep(2)


def bestmove(board, white):
    bestScore = -math.inf
    for move in board.legal_moves:
        board.push(move)
        score = minimax(board, 3, -math.inf, math.inf, True)
        bestScore = max(bestScore, score)
        board.pop()


def minimax(board, depth, alpha, beta, white):
    if 1:  # end
        pass

    if white:
        pass
    else:
        pass


if __name__ == '__main__':
    main()
