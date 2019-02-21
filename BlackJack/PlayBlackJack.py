# Game script
import Player_Class
import Dealer_Class

print("Welcome to BlackJack!")

while True:
    try:
        player_account_balance = int(input("What is the amount for which you need the chips: "))
    except ValueError:
        print("Please enter a valid amount")
        continue
    else:
        print("Here are your chips!")
        break

player = Player_Class.Player(player_account_balance)
dealer = Dealer_Class.Dealer()

while True:

    print("Please place your Bet!")

    while True:
        try:
            bet_amount = int(input("How much would you like to bet: "))
        except ValueError:
            print("Please enter a valid amount")
            continue
        else:
            if not player.withdraw(bet_amount):
                if_add_money = input("Would you like to add more money, Yes or No: ")
                if if_add_money.lower() == "yes":
                    amount_added = int(input("How much do you like to add: "))
                    player.deposit(amount_added)
                continue
            else:
                print("Bet Placed!")
                break

    player.dealt_cards_player(dealer.next_card())
    player.dealt_cards_player(dealer.next_card())
    print(
        f"Your cards are: {player.player_cards} and your cards total is: {player.card_total}")
    dealer.dealt_cards_dealer(dealer.next_card())
    dealer.dealt_cards_dealer(dealer.next_card())
    print(
        f"Dealer cards are: {dealer.dealer_cards[0]}. The other card is Hidden")
    blackjack = False
    decision = False
    if player.card_total == 21:
        blackjack = True
        print("Blackjack!!!. Player Wins")
        player.deposit(bet_amount + (bet_amount * 1.5))
        print(f"Player account balance is {player.balance}")
        
    while not blackjack:
        player_choice = input("Do you want to Hit or Stay: ")
        if player_choice.lower() == "hit":
            player.dealt_cards_player(dealer.next_card())
            print(
                f"Your cards are: {player.player_cards} and your cards total is: {player.card_total}")
            if player.card_total > 21:
                print("Players Busts!!")
                print(f"Player account balance is {player.balance}")
                blackjack = True
        else:
            print(
                f"Dealer cards are: {dealer.dealer_cards} and dealer cards total is: {dealer.card_total}")
            while not 17 <= dealer.card_total <= 21:
                dealer.dealt_cards_dealer(dealer.next_card())
                print(
                    f"Dealer cards are: {dealer.dealer_cards} and dealer cards total is: {dealer.card_total}")
                if dealer.card_total > 21:
                    print("Dealer Busts!!")
                    print("Player Wins!!")
                    player.deposit(bet_amount*2)
                    print(f"Player account balance is {player.balance}")
                    blackjack = True
                    break
            if blackjack == True:
                decision = False
            else:
                decision = True
                blackjack = True

    if decision == True:
        if player.card_total > dealer.card_total:
            player.deposit(bet_amount*2)
            print("Player Wins!!!")
        elif player.card_total == dealer.card_total:
            player.deposit(bet_amount)
            print("No one Wins!!")
        else:
            print("Player Loses!!!")
        print(f"Player account balance is {player.balance}")

    continue_play = input("Do you want ot play again: Yes or No: ")
    if continue_play.lower() == "yes":
        player.player_reset()
        dealer.dealer_reset()
        continue
    else:
        break
