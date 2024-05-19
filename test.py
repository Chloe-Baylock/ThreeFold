class Player:
  def __init__(self, score, name):
    self.score = score
    self.name = name


chloe = Player(1, "chloe")
probie = Player(2, "probie")
natalie = Player(3, "natalie")

def highest(a, b):
  return b

high = highest(chloe, highest(probie, natalie))
print(high)
print(high.name)