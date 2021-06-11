import chess
import math


def main():
    playing = 1
    board = chess.Board()
    print(board)
    print('Who play first?')
    print('0 - Human')
    print('1- AI')
    choice = int(input('Chose: '))

    while playing:
        # Check if is finisihed
        if choice:
            bestmove(board, 1)
            # Human play
        else:
            # Human play
            bestmove(board, 0)


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
