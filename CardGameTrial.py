class Card:
    suitList = ["Clubs", "Diamonds", "Hearts", "Spades"]
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranklist[self.rank] + "of" + self.suitList[self.suit])


threeOfClubs = Card(3,1)
card1 = Card(1,11)
print (card1)
