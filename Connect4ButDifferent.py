BoardList = [[' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
             [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
             [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
             [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
             [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
             [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
             [' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - '],
             [' 1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ']]


def PrintBoard(BoardList):
    for i in BoardList:
        row = ""
        for j in i:
            row += j
        print(row)


def PlacePiece(BoardList, column, player):
    # need to go into the column and see if the lowest row has a piece
    # if there is a piece check row above
    # thinking recursion but idk how i'd do it, it feels wrong tbh
    i = 6
    row = 6
    while i >= 0:
        if BoardList[row][column] != ' - ':
            i -= 1
            row -= 1
        else:
            BoardList[row][column] = player
            i = -2
    # return the location of the piece to check if there is a 4 in a row
    return [row, column]


def MoveInput(BoardList, Turn):
    # take input of column for the move
    # see if input is a number from 1-7
    # see if that column can have a piece played in the first place
    if Turn % 2 == 0:
        column = input("Player 1: Please pick a column: ")
    else:
        column = input("Player 2: Please pick a column: ")
    if column.isdigit() == False:
        print("Please input a number from 1 to 7")
        return False
    else:
        column = int(column)
        if column not in range(1, 8):
            print("Please input a number from 1 to 7")
            return False
        elif BoardList[0][column-1] != ' - ':
            print("That column is full")
            return False
        else:
            if Turn % 2 == 0:
                player = ' X '
            else:
                player = ' O '
            # by returning what place piece returned it returns the location of the move
            return PlacePiece(BoardList, column-1, player)


def CheckRows(BoardList):
    Xwins = 0
    Owins = 0
    for row in BoardList[0:7]:
        rowpieces = ""
        for piece in row:
            rowpieces += piece[1]
        if 'XXXX' in rowpieces:
            Xwins += 1
        elif 'OOOO' in rowpieces:
            Owins += 1
    return Xwins, Owins


def CheckCols(BoardList):
    Xwins = 0
    Owins = 0
    for col in range(0, 7):
        colpieces = ""
        for row in range(0, 7):
            piece = BoardList[row][col]
            colpieces += piece[1]
        if 'XXXX' in colpieces:
            Xwins += 1
        elif 'OOOO' in colpieces:
            Owins += 1
    return Xwins, Owins


def Check4s(set):
    Xwins = 0
    Owins = 0
    if 'XXXX' in set:
        Xwins += 1
    elif 'OOOO' in set:
        Owins += 1

    if Xwins == 0 and Owins == 0:
        return False
    else:
        return Xwins, Owins


def MakeSetDown(BoardList, row, col):
    set = ""
    while row < 7 and col < 7:
        set += BoardList[row][col][1]
        row += 1
        col += 1
    return set


def MakeSetUp(BoardList, row, col):
    set = ""
    while row < 7 and col >= 0:
        set += BoardList[row][col][1]
        row += 1
        col -= 1
    return set


def CheckDigs(BoardList):
    Xwins = 0
    Owins = 0
    RD1set = MakeSetDown(BoardList, 0, 3)
    RD1 = Check4s(RD1set)
    if RD1 != False:
        XRD1wins, ORD1wins = RD1
        Xwins += XRD1wins
        Owins += ORD1wins
    RD2set = MakeSetDown(BoardList, 0, 2)
    RD2 = Check4s(RD2set)
    if RD2 != False:
        XRD2wins, ORD2wins = RD2
        Xwins += XRD2wins
        Owins += ORD2wins
    RD3set = MakeSetDown(BoardList, 0, 1)
    RD3 = Check4s(RD3set)
    if RD3 != False:
        XRD3wins, ORD3wins = RD3
        Xwins += XRD3wins
        Owins += ORD3wins
    RD4set = MakeSetDown(BoardList, 0, 0)
    RD4 = Check4s(RD4set)
    if RD4 != False:
        XRD4wins, ORD4wins = RD4
        Xwins += XRD4wins
        Owins += ORD4wins
    RD5set = MakeSetDown(BoardList, 1, 0)
    RD5 = Check4s(RD5set)
    if RD5 != False:
        XRD5wins, ORD5wins = RD5
        Xwins += XRD5wins
        Owins += ORD5wins
    RD6set = MakeSetDown(BoardList, 2, 0)
    RD6 = Check4s(RD6set)
    if RD6 != False:
        XRD6wins, ORD6wins = RD6
        Xwins += XRD6wins
        Owins += ORD6wins
    RD7set = MakeSetDown(BoardList, 3, 0)
    RD7 = Check4s(RD7set)
    if RD7 != False:
        XRD7wins, ORD7wins = RD7
        Xwins += XRD7wins
        Owins += ORD7wins
    LU1set = MakeSetUp(BoardList, 0, 3)
    LU1 = Check4s(LU1set)
    if LU1 != False:
        XLU1wins, OLU1wins = LU1
        Xwins += XLU1wins
        Owins += OLU1wins
    LU2set = MakeSetUp(BoardList, 0, 4)
    LU2 = Check4s(LU2set)
    if LU2 != False:
        XLU2wins, OLU2wins = LU2
        Xwins += XLU2wins
        Owins += OLU2wins
    LU3set = MakeSetUp(BoardList, 0, 5)
    LU3 = Check4s(LU3set)
    if LU3 != False:
        XLU3wins, OLU3wins = LU3
        Xwins += XLU3wins
        Owins += OLU3wins
    LU4set = MakeSetUp(BoardList, 0, 6)
    LU4 = Check4s(LU4set)
    if LU4 != False:
        XLU4wins, OLU4wins = LU4
        Xwins += XLU4wins
        Owins += OLU4wins
    LU5set = MakeSetUp(BoardList, 1, 6)
    LU5 = Check4s(LU5set)
    if LU5 != False:
        XLU5wins, OLU5wins = LU5
        Xwins += XLU5wins
        Owins += OLU5wins
    LU6set = MakeSetUp(BoardList, 2, 6)
    LU6 = Check4s(LU6set)
    if LU6 != False:
        XLU6wins, OLU6wins = LU6
        Xwins += XLU6wins
        Owins += OLU6wins
    LU7set = MakeSetUp(BoardList, 3, 6)
    LU7 = Check4s(LU7set)
    if LU7 != False:
        XLU7wins, OLU7wins = LU7
        Xwins += XLU7wins
        Owins += OLU7wins
    return Xwins, Owins


def Check4InARow(BoardList):
    Xwins = 0
    Owins = 0
    rows = CheckRows(BoardList)
    if rows != False:
        Xrwins, Orwins = rows
        Xwins += Xrwins
        Owins += Orwins
    cols = CheckCols(BoardList)
    if cols != False:
        Xcwins, Ocwins = cols
        Xwins += Xcwins
        Owins += Ocwins
    digs = CheckDigs(BoardList)
    if digs != False:
        Xdwins, Odwins = digs
        Xwins += Xdwins
        Owins += Odwins
    if Xwins == 0 and Owins == 0:
        return False
    else:
        return Xwins, Owins


def FakeRotateBoard(BoardList):
    NewBoard = []
    col = 6
    while col >= 0:
        newrow = []
        for row in range(0, 7):
            piece = BoardList[row][col]
            newrow.append(piece)
        NewBoard.append(newrow)
        col -= 1
    NewBoard.append(BoardList[7])
    return NewBoard


def Gravity(BoardList):
    NewBoard = []
    for col in range(0, 7):
        newcol = []
        row = 6
        while row >= 0:
            piece = BoardList[row][col]
            if piece != " - ":
                newcol.append(piece)
            row -= 1
        while len(newcol) <= 6:
            newcol.append(' - ')
        NewBoard.append(newcol)
    NewBoard.append(BoardList[7])
    FinalBoard = FakeRotateBoard(NewBoard)
    return FinalBoard


def RotateBoard(BoardList):
    NewBoard = []
    for col in range(0, 7):
        newrow = []
        row = 6
        while row >= 0:
            piece = BoardList[row][col]
            newrow.append(piece)
            row -= 1
        NewBoard.append(newrow)
    NewBoard.append(BoardList[7])
    FinalBoard = Gravity(NewBoard)
    print("The Board Has Rotated Clockwise!!")
    return FinalBoard


def PlayConnect4ButDifferent(BoardList):
    Turn = 0
    x = False
    while x == False:
        if Turn == 49:
            print('----------------------------')
            PrintBoard(BoardList)
            print("Game Over")
            print("Draw!")
            x = True
        else:
            PrintBoard(BoardList)
            print('----------------------------')
            MovePossible = MoveInput(BoardList, Turn)
            if MovePossible == False:
                x = False
            else:
                Turn += 1
                x = Check4InARow(BoardList)
                print('----------------------------')
                if Turn % 2 == 0:
                    PrintBoard(BoardList)
                    print('----------------------------')
                    BoardList = RotateBoard(BoardList)
                    x = Check4InARow(BoardList)
                    print('----------------------------')
    Xwins, Owins = x
    PrintBoard(BoardList)
    print('----------------------------')
    print("Game Over!")
    if Xwins != 0 and Owins != 0:
        if Xwins == 1 and Owins == 1:
            print("Player 1 had 1 '4 in a Row' and Player 2 had 1 '4 in a Row'")
        elif Xwins == 1 and Owins != 1:
            print("Player 1 had 1 '4 in a Row' and Player 2 had",
                  Owins, "'4 in a Row's")
        else:
            print("Player 1 had", Xwins,
                  "'4 in a Row's and Player 2 had 1 '4 in a Row'")
    elif Xwins == 0 and Owins != 0:
        if Owins == 1:
            print("Player 2 had 1 '4 in a Row'")
        else:
            print("Player 2 had", Owins, "'4 in a Row's")
    else:
        if Xwins == 1:
            print("Player 1 had 1 '4 in a Row'")
        else:
            print("Player 1 had", Xwins, "'4 in a Row's")


PlayConnect4ButDifferent(BoardList)
