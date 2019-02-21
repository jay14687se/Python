##Player Class

class Player():
    player_cards = []
    card_total = 0
    def __init__(self, balance=0):
        self.balance = balance
        print(self.balance)

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount            
            return True
        else:
            print(f"Insufficient balance!  Your balance is: {self.balance}")
            return False
    
    def dealt_cards_player(self, cards):
        Player.player_cards.append(cards)
        if cards in ['K', 'J', 'Q']:
            Player.card_total += 10
        elif cards == 'A':
            if (Player.card_total + 11) > 21:
                Player.card_total += 1
            elif (Player.card_total + 11) <= 21:
                Player.card_total += 11
        else:
            Player.card_total += int(cards)
        #print(f"Your cards are: {Player.player_cards} and your cards total is: {Player.card_total}")

    def player_reset(self):
        Player.player_cards = []
        Player.card_total = 0
