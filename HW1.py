import random

#We first define the general attributes of items in a general class
class item(object):  
    def __init__(self, buyPrice, name):
        self.buyPrice = buyPrice
        self.name = name
#using inheritance we define a subclass for stock    
class Stock(item): 
    def __init__(self, buyPrice, name):
        item.__init__(self, buyPrice, name)
    def className(self): return "stock" 
    def SellPrice(self):
        return round(random.uniform(.5*self.buyPrice, 1.5*self.buyPrice),2)
    
#using inheritance we define a subclass for stock
class MutualFund(item):
    def __init__(self, name):
        item.__init__(self, 1, name)
    def className(self): return "mutual funds"
    def SellPrice(self):
        return round(random.uniform(.9, 1.2),2)
    
# we can add more items to the portfolio using inheritance(bonus question)

#*****************************************************************************************   
# now its the time for defining Portfolio class
class Portfolio(object):
    def __init__(self):
        self.cash = 0.0
        self.items = {"stock" : {}, "mutual funds" : {}} 
        self.transactions = ["No transactions yet---->"]

    def addCash(self, cashAmount):
        self.cash = (self.cash) + (cashAmount)
        self.transactions.append("Added %.2f$---->"%(cashAmount))

    def withdrawCash(self, cashAmount):
        if cashAmount > self.cash: print("insufficient cash ;Impossible to withdraw")
        else:
            self.cash = (self.cash)-(cashAmount)
            self.transactions.append("Withdrew %.2f$---->"%(cashAmount)) 

    def buyItem(self, quantity, itemName):
        if self.cash < quantity*itemName.buyPrice:
            print("Insufficient cash; Impossible to buy.")
            return None

        if itemName in self.items[itemName.className()]:
            self.items[itemName.className()][itemName]=self.items[itemName.className()][itemName]+ quantity 
        else:
            self.items[itemName.className()][itemName] =  0 + quantity
        self.transactions.append("Bought %.2f of %s %s---->" % (quantity, itemName.name, itemName.className())) 
        self.withdrawCash(quantity*itemName.buyPrice)
    def buyStock(self, quantity, itemName): #buy in whole units
        self.buyItem(round(quantity,0), itemName) 

    def buyMutualFund(self, quantity, itemName):
        self.buyItem(round(quantity,2), itemName)

    def sellItem(self, quantity, itemName):
        if itemName in self.items[itemName.className()]: #check existence in the portfolio
            if self.items[itemName.className()][itemName] < quantity: #check current ballance of the item
                print("Insufficient amount of %s %s---->" %(itemName.name, itemName.className()))
            else:
                self.items[itemName.className()][itemName]=self.items[itemName.className()][itemName] - quantity
                if self.items[itemName.className()][itemName] == 0: #remove dictionary key if balance is zero for an item
                    del self.items[itemName.className()][itemName]
                self.transactions.append("Sold %.2f of %s named %s---->" % (quantity, itemName.className(), itemName.name))
        else: print("The portfolio does not contain %s with name %s---->" %(itemName.className(), itemName.name))
        self.addCash(quantity*itemName.SellPrice()) 
    def sellStock(self, quantity, item): 
        self.sellItem(round(quantity,0), item) #sell in whole units
    def sellMutualFund(self, quantity, item):
        self.sellItem(quantity, item)
 

    def __str__(self):
        representation = "\n\ncash: $%-2.2f\n" %self.cash
        for itemName in self.items:
            representation+= "  %s: \n"%itemName
            if not self.items[itemName]: output+='\tnone\n'
            for i in self.items[itemName]:
                representation += str(i.name)+"   "+ str(f'{self.items[itemName][i]:9.2f}')+ "\n"
        return representation

    def history(self): 
        print(self.transactions)