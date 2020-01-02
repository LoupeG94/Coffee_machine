char = input()
vowel = 'aeiouy'
consonant = 'qwrtplkjhgfdszxcvbnm'
for i in char:
    if i in vowel:
        print("vowel")
    elif i in consonant:
        print('consonant')
    else:
        break
