def card_score(cards):
    sum = 0
    for card in cards:
        if card == 'A': sum += 4
        elif card == 'K': sum += 3
        elif card == 'Q': sum += 2
        elif card == 'J': sum += 1
    return sum
    
N = int(input())
all_sum = 0

for i in range(N):
    cards = input()
    all_sum += card_score(cards)

print(all_sum)