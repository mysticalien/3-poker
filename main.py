def generate_combinations():
    suits = ['S', 'C', 'D', 'H']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    combinations = []

    for suit in suits:
        for rank in ranks:
            card = rank + suit
            combinations.append(card)

    return combinations


def check_combinations(cards, combinations, ranks):
    new_list = [item for item in combinations if item not in cards]
    set_cards = []
    pair = []
    highest = []

    for k in range(0, len(new_list)):
        if cards[0][0] == cards[1][0] == new_list[k][0]:
            set_cards.append(new_list[k])
        elif cards[0][0] == cards[1][0]:
            flag = 1
            for j in range(2, len(cards), 2):
                if cards[j][0] == cards[j + 1][0] == new_list[k][0]:
                    flag = 0
                if cards[j][0] == cards[j + 1][0] and (
                        ranks.index(cards[j][0]) > ranks.index(cards[0][0])):
                    flag = 0
                if cards[j][0] == new_list[k][0] and (
                        ranks.index(cards[j][0]) > ranks.index(cards[0][0])):
                    flag = 0
                if cards[j + 1][0] == new_list[k][0] and (
                        ranks.index(cards[j + 1][0]) > ranks.index(cards[0][0])):
                    flag = 0
            if flag == 1:
                pair.append(new_list[k])
        elif cards[0][0] == new_list[k][0] or cards[1][0] == new_list[k][0]:
            flag = 1
            for j in range(2, len(cards), 2):
                if cards[j][0] == cards[j + 1][0] == new_list[k][0]:
                    flag = 0
                if cards[j][0] == cards[j + 1][0] and (
                        ranks.index(cards[j][0]) > ranks.index(new_list[k][0])):
                    flag = 0
            if flag == 1:
                pair.append(new_list[k])
        else:
            new_flag = 1
            if ranks.index(new_list[k][0]) > ranks.index(cards[0][0]) and ranks.index(new_list[k][0]) > ranks.index(cards[1][0]):
                highest_index = ranks.index(new_list[k][0])
            elif ranks.index(cards[0][0]) > ranks.index(cards[1][0]):
                highest_index = ranks.index(cards[0][0])
            else:
                highest_index = ranks.index(cards[1][0])
            for j in range(2, len(cards)):
                if ranks.index(cards[j][0]) > highest_index:
                    new_flag = 0
            if new_flag == 1:
                red_flag = 0
                for j in range(2, len(cards), 2):
                    if cards[j][0] == new_list[k][0] or cards[j][0] == cards[j + 1][0] or cards[j + 1][0] == new_list[k][0]:
                        red_flag = 1
                if red_flag == 0:
                    highest.append(new_list[k])

    return set_cards, pair, highest

def sorting(obj):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    sorted_cards = []
    for i in range(0, len(ranks)):
        for card in obj:
            if str(card[0]) == ranks[i]:
                sorted_cards.append(card)
    print(len(sorted_cards))
    for i in range(0, len(sorted_cards)):
        print(sorted_cards[i])


combinations = generate_combinations()
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

t = int(input())
for _ in range(t):
    n = int(input())

    cards = []

    for _ in range(n):
        rank, suit = input().split()  # Split rank and suit
        cards.append(rank)
        cards.append(suit)

    set_cards, pair, highest = check_combinations(cards, combinations, ranks)

    result = list(set(set_cards) | set(pair) | set(highest))

    if not result:
        print(0)
    else:
        sorting(result)

