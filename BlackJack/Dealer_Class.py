#dealer Class
import random
class Dealer:
    cards_in_deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']*4
    dealer_cards = []
    card_total = 0
    def __init__(self):
        pass
        #print("This is Dealer Class")

    def next_card(self):
        #print(New_Card.cards_in_deck)
        #print(len(Dealer.cards_in_deck))
        random_pop = random.randint(0, len(Dealer.cards_in_deck)-1)
        return Dealer.cards_in_deck.pop(random_pop)
        #print(Dealer.cards_in_deck)
    
    def dealt_cards_dealer(self, cards):
        Dealer.dealer_cards.append(cards)
        if cards in ['K', 'J', 'Q']:
            Dealer.card_total += 10
        elif cards == 'A':
            if (Dealer.card_total + 11) > 21:
                Dealer.card_total += 1
            elif (Dealer.card_total + 11) <= 21:
                Dealer.card_total += 11
        else:
            Dealer.card_total += int(cards)
        #print(f"Dealer cards are: {Dealer.dealer_cards[0]}")
    
    def dealer_reset(self):
        Dealer.dealer_cards = []
        Dealer.card_total = 0