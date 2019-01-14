text = input().upper()

def count1 (text):
    maximum = 0
    same = 0
    abc = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    for i in abc:
        counting = text.count(i)
        if maximum < counting:
            maximum = counting
            maxApha = i
        elif maximum == counting and maximum != 0 :
            same = counting
    if maximum == same:
        return '?'
    else:
        return maxApha

print(count1(text))
