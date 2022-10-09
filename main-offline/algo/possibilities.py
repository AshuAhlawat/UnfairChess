def possibilities(position_array, active_piece_pos):

    zero_array = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]
    def pawn(x, y, color, zero_array):
        
        try:
            if color == "w":
                if y == 6:
                    if position_array[y-1][x] == "" and position_array[y-2][x] == "":
                        zero_array[y-1][x] = 1
                        zero_array[y-2][x] = 1
                    elif position_array[y-1][x] == "":
                        zero_array[y-1][x] = 1
                else:
                    if position_array[y-1][x] == "":
                        zero_array[y-1][x] = 1
                        
                if x == 0:
                    if position_array[y-1][x+1] !="":
                        zero_array[y-1][x+1] = 1
                elif x == 7:
                    if position_array[y-1][x-1] !="":
                        zero_array[y-1][x-1] = 1
                else:
                    if position_array[y-1][x-1] !="":
                        zero_array[y-1][x-1] = 1
                    if position_array[y-1][x+1] !="":
                        zero_array[y-1][x+1] = 1
                    
            else:
                if y == 1:
                    if position_array[y+1][x] == "" and position_array[y+2][x] == "":
                        zero_array[y+1][x] = 1
                        zero_array[y+2][x] = 1
                    elif position_array[y+1][x] == "":
                        zero_array[y+1][x] = 1
                else:
                    if position_array[y+1][x] == "":
                        zero_array[y+1][x] = 1
                        
                if x == 0:
                    if position_array[y+1][x+1] !="":
                        zero_array[y+1][x+1] = 1
                elif x == 7:
                    if position_array[y+1][x-1] !="":
                        zero_array[y+1][x-1] = 1
                else:
                    if position_array[y+1][x-1] !="":
                        zero_array[y+1][x-1] = 1
                    if position_array[y+1][x+1] !="":
                        zero_array[y+1][x+1] = 1
        except:
            pass
        return zero_array
    
    def rook(x, y ,zero_array):

        i = y
        while i > 0:
            i -= 1
            if position_array[i][x] == "":
                zero_array[i][x] = 1
            else:
                zero_array[i][x] = 1
                break
        i = y
        while i < 7:
            i += 1
            if position_array[i][x] == "":
                zero_array[i][x] = 1
            else:
                zero_array[i][x] = 1
                break
        j = x
        while j > 0:
            j -= 1
            if position_array[y][j] == "":
                zero_array[y][j] = 1
            else:
                zero_array[y][j] = 1
                break
        j = x
        while j < 7:
            j += 1
            if position_array[y][j] == "":
                zero_array[y][j] = 1
            else:
                zero_array[y][j] = 1
                break
            
        return zero_array
            
    def bishop(x, y, zero_array):
        
        i = y
        j = x
        while i > 0 and j > 0:
            i -= 1
            j -= 1
            try:
                if position_array[i][j] == "":
                    zero_array[i][j] = 1
                else:
                    zero_array[i][j] = 1
                    break
            except:
                break
        i = y
        j = x
        while i > 0 and j < 7:
            i -= 1
            j += 1
            try:
                if position_array[i][j] == "":
                    zero_array[i][j] = 1
                else:
                    zero_array[i][j] = 1
                    break
            except:
                break
            
        i = y
        j = x
        while i < 7 and j > 0:
            i += 1
            j -= 1
            try:
                if position_array[i][j] == "":
                    zero_array[i][j] = 1
                else:
                    zero_array[i][j] = 1
                    break
            except:
                break
        i = y
        j = x
        while i < 7 and j < 7:
            i += 1
            j += 1
            try:
                if position_array[i][j] == "":
                    zero_array[i][j] = 1
                else:
                    zero_array[i][j] = 1
                    break
            except:
                break
        return zero_array
        
    def queen(x, y, zero_array):
        zero_array = bishop(x,y, zero_array)
        zero_array = rook(x,y,zero_array)
        
        return zero_array
        
        
    def knight(x, y, zero_array):
        x += 1
        y += 1
        
        try:
            if y>=2:
                zero_array[y-2][x+1] = 1
        except:
            pass

        try:
            if y >=3 and x >=0:
                zero_array[y-3][x] = 1
        except:
            pass

        try:
            zero_array[y][x+1] = 1
        except:
            pass

        try:
            if y >=3 and x >=2:
                zero_array[y-3][x-2] = 1
        except:
            pass

        try:
            if y >=0 and x >=3:
                zero_array[y][x-3] = 1
        except:
            pass

        try:
            if y >=2 and x >=3:
                zero_array[y-2][x-3] = 1
        except:
            pass

        try:
            if y >=0 and x >=2:
                zero_array[y+1][x-2] = 1

        except:
            pass

        try:
            zero_array[y+1][x] = 1

        except:
            pass
        
        return zero_array
    def king(x, y, zero_array):
        x += 1
        y += 1
        
        try:
            if y -1 >= 0:
                zero_array[y-1][x] = 1
        except:
            pass

        try:
            if y -2 >= 0:
                zero_array[y-2][x] = 1
        except:
            pass

        try:
                zero_array[y][x] = 1
        except:
            pass

        try:
            if y -2 >= 0 and x - 2>= 0:
                zero_array[y-2][x-2] = 1
        except:
            pass

        try:
            if x-2>= 0:
                zero_array[y][x-2] = 1
        except:
            pass

        try:
            if y - 1 >= 0 and x >= 2:
                zero_array[y-1][x-2] = 1
        except:
            pass

        try:
            if  x >= 1:
                zero_array[y][x-1] = 1
        except:
            pass

        try:
            if y -2 >= 0 and x -1 >= 0:
                zero_array[y-2][x-1] = 1
        except:
            pass
        return zero_array

    active_x = active_piece_pos[0]
    active_y = active_piece_pos[1]

    active_piece = position_array[active_y][active_x]

    if active_piece:
        piece_kind = active_piece[1]
        
        if piece_kind == "P":
            if active_piece[0]== "w":
                active_color = "w"
            else:
                active_color = "b"
            final_array = pawn(active_x,active_y,active_color,zero_array)
            
        if piece_kind == "R":
            final_array = rook(active_x,active_y,zero_array)
        if piece_kind == "B":
            final_array = bishop(active_x,active_y,zero_array)
        if piece_kind == "K":
            try:
                active_piece[2]
                final_array = knight(active_x,active_y,zero_array)
            except:
                final_array = king(active_x,active_y,zero_array) 
        if piece_kind == "Q":
            final_array=queen(active_x,active_y,zero_array)
    else:
        final_array = zero_array

    return final_array
