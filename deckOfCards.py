import random

class Card():
  def __init__(self, face, suit, value):
    self.face = face
    self.suit = suit
    self.value = value

  def printCardAndValue(self):
    suitIcon = {"club":"♣", "diamond":"♦", "heart":"♥", "spade":"♠"}
    print(f"{self.face}{suitIcon[self.suit]} {self.value}")

  def printCardOnly(self):
    suitIcon = {"club":"♣", "diamond":"♦", "heart":"♥", "spade":"♠"}
    print(f"{self.face}{suitIcon[self.suit]}")
  # def dealCards(self):
  #   return card

class Deck():
  def __init__(self):
    self.cards = []
    faces = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")
    suits = ("club", "diamond", "heart", "spade")
    # values = ()
    for  face in faces:
      for suit in suits:
        if face == "K" or face == "Q" or face == "J":
          value = 10
        elif face == "A":
          value = 0
        else:
          value = face
        card = Card(face, suit, value)
        self.cards.append(card)

  def shuffle(self):
    random.shuffle(self.cards)

  def deal(self):
    card = self.cards.pop()
    return card

deck = Deck()
deck.shuffle()
# card = deck.deal()
# card.printCardAndValue()
# card.printCardOnly()
dealerHand = []
playerHand = []
for _ in range(2):
  card = deck.deal()
  dealerHand.append(card)
  card = deck.deal()
  playerHand.append(card)

print(dealerHand)
print(playerHand)