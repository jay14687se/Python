import Dealer_Class
carddeck = Dealer_Class.Dealer()
carddeck.next_card()
carddeck.next_card()
carddeck.next_card()
carddeck.next_card()

else:
            print(f"Dealer cards are: {dealer.dealer_cards[0]}. The other card is Hidden")
            while 17 <= dealer.card_total <= 21:
                dealer.dealt_cards_dealer(dealer.next_card())
            break

