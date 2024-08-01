# Set up the game board as a list
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# Define a function to print the game board
def print_board():
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])

# Define a function to find the best move for the AI
def findBestMove():
    bestScore = float('-inf')
    bestMove = -1

    # Loop through all positions on the board
    for pos in range(9):
        # If the position is empty
        if board[pos] == "-":
            # Place the AI's marker and calculate the score using minimax
            board[pos] = "O"
            score = minimax(board, 0, False)
            # Undo the move
            board[pos] = "-"
            # If the current score is better than the best score, update best score and best move
            if score > bestScore:
                bestScore = score
                bestMove = pos

    # Make the best move
    board[bestMove] = "O"

# Define the minimax function to calculate the best move
def minimax(board, depth, isMax):
    # Evaluate the board
    score = evaluate(board)
    # If the AI wins, return the score
    if score == 10:
        return score - depth
    # If the player wins, return the score
    if score == -10:
        return score + depth
    # If the board is full, return 0 (tie)
    if "-" not in board:
        return 0
    
    # If it is the maximizer's turn (AI)
    if isMax:
        bestScore = float('-inf')

        # Loop through all positions on the board
        for pos in range(9):
            if board[pos] == "-":
                # Place the AI's marker and calculate the score using minimax
                board[pos] = "O"
                score = minimax(board, depth + 1, False)
                # Undo the move
                board[pos] = "-"
                # Update the best score
                if score > bestScore:
                    bestScore = score
    # If it is the minimizer's turn (player)
    else:
        bestScore = float('inf')

        # Loop through all positions on the board
        for pos in range(9):
            if board[pos] == "-":
                # Place the player's marker and calculate the score using minimax
                board[pos] = "X"
                score = minimax(board, depth + 1, True)
                # Undo the move
                board[pos] = "-"
                # Update the best score
                if score < bestScore:
                    bestScore = score

    return bestScore

# Define a function to evaluate the board and return a score
def evaluate(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    # Check if any win condition is met
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]]:
            if board[condition[0]] == "O":
                return 10
            elif board[condition[0]] == "X":
                return -10

    return 0

# Define a function to handle the player's move
def playerMove():
    position = input("Choose a position from 1-9: ")
    # Validate the input and ensure the chosen position is empty
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or board[int(position) - 1] != "-":
        if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")
        else:
            position = input("Position already taken. Choose a different position: ")
    # Place the player's marker
    board[int(position) - 1] = "X"

# Define a function to handle a player's turn
def take_turn(player):
    print(f"{player}'s turn.")
    if player == "X":
        playerMove()
    else:
        findBestMove()
    print_board()

# Define a function to check if the game is over
def check_game_over():
    # Check for a win
    if (board[0] == board[1] == board[2] != "-") or \
       (board[3] == board[4] == board[5] != "-") or \
       (board[6] == board[7] == board[8] != "-") or \
       (board[0] == board[3] == board[6] != "-") or \
       (board[1] == board[4] == board[7] != "-") or \
       (board[2] == board[5] == board[8] != "-") or \
       (board[0] == board[4] == board[8] != "-") or \
       (board[2] == board[4] == board[6] != "-"):
        return "win"
    # Check for a tie
    elif "-" not in board:
        return "tie"
    # Game is not over
    else:
        return "play"

# Define the main game loop
def play_game():
    print_board()
    current_player = "X"
    game_over = False
    # Continue the game until it is over
    while not game_over:
        take_turn(current_player)
        game_result = check_game_over()
        if game_result == "win":
            print(f"{current_player} wins!")
            game_over = True
        elif game_result == "tie":
            print("It's a tie!")
            game_over = True
        else:
            # Switch to the other player
            current_player = "O" if current_player == "X" else "X"

# Start the game
play_game()
