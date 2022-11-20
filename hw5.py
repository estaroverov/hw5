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


def Step(player, limit=28):
    step = int(input(f"Игрок {player}, Ваш ход: "))
    while step <= 0 or step > limit:
        step = int(input(f"Игрок {player}, Ваш ход: "))
    return step


def FinishGame(numSweets, player, counterSteps, sum1, sum2, bot=True):
    print("Final")
    threshold = 56
    maxSweets = 28
    while numSweets >= threshold+2:
        if player == 2:
            player = 1
            if bot == True:
                diff = numSweets - threshold
                step = diff-2
            else:
                step = Step(player)
            sum1 += step
        else:
            player = 2
            step = Step(player)
            sum2 += step
        counterSteps += 1
        numSweets -= step  # <=58
        print(counterSteps, "ход. Игрок", player, "взял конфет:", step)
        print("Осталось конфет:", numSweets)
    j = 0
    while numSweets > 0:
        if j == 0:
            if numSweets >= threshold+2:  # >=58
                if player == 1:
                    player = 2
                    step = Step(player)
                    sum2 += step
                else:
                    if step == maxSweets:  #
                        if bot == True:
                            step = 1  # Останется 29
                        else:
                            step = Step(player)
                    elif step < maxSweets:
                        if bot == True:
                            diff = numSweets - 30
                            step = diff + 1
                        else:
                            step = Step(player)
                    sum1 += step
                    player = 1
                    j += 1
            else:
                if player == 1:
                    player = 2
                    step = Step(player)
                    sum2 += step
                else:
                    if numSweets > 29 and numSweets < 58:  # оста
                        player = 1
                        if bot == True:
                            diff = numSweets - 30
                            step = diff+1  # Останется 29
                        else:
                            step = Step(player)
                        sum1 += step
                    j += 1
        else:
            if player == 1:
                player = 2
                step = Step(player, numSweets)
                sum2 += step
            else:
                player = 1
                if bot == True:
                    step = numSweets  # Останется 29\
                else:
                    step = Step(player, numSweets)
                sum1 += step

        counterSteps += 1
        numSweets -= step  # 58
        print(counterSteps, "ход. Игрок", player, "взял конфет:", step)
        print("Осталось конфет:", numSweets)

    print("Игрок 1 взял конфет:", sum1)
    print("Игрок 2 взял конфет:", sum2)
    return player


def Game(numSweets, player, bot=True):
    counter = 0
    i = numSweets
    sum1 = 0
    sum2 = 0
    maxSweets = 28
    threshold = 56
    while i > 0:
        counter += 1
        if player == 1:
            if bot == True:
                step = random.randint(1, maxSweets)
            else:
                step = Step(player)
        else:
            step = Step(player)
        i -= step
        print(counter, "ход. Игрок", player, "взял конфет:", step)
        if player == 1:
            sum1 += step
        else:
            sum2 += step
        print("Осталось конфет:", i)
        diff = i-threshold
        if diff <= maxSweets and i > threshold:
            return FinishGame(i, player, counter, sum1, sum2, bot)
        else:
            player = 1 if player == 2 else 2
        print(sum2) if player == 1 else print(sum1)

    # return player


player = random.randint(1, 2)
print(Game(300, player, True), "winner")

print("Первый ход сделал игрок №", player)
