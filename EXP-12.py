# Function to create board
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Function to display board
def display_board(board):
    print("\nCurrent Board:")
    for i in range(3):
        print(" " + board[i][0] + " | " + board[i][1] + " | " + board[i][2])
        if i < 2:
            print("---+---+---")
    print()

# Function to check winner
def check_winner(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Main game function
def play_game():
    board = create_board()
    current_player = 'X'
    moves = 0

    while moves < 9:
        display_board(board)
        print(f"Player {current_player}'s turn")

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

            if row not in range(3) or col not in range(3):
                print("Invalid position! Try again.")
                continue

            if board[row][col] != ' ':
                print("Cell already occupied! Try again.")
                continue

            board[row][col] = current_player
            moves += 1

            if check_winner(board, current_player):
                display_board(board)
                print(f"Player {current_player} Wins!")
                return

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'

        except ValueError:
            print("Please enter valid numbers!")

    display_board(board)
    print("It's a Draw!")

# Start game
play_game()
