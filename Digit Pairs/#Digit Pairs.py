#Digit Pairs

N = int(input())

num = list(map(str,input().split()))
num = num[:N]

bit = []

for items in num:
    digits = []
    for digit in items:
        digits.append(digit)
    digits.sort()
    bit_score = int(int(digits[0])*7 + int(digits[2])*11)
    bit_score = str(bit_score)
    if len(bit_score) == 3:
        bit_score = int(int(bit_score) % 100)
        bit.append(str(bit_score))
    else:
        bit.append(bit_score)

even_pos = []
odd_pos = []

pos = 1
for _ in bit:
    if pos%2 == 0:
        even_pos.append(_)
        pos += 1
    else:
        odd_pos.append(_)
        pos += 1

even_freq = {}
odd_freq = {}

for i in even_pos:
    if i[0] in even_freq:
        even_freq[i[0]] += 1
    else:
        even_freq[i[0]] = 1

for i in odd_pos:
    if i[0] in odd_freq:
        odd_freq[i[0]] += 1
    else:
        odd_freq[i[0]] = 1
pairs = 0
for key, value in even_freq.items():
    if value <=1:
        pass
    elif value == 2:
        pairs += 1
    else:
        pairs += 2

for key, value in odd_freq.items():
    if value <=1:
        pass
    elif value == 2:
        pairs += 1
    else:
        pairs += 2

print(pairs)
