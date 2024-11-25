def boardprinter(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def winchecker(board, player):
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def isfull(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

board = []
for _ in range(3):
    row = [" "] * 3
    board.append(row)

player = "X"

while True:
    boardprinter(board)
    try:
        move = input(f"Player {player}, enter your move (row and column separated by space): ")
        move = move.split()
        if len(move) != 2:
            raise ValueError("Input should be exactly two numbers separated by space.")
        
        row = int(move[0])
        col = int(move[1])
        
        if not (0 <= row < 3 and 0 <= col < 3):
            raise ValueError("Row and column values should be between 0 and 2.")

        if board[row][col] != " ":
            raise ValueError("This cell is already occupied. Try again.")
        
        board[row][col] = player

        if winchecker(board, player):
            boardprinter(board)
            print(f"Player {player} wins!")
            break
        if isfull(board):
            boardprinter(board)
            print("The game is a draw!")
            break
        
        if player == "X":
            player = "O"
        else:
            player = "X"
    
    except ValueError:
        print("Invalid input: Input should be two valid numbers separated by space, or the cell is already occupied.")
    except IndexError:
        print("Invalid input: Row and column values should be between 0 and 2.")
