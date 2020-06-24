#Prime Fibonnaci

from itertools import permutations
import math

primelist1st = []
primelist2nd = []
combination = []

n1, n2 = map(int,input().split())

for num in range(n1, n2 + 1):
    #prime number is greater than 1
    if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
            primelist1st.append(num)

comb = permutations(primelist1st,2)
for i in list(comb):
    n = int(''.join(str(j) for j in i))
    combination.append(n)

for num in combination:
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            primelist2nd.append(num)

primelist2nd = list(dict.fromkeys(primelist2nd))

smallest = min(primelist2nd)
largest = max(primelist2nd)

n1 = smallest
n2 = largest
nth = 0
n = len(primelist2nd)

for i in range(n - 1):
    nth = n1 + n2
    n1 = n2
    n2 = nth

print(n1)