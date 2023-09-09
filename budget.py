import math

class Category:
    ledger = []
    balance = 0
    #Class constructor defines the object category
    def __init__(self, category):
        self.category = category

    #check_funds method will return false if the amount is less than the balance and true if the amount is greater than the balance
    def check_funds(self, amount):
        if self.balance < amount:
            return False
        return True

    #deposit method will add to the ledger and increase the balance
    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": float(amount), "description": description})
        self.balance += amount

    #withdraw method will add to the ledger and decrease the balance if sufficient funds are available
    def withdraw(self, amount, description = ""):
        if not self.check_funds(amount):
            return False
        self.ledger.append({"amount": float(-1 * amount), "description": description})
        self.balance -= amount
        return True
    
    #get_balance method returns the current balance
    def get_balance(self):
        return self.balance
    
    #transfer method will update the ledger and transfer funds to a different category if sufficient funds are available
    def transfer(self, amount, destination):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, "Transfer to " + destination.category)
        destination.deposit(amount, "Transfer from " + self.category)
        return True
    
    #Format the string that will be returned the when the object is printed
    def __str__(self):
        returnStr = ""
        line = ""

        #Format the header
        for i in range(math.floor((30 - len(self.category)) / 2)):
            line += "*"
        line += self.category
        while len(line) < 30:
            line += "*"
        returnStr += line
        returnStr += "\n"
        line = ""

        
        #Add the ledger items
        for i in self.ledger:
            if len(i["description"]) > 23:
                line += i["description"][:23]
            else:
                line += i["description"]
                while(len(line) < 23):
                    line += " "

            currAmount = format(i['amount'], ".2f")
            for i in range(7 - len(currAmount)):
                line += " "
            line += currAmount
            
            returnStr = returnStr + line + "\n"
            line = ""

        returnStr += "Total: " + str(self.balance)

        
        return returnStr

        
def create_spend_chart(categories):
    pass

clothing = Category("Clothing")
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(25, "groceries")
food.withdraw(50, "restaurant and more food")
clothing.deposit(75, "test deposit")
print(food.balance)

'''
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)
'''