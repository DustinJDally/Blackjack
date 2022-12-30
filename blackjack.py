import random

# Create the Cards


# Create the Deck

  # Shuffle and Deal functions


# Create the Hand Class

  # Setup dealing 2 cards to dealer and player, assigning a value to the cards (A is 1 or 11)


# Create the bankroll class


# Create a betting function 

  # loss = lose bet
  # Push = keep bet
  # Win = bet = 1:1 (Bet * 1 == winnings)
  # Blackjack pays 3/2 (Bet * 1.5 == winnings)


# Create Hit function  (can add a split function later if interested)


# Setup a hit or stand function 


# Create show cards functions (include during the game (only 1 dealer card visible) and after (all cards visible))


# Create hand results and calculate winnings or losses



# Create the game play

  # Setup a loop that allows the following:
    # Ask Player to add money to bankroll
    # Ask player if they want to play (If you build poker you can select that here too)
    # Ask Player how much they want to bet
    # DEAL CARDS
    # SHOW CARDS (check if dealer or play have a Blackjack)
    #   If dealer GAME ENDS if Player they win 1.5x bet
    # If not Blackjack ask player if they want to hit or stand
    #   Check to make sure the player doesn't go over 21
    # Check if dealer is over 16 (Dealer stands at 17+)
    # Dealer hit or stand
    #   Check to make sure dealer doesn't go over 21
    # Determine winner
    # Ask if player wantes to play again (exit on NO)