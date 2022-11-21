def encode(string):
    encoded = ''
    k = 1
    for i in string.split():
        j = 0
        k = 1
        while j < len(i)-1:
            if j == len(i) - 2:
                if i[j] == i[j+1]:
                    k += 1
                    encoded += str(k)+i[j+1]
                else:
                    encoded += str(k)+i[j]
                    k = 1
                    encoded += str(k)+i[j+1]
                break
            if i[j] == i[j+1]:
                k += 1
            else:
                encoded += str(k)+i[j]
                k = 1
            j += 1
        encoded += ' '

    return encoded


print(encode('Пабв ппппннннннннннннннн лллабввввввввввввв абвжддд, абв Ввабввв kkk pppабв.'))


def decode(encoded):
    words = encoded.split()
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    number = ''
    result = []
    word = ''
    for i in words:
        j = 0
        while j < len(i):
            if i[j] in numbers:
                number+=i[j]
                if j<=len(i)-2 and i[j+1] not in numbers:
                    word += i[j+1]*int(number)
                    number = ''
            if j == len(i)-1:
                result.append(word)
                word = ''
                break
            j+=1
    return ' '.join(result)

print(decode(encode('Пабв ппппннннннннннннннн лллабввввввввввввв абвжддд, абв Ввабввв kkk pppабв.')))
