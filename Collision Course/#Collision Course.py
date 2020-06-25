#Collision Course
import math

C = int(input())
data = []
for i in range(C):
    x, y, v = map(int,input().split())
    d = math.sqrt(math.pow(x,2) + math.pow(y,2))
    t = d/v
    data.append(t)


all_freq = {} 

for i in data: 
	if i in all_freq: 
		all_freq[i] += 1
	else: 
		all_freq[i] = 1

Collision = 0

for key, value in all_freq.items():
    if value >= 2:
        Collision += int(math.factorial(value)/(math.factorial(2)*math.factorial(value -2)))

print(Collision)