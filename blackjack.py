import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,10]
    card = random.choice(cards)
    return card

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 22:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😏"
    else:
        return "You lose 😭"

def play_game():
    user_cards = []
    computer_cards = []
    user_score = -1
    comp_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calc_score(user_cards)
        comp_score = calc_score(computer_cards)
        print(f"your cards : {user_cards} and your score is : {user_score}")
        print(f"computers 1st card : {computer_cards[0]}")
        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y" :
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calc_score(computer_cards)

    print(f"your final hand : {user_cards} and score is : {user_score}")
    print(f"computers final hand : {computer_cards} and their score is : {comp_score}")
    print(compare(user_score, comp_score))

while input("do you want to play game of blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    print("new game started")
    play_game()