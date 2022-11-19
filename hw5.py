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

def FinishGame(numSweets, player, counterSteps, sum1, sum2):
    print("Final")
    threshold = 56
    maxSweets = 28
    while numSweets >= threshold+2:
        if player == 2:
            player = 1
            diff = numSweets - threshold
            step = diff-2
            sum1 += step
        else:
            player = 2
            step = random.randint(1, maxSweets)
        counterSteps += 1
        numSweets -= step  # <=58
        print(counterSteps, "ход. Игрок", player, "взял конфет:", step)
        print("Осталось конфет:", numSweets)
    j = 0
    while numSweets > 0:
        if j == 0:
            if numSweets >= threshold+2: # >=58
                if player == 1:
                    player = 2
                    step = random.randint(1, maxSweets)
                    sum2 += step
                else:
                    if step == maxSweets:  # оста
                        step = 1  # Останется 29
                        sum1 += step
                    elif step < maxSweets:
                        diff = numSweets - 30
                        step = diff + 1
                    player = 1
                    j += 1
            else:
                if player == 1:
                    player = 2
                    step = random.randint(1, maxSweets)
                    sum2 += step
                else:
                    if numSweets>29 and numSweets<58:  # оста
                        diff = numSweets - 30
                        step = diff+1
                        sum1 += step
                    elif step < maxSweets:
                        diff = numSweets - 30
                        step = diff + 1
                    player = 1
                    j += 1
        else:
            if player == 1:
                player = 2
                step = random.randint(1, maxSweets)
                sum2 += step
            else:

                player = 1
                step = numSweets  # Останется 29
                sum1 += step

        counterSteps += 1
        numSweets -= step  # 58
        print(counterSteps, "ход. Игрок", player, "взял конфет:", step)
        print("Осталось конфет:", numSweets)

    print("Игрок 1 взял конфет:", sum1)
    print("Игрок 2 взял конфет:", sum2)
    return player


def Game(numSweets, player):
    counter = 0
    i = numSweets
    sum1 = 0
    sum2 = 0
    maxSweets = 28
    threshold = 56
    while i > 0:
        counter += 1
        step = random.randint(1, maxSweets)

        if i >= maxSweets:
            i -= step
        else:
            print(counter, "ход. Игрок", player, "взял конфет:", i)
            i -= i
            break
        print(counter, "ход. Игрок", player, "взял конфет:", step)
        if player == 1:
            sum1 += step
        else:
            sum2 += step
        print("Осталось конфет:", i)
        diff = i-threshold
        if diff <= maxSweets and i > threshold:
            return FinishGame(i, player, counter, sum1, sum2)
        else:
            player = 1 if player == 2 else 2
        print(sum1) if player == 1 else print(sum2)

    return player


player = random.randint(1, 2)
print(Game(300, player), "winner")

print("Первый ход сделал игрок №", player)
