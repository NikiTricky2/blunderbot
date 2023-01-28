import chess
import chess.engine
import chess.pgn
from tqdm import tqdm

engine = chess.engine.SimpleEngine.popen_uci('/home/niki/Documents/Code/Python/blunderbot/stockfish-ubuntu-20.04-x86-64')

# THIS GOVERNS HOW LONG A MOVE CALCULATION TAKES
TIME = 10 # Time in seconds a move calculation should take
TIME_PER_MOVE = None # Time per individual move calculation
DEPTH = None # Depth at witch the engine should search at

RENDER_BOARD = "board.svg" # Render a board after every move. Good for troubleshooting. Set to None or the path to the board to be rendered.

def get_worst_move(board, engine, t=10, tm=None, d=None):
    moves = []
    mate = [] # Store mate moves
    legal_moves = list(board.legal_moves)
    if t:
        limit = chess.engine.Limit(time=t/len(legal_moves))
    elif tm:
        limit = chess.engine.Limit(time=tm)
    else:
        limit = chess.engine.Limit(depth=d)
    for el in tqdm(legal_moves):

        analisys = engine.analyse(board, limit)
        score = analisys.get("score")

        score_pov = score.pov(board.turn)
        if score_pov.score():
            move_score = score_pov.score()
            moves.append([el, move_score, analisys.get("depth"), 0])
        elif score_pov.mate():
            move_score = abs(int(score_pov.mate()))
            mate.append([el, move_score, analisys.get("depth"), 1])
        else:
            moves.append([el, 1e6, analisys.get("depth"), 0])

    if mate:
        mate = sorted(mate, key=lambda x: x[1])
        return mate[-1]
    moves = sorted(moves, key=lambda x: x[1])
    return moves[0]

board = chess.Board()

player_color_inp = None
while not player_color_inp in ["b", "w"]:
    player_color_inp = input("Input player (b/w): ")
    match player_color_inp:
        case "b":
            player_color = 0
        case "w":
            player_color = 1

to_move = 1

while not (board.is_checkmate() or board.is_stalemate()):
    if player_color == to_move:
        worst_move = get_worst_move(board, engine, t=TIME, tm=TIME_PER_MOVE, d=DEPTH)
        if worst_move[3]: # Check if a move is mate
            print(f"Move: {board.lan(worst_move[0])} (Mate in {worst_move[1]}, Depth: {worst_move[2]})")
        else:
            print(f"Move: {board.lan(worst_move[0])} (Score: {worst_move[1]}, Depth: {worst_move[2]})")

    if to_move:
        move = input("White move: ")
    else:
        move = input("Black move: ")

    if move == "undo":
        board.pop()
        to_move = int(not to_move)
        continue

    try:
        move = chess.Move.from_uci(move)
        if not (move in list(board.generate_legal_moves())):
            raise NotImplementedError("Not a valid move")
        board.push(move)
    except NotImplementedError:
        print("Invalid move. FEN code:", board.fen())
        continue
    except Exception as e:
        # raise e
        print("Invalid move (error code). FEN code:", board.fen())
        continue

    if RENDER_BOARD:
        with open(RENDER_BOARD, "w") as f:
            f.write(chess.svg.board(board, fill=dict.fromkeys([move.from_square, move.to_square], "#30ed26aa")))

    to_move = int(not to_move)

print("Game ended!")

engine.close()
