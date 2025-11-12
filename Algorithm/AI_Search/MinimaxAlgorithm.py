def minimax (board, is_max):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == '0': return -1
    if ' ' not in board: return 0

    scores = []
    for i in range(9):
        if board[i]== ' ':
            board[i]= 'X' if is_max else '0'
            score= minimax(board, not is_max)
            board[i]= ' '
            scores.append(score)

    return max(scores) if is_max else min(scores)

def check_winner(b):
    win= [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for i,j,k in win:
        if b[i]== b[j] == b[k]  !=' ': return b[i]
    return None

def best_move(board):
    best,move= -2,-1
    for i in range(9):
        if board[i]== ' ':
            board[i]= 'X'
            score = minimax(board,False)
            board[i]=' '
            if score> best:
                best,move = score,i
    return move

board = [' '] * 9
print("Best move:",best_move(board))