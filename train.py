import os
import chess.pgn

for fn in os.listdir("data"):
    pgn = open(os.path.join("data", fn))
    # game = None
    while 1:
        try:
            game = chess.pgn.read_game(pgn)
        except Exception as e:
            print(e)

        board = game.board()
        for move in game.mainline_moves():
            board.push(move)
            print(board)
        exit(0)