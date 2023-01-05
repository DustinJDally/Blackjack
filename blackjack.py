import random

# suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
suits = ('♣️', '♦️', '♥️', '♠️')
faces = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
values = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

playing = True

# Create the Cards class
class Card:

  def __init__(self, suit, face):
    self.suit = suit
    # self.suitSymbol = suitSymbol
    self.face = face

  def __str__(self):
    # suitSymbols = {'Clubs':'♣️', 'Diamonds':'♦️', 'Hearts':'♥️', 'Spades':'♠️'}
    return self.face + self.suit

# Create the Deck
class Deck:

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
class Bankroll:
  def __init__(self):
    self.deposit = 0
    self.chipTotal = 0
    self.bet = 0

  # Deposit money
  def depositMoney(self):
    self.chipTotal += self.deposit

  # loss = lose bet
  def placeBet(self):
    self.chipTotal -= self.bet

  # Win = bet = 1:1 (Bet * 1 == winnings)
  def winBet(self):
    self.chipTotal += (self.bet + self.bet)

  # Blackjack pays 3/2 (Bet * 1.5 == winnings)
  def winBlackjack(self):
    self.chipTotal += (self.bet + (self.bet * 1.5))

  # Push = get bet back
  def pushBet(self):
    self.chipTotal += self.bet


# Create a betting function
def placeBet(bankroll):

  while True:
    try:
      bankroll.bet = int(input('Place your bet: '))
    except ValueError:
      print('Please enter a number value for the bet')
    else: 
      if bankroll.bet > bankroll.total:
        print("You can't afford that bet, try again")
      else: 
        break

# Create Hit function  (can add a split function later if interested)
def hit(deck, hand):

  hand.dealCard(deck.deal()) 
  hand.isAce()

# Setup a hit or stand function
def playerAction(deck, hand):
  global playing

  while True: 
    action = input('Hit (H) or Stand (S)')
    if action[0].upper == 'H':
      hit(deck,hand)
    elif action[0].upper == 'S':
      print('Player stands, action to dealer')
    else:
      print('Invalid option, please enter H to hit or S to stand: ')
      continue
    break


# Create show cards functions (include during the game (only 1 dealer card visible) and after (all cards visible))

def showCardsInAction(player, dealer):
  print("\nThe Dealer's Hand is:\n")
  print('[X] ', dealer.cards[1], 'Value: ', dealer.value)
  print("The Player's Hand:\n", *player.cards, 'Value:', player.value, sep=' ')

def showCardsAfterAction(player, dealer):
  print("The Dealer's Hand:\n", *dealer.cards,'Value: ', dealer.value, sep=' ')
  print("The Player's Hand:\n", *player.cards,'Value: ', dealer.value, sep=' ')

# Create hand results and determine payout
def playerBusts(player, dealer, bankroll):
  print('Player busted! You lose, sorry')
  bankroll.loseBet()

def playerWins(player, dealer, bankroll):
  print('You beat the dealer! You win, congrats!')
  bankroll.winBet()

def playerBlackjacks(player, dealer, bankroll):
  print('YOU GOT BLACKJACK! GAME PAYS 3:2!')
  bankroll.winBlackjack()

def dealerBusts(player, dealer, bankroll):
  print('Dealer busted! You win, congrats')
  bankroll.winBet()

def dealerWins(player, dealer):
  print('The dealer beat you! You lose, sorry!')

def dealerBlackjacks(player, dealer):
  print('Dealer got a Blackjack, better luck next time')

def gamePushes(player, dealer, bankroll):
  print('You and the dealer tied! ')
  bankroll.pushBet()


# Create the game play

# Setup a loop that allows the following:
while True:
  print('Welcome to the Blackjack table!')

  #Setup and deck and prepare the deal
  deck = Deck()
  deck.shuffle()

  playerHand = Hand()
  playerHand.addCard(deck.deal())
  playerHand.addCard(deck.deal())

  dealerHand = Hand()
  dealerHand.addCard(deck.deal())
  dealerHand.addCard(deck.deal())

  # Ask Player to add money to bankroll
  playerBankroll = Bankroll()

    # Ask player if they want to play (If you build poker)
    # Ask Player how much they want to bet
  placeBet(playerBankroll)
  showCardsInAction(playerHand, dealerHand)

  while playing:

    #check if dealer or play have a Blackjack
    if playerHand.value == 21 and dealerHand.value == 21:
      gamePushes(playerHand, dealerHand, playerBankroll)
    elif dealerHand == 21:
      dealerBlackjacks(playerHand, dealerHand)
      break
    elif playerHand == 21:
      playerBlackjacks(playerHand, dealerHand, playerBankroll)
      break
    else:
      continue

    # Ask player to hit or stand
    playerAction(deck, playerHand)
    # Show the cards again
    showCardsInAction(playerHand, dealerHand)

    if playerHand.value > 21:
      playerBusts(playerHand, dealerHand, playerBankroll)
      break

  if playerHand.value <= 21:
    while dealerHand < 17:
      hit(deck,dealerHand)
    showCardsAfterAction(playerHand, dealerHand)
  
  if dealerHand > 21:
    dealerBusts(playerHand, dealerHand)
  elif dealerHand.value > playerHand.value:
    dealerWins(playerHand, dealerHand)
  elif dealerHand < playerHand.value:
    playerWins(playerHand, dealerHand, playerBankroll)
  else:
    gamePushes(playerHand, dealerHand, playerBankroll)

#Show new Bankroll:
print('\nYour current bankroll is: ' ,playerBankroll.chipTotal)
playAgain = input('Would you like to play again? Yes (Y) or No (N)')

if playAgain == 



# input('Hit (H) or Stand (S)')
#     if action[0].upper == 'H':
#       hit(deck,hand)
#     elif action[0].upper == 'S':
#       print('Player stands, action to dealer')
#     else:
#       print('Invalid option, please enter H to hit or S to stand: ')
#       continue
#     break
# TESTING

# testDeck = Deck()

# # print(testDeck)
# testDeck.shuffle()
# testPlayer = Hand()
# testPlayer.addCard(testDeck.deal())
# testPlayer.addCard(testDeck.deal())
# testPlayer.value

# for card in testPlayer.cards:
#   print(card)
# print (testPlayer.value)