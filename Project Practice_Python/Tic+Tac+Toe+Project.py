
# coding: utf-8

# In[62]:

from IPython.display import clear_output
keypad = ['0','1','2','3','4','5','6','7','8']
board = ['i1','i2','i3','j1','j2','j3','k1','k2','k3']

# Creat a Board


# In[63]:

def restart_game():
    print 'Welcome to Wei Chien Tic Tac Toe Game'
    global keypad,board
    keypad = ['0','1','2','3','4','5','6','7','8']
    board = ['i1','i2','i3','j1','j2','j3','k1','k2','k3']
    global n
    n = 1


# In[64]:

def board_print():
    clear_output()
    print('   |   |')
    print(' ' + keypad[0] + ' | ' + keypad[1] + ' | ' + keypad[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + keypad[3] + ' | ' + keypad[4] + ' | ' + keypad[5])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + keypad[6] + ' | ' + keypad[7] + ' | ' + keypad[8])
    print('   |   |')
# Print a board


def player1():
    
    loc = ''
    while loc not in keypad:
        loc = raw_input('Player 1 where you want to put your O:') 
        
    for loc_change in keypad:
        if loc_change == loc:
            board [int(keypad[int(loc_change)])] = 'O'
            keypad[int(keypad[int(loc_change)])] = 'O'
                
    board_print()


# In[66]:

def player2():
    
    loc2 = ''
    while loc2 not in keypad:
        loc2 = raw_input('Player 2 where you want to put your X:') 
        
    for loc2_change in keypad:
        if loc2_change == loc2:
            board [int(keypad[int(loc2_change)])] = 'X'
            keypad[int(keypad[int(loc2_change)])] = 'X'
                
    board_print()



# In[67]:

def check_tie():
    board_check_str = "".join(board)
    if board_check_str.isalpha():
        print'Game Tied. There is no winer'
        global n
        n = 0
    else:
        check_win_lost()
    


# In[68]:

def check_win_lost():
    if board[0]==board[1]==board[2] or board[3]==board[4]==board[5] or board[6]==board[7]==board[8] or board[0]==board[3]==board[6] or board[1]==board[4]==board[7] or board[2]==board[5]==board[8] or board[0]==board[4]==board[8]or board[2]==board[4]==board[6]:
        if board[0]==board[1]==board[2]=='X' or board[3]==board[4]==board[5]=='X' or board[6]==board[7]==board[8]=='X' or board[0]==board[3]==board[6]=='X' or board[1]==board[4]==board[7]=='X' or board[2]==board[5]==board[8]=='X' or board[0]==board[4]==board[8]=='X'or board[2]==board[4]==board[6]=='X':
            print'Player 2 is a winer'
            global n
            n = 0
        else:
            print'Player 1 is a winer'
            n = 0    
    else:
        pass


# In[69]:

def game():
    restart_game()
    board_print()
    while n>0:
        player1()
        check_tie()
        if n!=0:
            player2()
            check_tie()
        else:
            pass
    else:
        print'The Game is end'
        


# In[71]:

game()


# In[ ]:



