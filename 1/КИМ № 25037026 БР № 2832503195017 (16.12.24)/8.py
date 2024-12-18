from itertools import product
a = product('012345678', repeat = 5)
c = 0
for i in a:
    word = ''.join(i)
    if word[0] != '0':
        if word.count('5') == 1:
            if word[0] != word[1]:
                if word[1] != word[2]:
                    if word [2] != word[3]:
                        if word[3] != word[4]:
                            c += 1
print(c)