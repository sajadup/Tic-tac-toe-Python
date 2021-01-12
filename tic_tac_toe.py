import random
import sys

board=[i for i in range(0,9)]
player, computer = '',''
moves=((1,7,3,9),(5,),(2,4,6,8))
winner=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
tab=range(1,10)

def ttt_board():
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

def ttt_select():
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[::-1]
    return chars

def ttt_move(panel, player, move):
    if move in tab and panel[move-1] == move-1:
        return True
    return False

def ttt_play(panel, player, move, undo=False):
    if ttt_move(panel, player, move):
        panel[move-1] = player
        win=ttt_win(panel, player, move)
        if undo:
            panel[move-1] = move-1
        return (True, win)
    return (False, False)

def ttt_computer():
    move=-1
    for i in range(1,10):
        if ttt_play(board, computer, i, True)[1]:
            move=i
            break
    if move == -1:
        for i in range(1,10):
            if ttt_play(board, player, i, True)[1]:
                move=i
                break
    if move == -1:    
        for tup in moves:
            for mv in tup:
                if move == -1 and ttt_move(board, computer, mv):
                    move=mv
                    break
    return ttt_play(board, computer, move)

def ttt_win(panel, player, move):
    places=[]
    x=0
    for i in panel:
        if i == player: places.append(x);
        x+=1
    win=True
    for tup in winner:
        win=True
        for ix in tup:
            if panel[ix] != player:
                win=False
                break
        if win == True:
            break
    return win

def ttt_check():
    return board.count('X') + board.count('O') != 9

player, computer = ttt_select()
result='Draw'
while ttt_check():
    ttt_board()
    print('Your turn ! [1-9] : ', end='')
    move = int(input())
    moved, won = ttt_play(board, player, move)
    if not moved:
        print('Invalid number')
        continue
    if won:
        result='You won'
        break
    elif ttt_computer()[1]:
        result='You lose'
        break;

ttt_board()
print(result)