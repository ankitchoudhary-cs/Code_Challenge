#Swayamvar

N = int(input())
brides_to_be = input()
grooms_to_be = input()

unmatched_pairs = N
pairs = N

brides_to_be_list = []
grooms_to_be_list = []

for drinks in brides_to_be:
    brides_to_be_list.append(drinks)

for drinks in grooms_to_be:
    grooms_to_be_list.append(drinks)

for b_items in range(N):
    for g_items in grooms_to_be_list:
        if brides_to_be_list[b_items] == g_items:
            unmatched_pairs -= 1
            grooms_to_be_list.remove(g_items)
            break
    if unmatched_pairs == pairs:
        break
    else:
        pairs -= 1

print(unmatched_pairs)