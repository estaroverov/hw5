import random
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def RemoveWords(string):
    words = string.split()
    i = 0
    while i < len(words):
        j = 0
        while j < len(words[i]):
            if words[i][j] == 'а' and j <= len(words[i])-2 and words[i][j+1] == 'б' and words[i][j+2] == 'в':
                words.pop(i)
                i -= 1
                break
            j += 1
        i += 1
    return words


print(RemoveWords("Пабв пппп лллабв абвжддд, абв Ввабввв kkk pppабв."))

