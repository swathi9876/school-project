import time
ques=input('Lets play(yes/no)?')
if ques=='no':
    time.sleep(1)
    print('OK,Program over...PS-I know you are scared')
    time.sleep(11)
elif ques=='yes':
    while ques!='no':
        x=input('2 player(a) or do you want to go against the computer(b)?')
        if x=='a':
            a=input('Are you ready(y/n)?')
            if a=='n':
                k=input('Are you scared(y/n)?')
                if k=='n':
                    a=input('choose again wisely...do you wanna play?(yes/no)?')
                elif k=='y':
                    print('I knew it')
                else:
                    print('Are you so scared that you cannot even type properly.Shut Up and Play')
            import os    
            import time    
            
            board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
            player = 1    
               
            ########win Flags##########    
            Win = 1    
            Draw = -1    
            Running = 0    
            Stop = 1    
            choice = 0
            ###########################    
            Game = Running    
            Mark = 'X'    
               
            #This Function Draws Game Board    
            def DrawBoard():    
                print(" %c | %c | %c " % (board[1],board[2],board[3]))    
                print("___|___|___")    
                print(" %c | %c | %c " % (board[4],board[5],board[6]))    
                print("___|___|___")    
                print(" %c | %c | %c " % (board[7],board[8],board[9]))    
                print("   |   |   ")    
               
            #This Function Checks position is empty or not    
            def CheckPosition(x):    
                if(board[x] == ' '):    
                    return True    
                else:    
                    return False    
               
            #This Function Checks player has won or not    
            def CheckWin():    
                global Game    
                #Horizontal winning condition    
                if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
                    Game = Win    
                elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
                    Game = Win    
                elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
                    Game = Win    
                #Vertical Winning Condition    
                elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
                    Game = Win    
                elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
                    Game = Win    
                elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
                    Game=Win    
                #Diagonal Winning Condition    
                elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
                    Game = Win    
                elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
                    Game=Win    
                #Match Tie Condition    
                elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
                    Game=Draw    
                else:
                    Game=Running
            print('GAME DESIGNED BY RISHABH AGRAWAL')    
            print("Player 1 [X] --- Player 2 [O]\n")    
            print()    
            print()    
            print("Please Wait...")    
            time.sleep(3)    
            while(Game == Running):    
                choice=0;
                os.system('cls')    
                DrawBoard()    
                if(player % 2 != 0):    
                    print("Player 1's chance")    
                    Mark = 'X'    
                else:    
                    print("Player 2's chance")    
                    Mark = 'O'    
                
                
                
                while(choice>9 or choice==0):
                    choice = int(input("Enter the position between [1-9] where you want to mark : "))    
                    
                if(CheckPosition(choice)):    
                    board[choice] = Mark    
                    player+=1    
                    CheckWin()    
                
            os.system('cls')    
            DrawBoard()    
            if(Game==Draw):    
                time.sleep(6)
                print("Game Draw")    
            elif(Game==Win):    
                player-=1    
                if(player%2!=0):    
                    time.sleep(10)
                    print("Player 1 Won")    
                else:    
                    time.sleep(10)
                    print("Player 2 Won")
            time.sleep(2)
            ques=input('Wanna play this mode again(yes/no)?')
            a=input('Wanna play the other mode(yes/no)?')
        elif x=='b':
            a=input('Are you ready(y/n)?')
        if a=='n':
            k=input('Are you scared(y/n)?')
            if k=='n':
                a=input('choose again wisely...do you wanna play?(yes/no)?')
            elif k=='y':
                print('I knew it')
            else:
                print('Are you so scared that you cannot even type properly.Shut Up and Play')
        while a!='no':
            import random
            import time
            
            board=[i for i in range(0,9)]
            player, computer = '',''
            
            # Corners, Center and Others, respectively
            moves=((1,7,3,9),(5,),(2,4,6,8))
            # Winner combinations
            winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
            # Table
            tab=range(1,10)
            
            def print_board():
                x=1
                for i in board:
                    end = ' | '
                    if x%3 == 0:
                        end = ' \n'
                        if i != 1: end+='---------\n';
                    char=' '
                    if i in ('X','O'): char=i;
                    x+=1
                    print(char,end=end)
                    
            def select_char():
                chars=('X','O')
                if random.randint(0,1) == 0:
                    return chars[::-1]
                return chars
            
            def can_move(brd, player, move):
                if move in tab and brd[move-1] == move-1:
                    return True
                return False
            
            def can_win(brd, player, move):
                places=[]
                x=0
                for i in brd:
                    if i == player: places.append(x);
                    x+=1
                win=True
                for tup in winners:
                    win=True
                    for ix in tup:
                        if brd[ix] != player:
                            win=False
                            break
                    if win == True:
                        break
                return win
            
            def make_move(brd, player, move, undo=False):
                if can_move(brd, player, move):
                    brd[move-1] = player
                    win=can_win(brd, player, move)
                    if undo:
                        brd[move-1] = move-1
                    return (True, win)
                return (False, False)
            
            # AI goes here
            def computer_move():
                move=-1
                # If I can win, others don't matter.
                for i in range(1,10):
                    if make_move(board, computer, i, True)[1]:
                        move=i
                        break
                if move == -1:
                    # If player can win, block him.
                    for i in range(1,10):
                        if make_move(board, player, i, True)[1]:
                            move=i
                            break
                if move == -1:
                    # Otherwise, try to take one of desired places.
                    for tup in moves:
                        for mv in tup:
                            if move == -1 and can_move(board, computer, mv):
                                move=mv
                                break
                return make_move(board, computer, move)
            
            def space_exist():
                return board.count('X') + board.count('O') != 9
            
            player, computer = select_char()
            print('Player is [%s] and computer is [%s]' % (player, computer))
            result='%%% Deuce ! %%%'
            while space_exist():
                print_board()
                print('# Make your move ! [1-9] : ', end='')
                move = int(input())
                moved, won = make_move(board, player, move)
                if not moved:
                    print(' >> Invalid number ! Try again !')
                    continue
                #
                if won:
                    result='*** Congratulations ! You won ! ***'
                    break
                elif computer_move()[1]:
                    result='=== You lose ! =='
                    break
            
            print_board()
            time.sleep(4)
            print(result)
            time.sleep(3)
            a=input('Wanna play this mode again(yes/no)?')
            ques=input('Wanna play the other mode(yes/no)?')
    print('Made by RISHABH')
