import random

def check_face_cards(card):
    '''Take in the card to check if it's a face card,
    and return the appropriate blackjack value'''
    if card == 11:
        card = 'J'
    elif card == 12:
        card = 'Q'
    elif card == 13:
        card = 'K'
    elif card == '1':
        card = 'A'
    return card
        

def deal(deck):
    '''Deal a card from shuffled deck, returns hand'''
    hand = []
    for _ in range(2):
        random.shuffle(deck)
        card = deck.pop()
        card = check_face_cards(card)
        hand.append(card)
    return(hand)

def total(hand):
    '''Takes in the list containing hands,
    returns the total after computing it'''
    total = 0
    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
            total += 10
        elif card == 'A':
            if total >= 11: total += 1
            else: total += 11
        else:
            total += card
    return total

def hit(hand, deck):
    '''Pop the deck and deal the card to the needed hand,
    return the hand by reference'''
    card = deck.pop()
    card = check_face_cards(card)
    hand.append(card)
    return hand

def blackjack(player_hand, dealer_hand):
    '''Check if the total is 21,
    and assign winner as needed'''
    if total(player_hand) == 21:
        print('Blackjack! You win')
        return 1
    elif total(dealer_hand) == 21:
        print('Dealer Blackjack. You lose')
        return -1
    else:
        return 0

def score(dealer_hand, player_hand):
    '''Compare total of both the hands, and decide winner'''
    player_total = total(player_hand)
    dealer_total = total(dealer_hand)

    print('Player hand, Dealer hand', player_hand, dealer_hand)
    if player_total == 21:
        print ("Congratulations! You got a Blackjack!")
        return 1
    elif dealer_total == 21:		
        print ("Sorry, you lose. The dealer got a blackjack.")
        return -1
    elif player_total > 21:
        print ("Sorry. You busted. You lose.")
        return -1
    elif dealer_total > 21:
        print ("Dealer busts. You win!")
        return 1
    elif player_total < dealer_total:
        print ("Sorry. Your score isn't higher than the dealer. You lose.")
        return -1
    elif player_total > dealer_total:			   
        print ("Congratulations. Your score is higher than the dealer. You win")
        return 1
    else:
        print('It\'s a draw, both hands equal')
        return 0


def game(target):
    print('Game begins\n')
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
    quit = 0
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print('Player, dealer', player_hand, dealer_hand) #for debugging
    
    quit = blackjack(player_hand, dealer_hand)
    while quit == 0:
        if total(player_hand) < target: # hit till a target
            print('Player hit')
            hit(player_hand, deck)
            print('Player hand', player_hand)
            if total(player_hand) > 21:
                print('Bust, you lost')
                return -1
        else: # stay, so the dealer will hit themselves now
            print('Player stays now')
            while total(dealer_hand) < 17:
                print('Dealer hit')
                hit(dealer_hand, deck)
                print('Dealer hand', dealer_hand)
                if total(dealer_hand) > 21:
                    print('Dealer bust, you win')
                    return 1
            return score(dealer_hand, player_hand)
    return quit
            
#value = game(16)
#print(value)
