n = input("Please enter your text here: ").lower()

alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_count = {}

for i in n:
    if i in alphabet:
        if i in letter_count:
            letter_count[i] = letter_count[i] + 1
        else:
            letter_count[i] = 1

keys = letter_count.keys()

for i in sorted(keys):
    print(i, letter_count[i])
