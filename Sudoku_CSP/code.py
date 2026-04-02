# Sudoku (same logic, different writing)

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def safe(r, c, val):
    
    # row
    for j in range(9):
        if board[r][j] == val:
            return False
    
    # column
    for i in range(9):
        if board[i][c] == val:
            return False
    
    # box
    br = (r//3)*3
    bc = (c//3)*3
    
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if board[i][j] == val:
                return False
    
    return True

def dfs():
    for i in range(9):
        for j in range(9):
            
            if board[i][j] == 0:
                
                for v in range(1, 10):
                    if safe(i, j, v):
                        board[i][j] = v
                        
                        if dfs():
                            return True
                        
                        board[i][j] = 0
                
                return False
    return True

dfs()

print("Sudoku Solution:")
for r in board:
    print(r)