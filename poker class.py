class Poker:
    def __init__(self, carts):
        self.np = __import__('numpy')
        self.specialFlagScore = {'j' : 11, 'q' : 12, 'k' : 13, 'a' : 14}
        self.cart_type = ['C','D','S','H']
        self.carts = carts
    
    def checkConsecutive(self, l):
        return (sum(self.np.diff(sorted(l)) == 1) >= len(l) - 1) 

    def weightCart(self, item) :
        flag = item[0:-1].lower()
        if flag in self.specialFlagScore.keys():
            return self.specialFlagScore.get(flag)
        
        return int(flag)

    def getWeightCards(self, arr):
        return [self.weightCart(item) for item in arr]

    def isTakCard(self, arr):
        firstFlagCard = arr[0][-1].lower()
        return all(firstFlagCard == item[-1].lower() for item in arr)

    def allFlagsfindCards(self, arr, characters):
        return all(self.findCard(arr, char) for char in characters)

    def findCard(self, arr, character):
        return any(character.lower() in item.lower() for item in arr)

    def checkNumOfKind(self, arr, num):
        WeightCards = self.getWeightCards(arr)
        return any(WeightCards.count(item) == num for item in WeightCards)

    def checkNumPair(self, arr, num):
        WeightCards = self.getWeightCards(arr)
        return [WeightCards.count(item) == 2 for item in WeightCards].count(True) == num

    def checkRoyalFlush(self, arr):
        return self.isTakCard(arr) and self.allFlagsfindCards(arr, ['A','K','Q','J','10'])

    def checkStraightFlush(self, arr):
        return self.isTakCard(arr) and self.checkConsecutive(self.getWeightCards(arr))
    
    def checkFourOfKind(self, arr):
        return self.checkNumOfKind(arr, 4)

    def checkThreeOfKind(self, arr):
        return self.checkNumOfKind(arr, 3)

    def checkTwoPair(self, arr):
        return self.checkNumPair(arr, 4)

    def checkFlush(self, arr):
        return self.isTakCard(arr)

    def checkStraight(self, arr):
        return self.checkConsecutive(self.getWeightCards(arr))

    def checkPair(self, arr):
        return self.checkNumPair(arr, 2)

    def isCartTypeValid(self, carts):
        return all(cart[-1] in self.cart_type for cart in carts)

    def isCartNumValid(self, carts):
        cartValues = [cart[0:-1] for cart in carts]
        for cartValue in cartValues:
            if(cartValue.lower() not in self.specialFlagScore.keys()):
                if(cartValue.isdigit()):
                    if(int(cartValue) < 1 and int(cartValue) > 10):
                        return False
                else:
                    return False
        return True

    def run(self):
        result = {}
        for item in self.carts:
            if(not self.isCartTypeValid(item)):
                raise Exception("type of cart not in cart_type")
            elif(not self.isCartNumValid(item)):
                raise Exception("cart between 1 and 10")
            elif(self.checkRoyalFlush(item)) :
                result[0] = item
            elif(self.checkStraightFlush(item)) :
                result[1] = item   
            elif(self.checkFourOfKind(item)) :
                result[2] = item
            elif(self.checkThreeOfKind(item) and self.checkTwoPair(item)) :
                result[3] = item
            elif(self.checkFlush(item)):
                result[4] = item
            elif(self.checkStraight(item)):
                result[5] = item
            elif(self.checkThreeOfKind(item)) :
                result[6] = item
            elif(self.checkTwoPair(item)) :
                result[7] = item
            elif(self.checkPair(item)) :
                result[8] = item
            else:
                result[9] = item

        SortUsers = sorted(result.keys())
        
        print(result[SortUsers[0]])


#####################
    #Club ♣️
    #Diamond ♦️
    #Spade ♠️
    #Heart ♥️
carts = [
    ['aH','aH','jD','jD','7H'],
    #  ['aH','aC','kD','jS','7H'],
    ['jH','jC','5D','5S','7H'],
    ['7H','7D','7C','QS','3H'],
    ['10H','9C','8D','7S','6H'],
    # # ['kC','10C','8C','7C','5C'],
    ['aH','aC','aD','3S','3H'],
    ['9H','9C','9D','9S', '3H'],
    # ['10S','jS','9S','8S','7S'],
    ['aD','kD','qD','jD','10D'],
]

poker = Poker(carts)
poker.run()
