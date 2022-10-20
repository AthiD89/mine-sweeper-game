# ===  MineSweeper ===

#Creating the original grid
#Declare constants
EMPTY = "-"
MINE = "#"
UNKNOWN = "*"
FLAG = "$"

grid = [["-","-","-","#","#","-","-","#","-"],
        ["-","#","-","-","-""-","-","-","-",],
        ["-","-","#","-","-""-","-","#","-",],
        ["-","#","#","-","-","-","-","-","#"],
        ["-","#","#","-","#""-","-","#","-",],
        ["-","#","-","-","-","-","-","#","-"],
        ["-","#","#","-","-","-","-","#","-"],
        ["#","-","#","-","-""-","-","-","-",],
        ["-","-","-","-","-","-","-","#","-"]]

player_grid = [["*","*","*","*","*","*","*","*","*"],
              ["*","*","*","*","*""*","*","*","*",],
              ["*","*","*","*","*""*","*","*","*",],
              ["*","*","*","*","*""*","*","*","*",],
              ["*","*","*","*","*","*","*","*","*"],
              ["*","*","*","*","*","*","*","*","*"],
              ["*","*","*","*","*","*","*","*","*"],
              ["*","*","*","*","*","*","*","*","*"],
              ["*","*","*","*","*","*","*","*","*"]]

def count(row, col):
    offsets = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(1,-1))
    count = 0
    for offset in offsets:
        offset_row = row + offset[0]
        offset_col = col + offset[1]

        #check for boundaries
        if ((offset_row>=0 and offset_row<=8) and (offset_col>=0 and offset_col<=8)):
            if grid[offset_row][offset_col] == MINE:
                count += 1
    return count


def click(row, col):
    #check if it is a mine
    if grid[row][col] == MINE:
        print("BOOM!")
    elif player_grid[row][col] == UNKNOWN:
        player_grid[row][col] = count(row,col)

        #find all connected mines
        cells = [(row, col)]
        offsets = ((-1,0),(0,1),(1,0),(0,-1))
        while len(cells) > 0:
        #Count the mines Left right, south and north
            cell = cells.pop()
            for offset in offsets:
                row = offset[0] + cell[0]
                col = offset[1] + cell[1]
                if ((grid[row][col] == UNKNOWN) and (player_grid[row][col]== EMPTY) and (count(row, col)==EMPTY)):
                    grid[row][col] = count[row][col]

                    if (row, col) not in cells:
                        cells.append((row, col))
                    else:
                        grid[row][col] = count[row][col]
                        
        
        
        

def set_flag(row, col):
    if grid[row][col] == UNKNOWN:
        grid[row][col] = FLAG

def show_grid():
    symbols = {"-":"1", "#":"2"}
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            value = grid[row][col]
            if value in symbols:
                symbol = symbols[value]
            else:
                symbol = str(value)
            print(f"{symbol} ", end='')
        print("")


#Testing code
click(2, 3)
set_flag(1,1)
show_grid()
print(count(7,3))




