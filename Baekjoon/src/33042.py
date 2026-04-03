N = int(input())
cards = input().split()
cards_dict = dict()
is_not_answer = True

for card in range(len(cards)):
    cards_dict[cards[card]] = cards_dict.get(cards[card], 0) + 1
    if cards_dict[cards[card]] == 5:
        print(card+1)
        is_not_answer = False
        break

if is_not_answer:
    print(0)