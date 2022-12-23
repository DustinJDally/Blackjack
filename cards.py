class Card():
  def __init__(self, face, suit, value):
    self.face = face
    self.suit = suit
    self.value = value
  
  def printCard(self):
    suitIcon = {"club":"♣", "diamond":"♦", "heart":"♥", "spade":"♠"}
    # cardValue={"A":0, "J":10, "Q":10, "K":10, "face":"face"}
    print(f"{self.face}{suitIcon[self.suit]}{self.value}")

# card = Card("9", "diamond")

# card.printCard()

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


deck = Deck()
for card in deck.cards:
  card.printCard()