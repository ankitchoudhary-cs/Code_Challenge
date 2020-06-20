#Philaland Coin
import math

T = int(input("Enter the no. of cases: "))
output = []

for i in range(T):
    N = int(input("Enter the maximum price of the item present on Philaland: "))

    coin = 0

    while math.pow(coin,2) <= N:
        coin += 1
    output.append(coin)
for item in output:
    print(item)
