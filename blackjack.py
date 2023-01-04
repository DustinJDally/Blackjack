import random

# suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
suits = ('♣️', '♦️', '♥️', '♠️')
faces = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
values = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

playing = True

# Create the Cards class
class Card():

  def __init__(self, suit, face):
    self.suit = suit
    # self.suitSymbol = suitSymbol
    self.face = face
  
  def __str__(self):
    # suitSymbols = {'Clubs':'♣️', 'Diamonds':'♦️', 'Hearts':'♥️', 'Spades':'♠️'}
    return self.face + self.suit

# Create the Deck
class Deck():

  def __init__(self):
    self.deck = []
    for suit in suits:
      for face in faces:
        self.deck.append(Card(suit,face))
  
  def __str__(self):
    fullDeck = ''
    for card in self.deck:
      fullDeck += '\n ' +card.__str__()
    return 'The Deck has: ' + fullDeck

  # Shuffle and Deal functions
  def shuffle(self):
    random.shuffle(self.deck)

  def deal(self):
    dealtCard = self.deck.pop()
    return dealtCard

# Create the Hand Class
class Hand:
  def __init__(self):
    self.cards = []
    self.value = 0
    self.aces = 0

  def addCard(self, card):
    self.cards.append(card)
    self.value += values[card.face]
    if card.face == 'A':
      self.aces += 1

  def isAce(self):
    if self.value > 21 and self.aces:
      self.value -= 10
      self.aces -= 1

  # def __str__(self):
  #   if self.aces:
  #     return self.value - 10 + ' or ' + self.value
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


# TESTING

testDeck = Deck()

# print(testDeck)
testDeck.shuffle()
testPlayer = Hand()
testPlayer.addCard(testDeck.deal())
testPlayer.addCard(testDeck.deal())
testPlayer.value

for card in testPlayer.cards:
  print(card)
print (testPlayer.value)