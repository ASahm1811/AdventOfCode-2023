from main import lines

list_cards = [0]
sum_cards = 0

for l in lines:
    # print(l.strip().split(": ")[1].split(" | "))
    c_list = [c for c in l.strip().split(": ")[0].split(" ") if
              c]
    # print(c_list)

    card_list = []
    for x in range(int(c_list[1])):
        card_list.append(0)

    card_list.append(1)

    n = 0
    i = 0
    i_list = [i for i in l.strip().split(": ")[1].split(" | ")[0].split(" ") if
              i]
    j_list = [j for j in l.strip().split(": ")[1].split(" | ")[1].split(" ") if
              j]
    while i < len(i_list):
        j = 0
        while j < len(j_list):
            if i_list[i] == j_list[j]:
                n = n + 1
                card_list.append(1)
            j = j + 1
        i = i + 1
    list_cards.insert(int(c_list[1]), card_list)

print(list_cards)

for l in lines:
    # print(l.strip().split(": ")[1].split(" | "))
    c_list = [c for c in l.strip().split(": ")[0].split(" ") if
              c]
    # print(c_list)

    sum_cards = sum_cards + sum(list_cards[int(c_list[1])])

    x = int(c_list[1]) + 1
    while x < len(list_cards[int(c_list[1])]):
        if list_cards[int(c_list[1])][x] > 0:
            print(int(c_list[1]), list_cards[x])
            sum_cards = sum_cards + sum(list_cards[x])
        x = x + 1

print(sum_cards)


print("Sum: ", sum_cards)


