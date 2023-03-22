# Initial value

row0 = [0,0,0,0,0,0,0,0,0,0] # unavailable
row1 = [0,0,0,0,0,0,0,0,0,0]
row2 = [0,0,0,0,0,0,0,0,0,0]
row3 = [0,0,0,0,0,0,0,0,0,0]
row4 = [0,0,0,0,1,2,0,0,0,0]
row5 = [0,0,0,0,2,1,0,0,0,0]
row6 = [0,0,0,0,2,0,0,0,0,0]
row7 = [0,0,0,2,2,0,0,0,0,0]
row8 = [0,0,0,0,0,0,0,0,0,0]
row9 = [0,0,0,0,0,0,0,0,0,0] # unavailable

rows = [row0,row1,row2,row3,row4,row5,row6,row7,row8,row9]

# Setting

color = 1 # 1 is black, 2 is white
row_num = 6 # 1~8
column_num = 3 # 1~8

def othello(rows,color,row_num,column_num):

    if color == 1:
        other_color = 2
    if color == 2:
        other_color = 1

    around_sum = rows[row_num-1][column_num-1] + rows[row_num][column_num-1] + rows[row_num+1][column_num-1]
    + rows[row_num-1][column_num] + rows[row_num][column_num] + rows[row_num+1][column_num]
    + rows[row_num-1][column_num+1] + rows[row_num][column_num+1] + rows[row_num+1][column_num+1]

    upper = (-1,0)
    upper_right = (-1,1)
    right = (0,1)
    bottom_right = (1,1)
    bottom = (1,0)
    bottom_left = (1,-1)
    left = (0,-1)
    upper_left = (-1,-1)

    # the difinition of the vector
    vectors = [upper,upper_right,right,bottom_right,bottom,bottom_left,left,upper_left]

    if around_sum != 0:
        print('そこには置けません')
    else: # the case that the player can put the own stone
        place_check = False
        for vector in vectors:
            turnover = []
            for cnt in range(7):
                # the case of the other color
                if rows[row_num + vector[0] * (cnt+1)][column_num + vector[1] * (cnt+1)] == other_color:
                    turnover.append(cnt)
                # the case of the color
                elif rows[row_num + vector[0] * (cnt+1)][column_num + vector[1] * (cnt+1)] == color:
                    for turnover_cnt in turnover:
                        rows[row_num + vector[0] * (turnover_cnt+1)][column_num + vector[1] * (turnover_cnt+1)] = color
                    place_check = True
                # the case of no color
                else:
                    break
        if place_check:
            rows[row_num][column_num] = color
            print('置くことができました')
        else:
            print('そこには置けません')

    # Totalling
    black_score = 0
    white_score = 0
    for row in rows[1:8]:
        for value in row[1:8]:
            if value == 1:
                black_score += 1
            elif value == 2:
                white_score += 1


    # Console

    print(row1[1:8])
    print(row2[1:8])
    print(row3[1:8])
    print(row4[1:8])
    print(row5[1:8])
    print(row6[1:8])
    print(row7[1:8])
    print(row8[1:8])

    print('black',black_score)
    print('white',white_score)