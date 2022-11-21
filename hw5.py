import random
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def RemoveWords(string):
    words = string.split()
    i = 0
    while i < len(words):
        j = 0
        print(words[i])
        while j < len(words[i]):
            if words[i][j] == 'а' and j <= len(words[i])-2 and words[i][j+1] == 'б' and words[i][j+2] == 'в':
                words.pop(i)
                i -= 1
                break
            j += 1
        i += 1
    return words


print(RemoveWords("Пабв пппп лллабв абвжддд, абв Ввабввв kkk pppабв."))

# Создайте программу для игры с конфетами человек против человека.




# Создайте программу для игры в ""Крестики-нолики"".


row = lambda:  ["|   ", "|   |", "   |"]


matrix = [row(), row(), row()]
# print(matrix)


def CheckWin(coord, player):
    if player == True:
        player = 1
    else:
        player = 2
    comb1 = [[0, 0], [0, 1], [0, 2]]
    comb2 = [[0, 0], [1, 1], [2, 2]]
    comb3 = [[0, 0], [1, 0], [2, 0]]
    comb4 = [[2, 0], [1, 1], [0, 2]]
    k = 0
    while k < 3:
        j = 0
        for i in coord:
            if i in map(lambda x: [x[0]+k, x[1]], comb1):
                j += 1
        if j == 3:
            return player
        j = 0
        for i in coord:
            if i in comb2:
                j += 1
        if j == 3:
            return player
        j = 0
        for i in coord:
            if i in comb4:
                j += 1
        if j == 3:
            return player
        j = 0
        for i in coord:
            if i in map(lambda x: [x[0], x[1]+k], comb3):
                j += 1
        if j == 3:
            return player
        k += 1
    return 0


def InitField(matrix, x, y, value):
    if y == 0:
        matrix[x][y] = f'| {value} '
    elif y == 1:
        matrix[x][y] = f'| {value} |'
    elif y == 2:
        matrix[x][y] = f' {value} |'
    i, j = [0, 0]
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            print(f'{matrix[i][j]}', end='')
            j += 1
        print("\n-------------")
        i += 1
    return matrix


player = False
i = 0
firstPlayer = []
secondPlayer = []
while (i < 9):
    player = not player
    if player == True:
        symbol = 'crosses'
    else:
        symbol = 'nulls'
    x = int(input(f'{symbol} row: '))-1
    y = int(input(f'{symbol} col: '))-1
    if [x,y] in firstPlayer or [x,y] in secondPlayer:
        continue
    if player:
        firstPlayer.append([x, y])
        matrix = InitField(matrix, x, y, 'x')
        if CheckWin(firstPlayer, player) > 0:
            print("Crosses win!")
            break
    else:
        secondPlayer.append([x, y])
        matrix = InitField(matrix, x, y, '0')
        if CheckWin(secondPlayer, player) > 0:
            print("Nulls win!")
            break

    i += 1
if i == 9:
    print("Draw!")
