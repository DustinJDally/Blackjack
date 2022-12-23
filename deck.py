# clubs (♣), diamonds (♦), hearts (♥) and spades (♠)

class Card():
  def __init__(self, face, suit, value):
    self.face = face
    self.suit = suit
    self.value = value

  def printCard(self):
    suitIcon = {"club":"♣", "diamond":"♦", "heart":"♥", "spade":"♠"}
    print(f"{self.face}{suitIcon[self.suit]} value = {self.value}")

card = Card("K", "diamond", 10)

card.printCard()