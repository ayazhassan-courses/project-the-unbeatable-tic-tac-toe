ai = 'X'
human = 'O'
currentPlayer = human
board = [ [ '' for i in range(0,3)] for i in range(0,3)]
print(board)
print()


def checkWinner():
    winner = 'null'
    # horizontal 
    for i in range(0,3):
        if (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]) : 
            if board[i][0] != '' and board[i][1] != '' and board[i][1] != '':
                winner = board[i][0]

    # verticle 
    for i in range(0,3):
        if (board[0][i] == board[1][i]) and (board[1][i] == board[2][i]): 
            if board[0][i] != '' and board[1][i] != '' and board[2][i] != '':
                winner = board[0][i]

    # Diagonal 
    if (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]): 
        if board[0][0] != '' and board[1][1] != '' and board[2][2] != '':
            winner = board[0][0]
    if (board[2][0] == board[1][1]) and (board[1][1] == board[0][2]): 
        if board[2][0] != '' and board[1][1] != '' and board[0][2] != '':
            winner = board[2][0]

    openspots = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == '':
                openspots += 1
    
    if winner == 'null' and openspots == 0:
        return 'tie'
    else: 
        return winner 


def best_move(currentPlayer):
    bestScore = -9999999999
    move = ()
    for i in range(0,3):
        for j in range(0,3):
            # is the spot available? 
            if board[i][j] == '': 
                board[i][j] = ai 
                score = minimax(board, 0, False)
                board[i][j] = ''  
                if score > bestScore: 
                    bestScore = score 
                    move = (i,j)

    board[move[0]][move[1]] = ai 
    currentPlayer = human 
    print('AI turns')
    print()
    print(str(board[0])+'\n'+str(board[1])+'\n'+str(board[2])+'\n')
    print()
    
    return checkWinner(), currentPlayer

scores = {
    'X':10,
    'O':-10,
    'tie':0
}

def minimax(board,depth,isMaximizing):
    result = checkWinner()
    if result != 'null':
        return scores[result]
    if isMaximizing: 
        bestScore = - 999999999
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j]=='':
                    board[i][j] = ai
                    score = minimax(board, depth+1, False)
                    board[i][j] = ''
                    bestScore = max(int(score), int(bestScore))
        return bestScore
    
    else: 
        bestScore = 999999999
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j]=='':
                    board[i][j] = human
                    score = minimax(board, depth+1, True)
                    board[i][j] = ''
                    bestScore = min(int(score), int(bestScore))

        return bestScore

def playersTurn(currentPlayer):
    
    if currentPlayer == human:
        dumdum = int(input('Its your turn  '))
        if dumdum == 1: board[0][0] = human
        elif dumdum == 2: board[0][1] = human
        elif dumdum == 3: board[0][2] = human
        elif dumdum == 4: board[1][0] = human
        elif dumdum == 5: board[1][1] = human
        elif dumdum == 6: board[1][2] = human
        elif dumdum == 7: board[2][0] = human
        elif dumdum == 8: board[2][1] = human
        elif dumdum == 9: board[2][2] = human

        print('Human turns')
        print()
        print(str(board[0])+'\n'+str(board[1])+'\n'+str(board[2])+'\n')
        print()
        

        currentPlayer = ai
        x,currentPlayer = best_move(currentPlayer)
    
        if x == 'null':
            playersTurn(currentPlayer)

        if x == 'X' or x == 'O': 
            print(x,'WINS!')
        elif x ==  'tie': print("its a "+x)
        return 


        


playersTurn(currentPlayer)


