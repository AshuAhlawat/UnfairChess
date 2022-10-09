# FUNCTIONS


# ROOK
def rookattack(b_x, b_y, q_x, q_y):
    
    # creating empty board
    boardr = []
    for y in range(b_y):
        row = []
        for x in range(b_x):
            row.append(" ")
        boardr.append(row)

    # rooks attack
    for row in range(b_y):
        boardr[row][q_x-1] = "o"
    for col in range(b_x):
        boardr[q_y-1][col] = "o"

    # rooks position
    boardr[q_y-1][q_x-1] = "R"

    # printing board
    look = ""
    for y in boardr:
        for x in boardr[boardr.index(y)]:
            look += ("|"+x+"|  ")
        look += ("\n\n")
    print(look)


# BISHOP
def bishopattack(b_x, b_y, q_x, q_y):
    # creating empty board
    boardb = []
    for y in range(b_y):
        row = []
        for x in range(b_x):
            row.append(" ")
        boardb.append(row)

    # bishops attack
    for row in range(b_y):
        if q_x-q_y+row>=0:
            try:
                boardb[row][q_x-q_y+row]="o"
            except:
                pass
        
    for row in range(b_y):
        if q_x+q_y-row-2>=0:
            try:
                boardb[row][q_x+q_y-row-2]="o"
            except:
                pass
    
        
    # bishops position
    boardb[q_y-1][q_x-1] = "B"

    # printing board
    look = ""
    for y in boardb:
        for x in boardb[boardb.index(y)]:
            look += ("|"+x+"|  ")
        look += ("\n\n")
    print(look)

# KING
def kingattack(b_x, b_y, q_x, q_y):
    # creating empty board
    boardk = []
    for y in range(b_y):
        row = []
        for x in range(b_x):
            row.append(" ")
        boardk.append(row)
    
    # king attack
    try:
        if q_y -1 >= 0:
            boardk[q_y-1][q_x] = "o"
    except:
        pass

    try:
        if q_y -2 >= 0:
            boardk[q_y-2][q_x] = "o"
    except:
        pass

    try:
            boardk[q_y][q_x] = "o"
    except:
        pass

    try:
        if q_y -2 >= 0 and q_x - 2>= 0:
            boardk[q_y-2][q_x-2] = "o"
    except:
        pass

    try:
        if q_x-2>= 0:
            boardk[q_y][q_x-2] = "o"
    except:
        pass

    try:
        if q_y - 1 >= 0 and q_x >= 2:
            boardk[q_y-1][q_x-2] = "o"
    except:
        pass

    try:
        if  q_x >= 1:
            boardk[q_y][q_x-1] = "o"
    except:
        pass

    try:
        if q_y -2 >= 0 and q_x -1 >= 0:
            boardk[q_y-2][q_x-1] = "o"
    except:
        pass
    
    #kings position
    boardk[q_y-1][q_x-1] = "K"
    
    #printing board
    look = ""
    for y in boardk:
        for x in boardk[boardk.index(y)]:
            look += ("|"+x+"|  ")
        look += ("\n\n")
    print(look)

# KNIGHT
def knightattack(b_x, b_y, q_x, q_y):
    # creating empty board
    boardkn = []
    for y in range(b_y):
        row = []
        for x in range(b_x):
            row.append(" ")
        boardkn.append(row)

    # Knight attack
    try:
        if q_y-2>=0:
            boardkn[q_y-2][q_x+1] = "o"
    except:
        pass

    try:
        if q_y >=3 and q_x >=0:
            boardkn[q_y-3][q_x] = "o"
    except:
        pass

    try:
        boardkn[q_y][q_x+1] = "o"
    except:
        pass

    try:
        if q_y >=3 and q_x >=2:
            boardkn[q_y-3][q_x-2] = "o"
    except:
        pass

    try:
        if q_y >=0 and q_x >=3:
            boardkn[q_y][q_x-3] = "o"
    except:
        pass

    try:
        if q_y >=2 and q_x >=3:
            boardkn[q_y-2][q_x-3] = "o"
    except:
        pass

    try:
        if q_y >=0 and q_x >=2:
            boardkn[q_y+1][q_x-2] = "o"

    except:
        pass

    try:
        boardkn[q_y+1][q_x] = "o"

    except:
        pass

    # knight's position
    boardkn[q_y-1][q_x-1] = "N"

    # printing board
    look = ""
    for y in boardkn:
        for x in boardkn[boardkn.index(y)]:
            look += ("|"+x+"|  ")
        look += ("\n\n")
    print(look)

# QUEEN
def queenattack(b_x, b_y, q_x, q_y):
    
    # creating empty board
    boardq = []
    for y in range(b_y):
        row = []
        for x in range(b_x):
            row.append(" ")
        boardq.append(row)

    # queen's rook attack
    for row in range(b_y):
        boardq[row][q_x-1] = "o"
    for col in range(b_x):
        boardq[q_y-1][col] = "o"

    # queen's bishop attack
    for row in range(b_y):
        if q_x-q_y+row>=0:
            try:
                boardq[row][q_x-q_y+row]="o"
            except:
                pass
        
    for row in range(b_y):
        if q_x+q_y-row-2>=0:
            try:
                boardq[row][q_x+q_y-row-2]="o"
            except:
                pass
    
    # queens position
    boardq[q_y-1][q_x-1] = "Q"

    # printing board
    look = ""
    for y in boardq:
        for x in boardq[boardq.index(y)]:
            look += ("|"+x+"|  ")
        look += ("\n\n")
    print(look)

# MAIN
b_x = 8
b_y = 8

print("\n\n")

q_x = int(input("Location \n x : "))
q_y = int(input(" y : "))

print("\n\n")

print("Rook's Attack \n\n")
rookattack(b_x, b_y, q_x, q_y)

print("\n\n")

print("Bishop's Attack \n\n")
bishopattack(b_x, b_y, q_x, q_y)

print("\n\n")

print("King's Attack \n\n")
kingattack(b_x, b_y, q_x, q_y)

print("\n\n")

print("Knight's Attack \n\n")
knightattack(b_x, b_y, q_x, q_y)

print("\n\n")

print("Queen's Attack \n\n")
queenattack(b_x, b_y, q_x, q_y)

#CREDITS Capti/Silver

