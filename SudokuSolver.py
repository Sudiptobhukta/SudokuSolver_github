def sodokuSolver(board):
    row= -1
    col=-1
    flag = False

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                row = i
                col=j
                flag = True
                break
        if flag is True:
            break
    
    if row == -1:
        return True
    
    for num in range(1,10):
        if isPresentCheck(board,row,col,num):
            board[row][col]=num
        if sodokuSolver(board) is True:
            return True
        board[row][col]=0
    return False


def isPresentCheck(board,row,col,num):
    if presentRow(board,row,num):
        return False
    if presentCol(board,col,num):
        return False
    if presentInbox(board,row-(row%3),col-(col%3),num):
        return False
    return True

#CHECKING IN THE ROW
def presentRow(board,row,num):
    for i in range(9):
        if board[row][i] == num:
            return True
    return False

#CHECKING IN THE COLUMN
def presentCol(board,col,num):
    for i in range(9):
        if board[i][col]==num:
            return True
    return False

# CHECKING THE BOX
def presentInbox(board,row,col,num):
    for i in range(9):
        for j in range(9):
            if board[i][j]==num:
                return True
    return False



matrix = [[int(ele) for ele in input().split()]for i in range(9)]
ans= sodokuSolver(matrix)
if ans is True:
    print('True')
else:
    print('False')