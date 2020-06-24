from tkinter import *
from tkinter import messagebox
import random as r

###############   Main Program #################
root=Tk()                   #Window defined
root.title("Tic-Tac-Toe")   #Title given
# a=r.choice(['O','X'])       #Two operators defined
human = 'O'
currentPlayer = human
ai = 'X'
colour={'O':"deep sky blue",'X':"lawn green"}
board = [ [ '' for i in range(0,3)] for i in range(0,3)]
b=[[],[],[]]

########################################################################################################33

def checkWinner():

    winner = 'null'

    # horizontal 

    for i in range(0,3):

        if (board[i][0] == board[i][1]) and (board[i][1] == board[i][2]) : 

            if board[i][0] != '' and board[i][1] != '' and board[i][2] != '':

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
    b[move[0]][move[1]].config(text=ai,state=DISABLED,disabledforeground=colour[ai])

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

##########################################################################################################


def button(frame):          #Function to define a button
    b=Button(frame,padx=1,bg="papaya whip",width=3,text="",font=('arial',60,'bold'),relief="sunken",bd=10)
    return b

def reset():                #Resets the game
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=""
                board[i][j] = ""
                b[i][j]["state"]=NORMAL
    

def click(row,col):
        b[row][col].config(text=human,state=DISABLED,disabledforeground=colour[human])
        board[row][col] = human
       
        x=checkWinner()
        if x == 'X' or x == 'O': 
            messagebox.showinfo("Congrats!!","'"+x+"' has won")
            print(x,'WINS!')
            reset()

        elif x ==  'tie': 
            messagebox.showinfo("Tied!!","The match ended in a draw")
            print("its a "+x)
            reset()
            return
        
        currentPlayer = ai
        # label.config(text="computer's Chance")
        whoseTurn.set("Computer's Turn")
        x,currentPlayer = best_move(currentPlayer)
        whoseTurn.set('Humans Turn')
        if x == 'X' or x == 'O': 
            messagebox.showinfo("Congrats!!","'"+x+"' has won")
            print(x,'WINS!')
            reset()

        elif x ==  'tie': 
            messagebox.showinfo("Tied!!","The match ended in a draw")
            print("its a "+x)
            reset()
            return
###############   Main Program #################
whoseTurn = StringVar()
whoseTurn.set("Human's Turn")

for i in range(3):
        for j in range(3):
                b[i].append(button(root)) 
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                # if yo: print('heha')
                b[i][j].grid(row=i,column=j)

print('here')
# if currentPlayer == human:                
label=Label(textvariable=whoseTurn,font=('arial',20,'bold'))
# elif currentPlayer == ai:

label.grid(row=3,column=0,columnspan=3)
root.mainloop()
