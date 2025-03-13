# Tamaño del tablero
BOARD_SIZE = 10

# Crear tablero vacío
def create_board():
    return [["."] * BOARD_SIZE for _ in range(BOARD_SIZE)]

def print_board(board):
    print("\n  " + " ".join(str(i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        print(str(i) + " " + " ".join(row))

board = create_board() 
print(print_board(board))