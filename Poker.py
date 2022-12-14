import random
import copy

#Arun Sabaratnam 300297854
#Bob Yang 300288751

class Player:
  def __init__(self):
    self.hand = []
    
  def print(self):
    print(self.hand)
  
class PokerGame(Player):
  def __init__(self, deck, players, n = 2):
    self.playersnum = n
    self.players = players
    self.tablecards = []
    self.deck = deck
    
  def print(self):
    print(self.playersnum)
    print(self.tablecards)
    
    for i in self.players:
      print(i.hand)
      
    print(self.deck)
  
  def add_card(self,index):
    self.players[index].hand.append(self.deck[0])
    self.deck.pop(0)
     
  def add_to_table(self):
    self.tablecards.append(self.deck[0])
    self.deck.pop(0)
    
  def isStraightFlush(self,values, cards):    
    if PokerGame.isStraight(self,values,cards) == True and PokerGame.isFlush(self,cards) == True:
      return True 
    
    return False 
    
  def isFourOfAKind(self, cards):
    firstvalues = [x[0] for x in cards]
    copyoffirstvalues = copy.deepcopy(firstvalues)
    
    firstvalues = list(set(firstvalues))
    
    if len(firstvalues) != 2:
      return False 
    
    for i in firstvalues:
      if copyoffirstvalues.count(i) == 4:
        return True 
    
    return False 

  def isFullHouse(self,cards):
    firstvalues = [x[0] for x in cards]
    copyoffirstvalues = copy.deepcopy(firstvalues)
    
    firstvalues = list(set(firstvalues))
        
    if len(firstvalues) != 2:
      return False 
    
    if copyoffirstvalues.count(firstvalues[0]) == 3 and copyoffirstvalues.count(firstvalues[1]) == 2 or copyoffirstvalues.count(firstvalues[0]) == 2 and copyoffirstvalues.count(firstvalues[1]) == 3:
      return True 
    
    return False 
      
  def isFlush(self,cards):
    secondvalues = [x[1] for x in cards]
    
    if secondvalues.count(secondvalues[0]) != len(secondvalues):
      return False 
    
    return True    
      
  def isStraight(self,values, cards):
    firstvalues = [x[0] for x in cards]
    valuesofhand = []
    
    for i in firstvalues:
      valuesofhand.append(values[i])
      valuesofhand = sorted(valuesofhand)
      
    if 13 in valuesofhand:
        for i in range(len(valuesofhand)):
            if valuesofhand[i] == 1:
                valuesofhand[i] = 14
                valuesofhand = sorted(valuesofhand)
              
    for i in range(len(valuesofhand)):
      try:
        if valuesofhand[i+1] - valuesofhand[i] != 1:
          return False
        
      except:
        break
        
    return True 
  
  def isThreeOfAKind(self,cards):
    firstvalues = [x[0] for x in cards]
    copyoffirstvalues = copy.deepcopy(firstvalues)
    
    firstvalues = list(set(firstvalues))
    
    for i in firstvalues:
      if copyoffirstvalues.count(i) == 3:
        return True 
    
    return False   
  
  def isTwoPairs(self, cards):
    firstvalues = [x[0] for x in cards]
    copyoffirstvalues = copy.deepcopy(firstvalues)
    
    firstvalues = list(set(firstvalues))
    
    if len(firstvalues) != 3:
      return False 
    
    paircheck = []
    for i in range(len(firstvalues)):
      paircheck.append(copyoffirstvalues.count(firstvalues[i]))
      paircheck = sorted(paircheck)
      
    
    if paircheck == [1,2,2]:
      return True
    return False 
       
  def isOnePair(self,cards):
    firstvalues = [x[0] for x in cards]
    copyoffirstvalues = copy.deepcopy(firstvalues)
    
    firstvalues = list(set(firstvalues))
    
    paircheck = []
    for i in range(len(firstvalues)):
      paircheck.append(copyoffirstvalues.count(firstvalues[i]))
      paircheck = sorted(paircheck)
       
    if 2 in paircheck:
      return True
    return False 
  
  def combinations(self, cards):
    #answer list to store all possible combinations
    ans = []
    #make a copy of the cards to make sure they are not being alterred in the recursion
    cards2 = cards.copy()

    def possibleCombo(s, c):
      #if the length of the combination is 5 append to answer
      if len(c) == 5:
        ans.append(c.copy())
        return
      
      for i in range(len(cards2)):
        #making sure there are no duplicate cards
        if c.count(cards2[i]) > 0:
          continue
        #generating all possible combinations of cards
        c.append(cards2[i])
        possibleCombo(i+1, c)
        c.pop()
     
    #0 is the starting position (index 0) of the array
    possibleCombo(0, [])
    return ans

class TexasHoldem(PokerGame):
    def __init__(self, deck, players, n = 2):
      super().__init__(deck, players, n)
      self.best = []
    
    def deal(self):
      for i in range(len(self.players)):
        for j in range(2):
          PokerGame.add_card(self,i)
      
      for i in range(5):
        PokerGame.add_to_table(self)
      
    def hands(self, values):
      for i in range(len(self.players)):
        Tcards = []
        bests = []

        for j in range(len(self.players[i].hand)):
          Tcards.append(self.players[i].hand[j])
        
        for k in range(len(self.tablecards)):
          Tcards.append(self.tablecards[k])
        
        combos = PokerGame.combinations(self, Tcards)

        for i in range(len(combos)):
          if PokerGame.isStraightFlush(self, values, combos[i]):
            bests.append("Straight Flush")
          elif PokerGame.isFourOfAKind(self,combos[i]):
            bests.append("Four of a kind")
          elif PokerGame.isFullHouse(self, combos[i]):
            bests.append("Full house")
          elif PokerGame.isFlush(self, combos[i]):
            bests.append("Flush")
          elif PokerGame.isStraight(self, values, combos[i]):
            bests.append("Straight")
          elif PokerGame.isThreeOfAKind(self, combos[i]):
            bests.append("Three of a kind")
          elif PokerGame.isTwoPairs(self, combos[i]):
            bests.append("Two pairs")
          elif PokerGame.isOnePair(self, combos[i]):
            bests.append("One pair")
          else:
            bests.append("High card")
                 
        if bests.count("Straight Flush")>0:
          self.best.append("Straight Flush")
        elif bests.count("Four of a kind")>0:
          self.best.append("Four of a kind")
        elif bests.count("Full house")>0:
          self.best.append("Full house")
        elif bests.count("Flush")>0:
          self.best.append("Flush")
        elif bests.count("Straight")>0:
          self.best.append("Straight")
        elif bests.count("Three of a kind")>0:
          self.best.append("Three of a kind")
        elif bests.count("Two pairs")>0:
          self.best.append("Two pairs")
        elif bests.count("One pair")>0:
          self.best.append("One pair")
        elif bests.count("High card")>0:
          self.best.append("High card")
        
      return self.best
        
#test cases
deck = []
cards = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']

values = {}

for i in range(1, len(cards) + 1):
  values[cards[i-1]] = i

suit = ['D','C','S','H']  

n = int(input('Please input the amount of players that are playing the game\n'))
players = [Player() for i in range(n)]

for i in cards:
  for j in suit:
    temp = ''
    temp = temp + i + j 
    deck.append(temp)
    
random.shuffle(deck)

game = PokerGame(deck,players,n)

T = TexasHoldem(deck,players,n)

T.deal()

for i in range(len(T.players)):
  print("Player", i+1, "hand: ", end='')
  T.players[i].print()

print("Table cards: ", T.tablecards)

print(T.hands(values))
