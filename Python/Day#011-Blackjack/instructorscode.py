""" Blackjack
    Coded by TechGYQ
    www.mythosworks.com
    OC:2022.05.24-1738 """

from random import choice as pick
game_over = False


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = pick(cards)
    return card


def get_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def game_check(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw"

    elif dealer_score == 0:
        return "House has blackjack!"

    elif player_score == 0:
        return f"{user} has blackjack!"

    elif player_score > 21:
        return f"{user} busts!"

    elif dealer_score > 21:
        return "House loses!"

    elif player_score > dealer_score:
        return f"{user} wins!"

    else:
        return "House wins!"


user = input("What's your name stranger? ")
player_cards = []
dealer_cards = []

for i in range(2):
    player_cards.append(deal_card())
    dealer_cards.append(deal_card())

while not game_over:
    player_score = get_score(player_cards)
    dealer_score = get_score(dealer_cards)
    print(f"{user}'s cards: {player_cards}, Totaling: {player_score}")
    print(f"House is showing a {dealer_cards[0]}")

    if player_score == 0 or dealer_score == 0 or player_score > 21:
        game_over = True

    else:
        hit = input("Would you like another card? ")
        if hit.startswith("y"):
            player_cards.append(deal_card())

        else:
            game_over = True

while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(deal_card())
    dealer_score = get_score(dealer_cards)

print(game_check(player_score, dealer_score))