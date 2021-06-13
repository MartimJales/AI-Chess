import chess
import math
from os import system
from time import sleep
from random import randint


def main():
    playing = 1
    board = chess.Board()
    print(board)
    print('Who play first?')
    print('0 - Human')
    print('1- AI')
    choice = int(input('Chose: '))

    while playing:
        system('clear')
        print(board)
        # Check if is finisihed - Both function are making that but I could compress in just one maybe
        if choice:
            bestmove(board, chess.WHITE)
            human_play(board)
        else:
            human_play(board)
            bestmove(board, chess.BLACK)


def human_play(board):
    while True:
        human_move = input('Human move: ')
        move = chess.Move.from_uci(human_move)
        if board.is_legal(move):
            board.push(move)
            break
        else:
            # Need to make a function to verify uci validattion
            print('Invalid move!')
            sleep(2)


def bestmove(board, white):
    # Normally eval in white is positive but i need to check that
    bestMove = ""
    if white:
        bestScore = -math.inf
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, 3, -math.inf, math.inf, True)
            board.pop()
            if score > bestScore:
                bestScore = score
                bestMove = move
    else:
        bestScore = math.inf
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, 3, -math.inf, math.inf, False)
            board.pop()
            if score < bestScore:
                bestScore = score
                bestMove = move
    board.push(bestMove)


def minimax(board, depth, alpha, beta, white):
    if depth == 0 or board.is_game_over:
        return randint(-10, 10)  # Need to make the right evaluation function

    if white:
        bestScore = -math.inf
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth-1, alpha, beta, True)
            board.pop()
            bestScore = max(score, bestScore)
            alpha = max(score, alpha)
            if beta <= alpha:
                break
        return bestScore
    else:
        bestScore = math.inf
        for move in board.legal_moves:
            board.push(move)
            score = minimax(board, depth-1, alpha, beta, False)
            board.pop()
            bestScore = min(score, bestScore)
            beta = min(score, beta)
            if beta <= alpha:
                break
        return bestScore


if __name__ == '__main__':
    main()
