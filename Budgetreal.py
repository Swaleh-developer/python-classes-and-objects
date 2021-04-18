class Budget:

  #Instantiating the objects 
  def __init__(self, budget):
    self.ledger_book = []
    self.amount = 0
    self.budget = budget

 #Checking available funds
  def check_available_funds (self, amount):
      if self.amount < amount:
        return False
      else:
          return True
    
       
  #Deposit method
  def deposit(self, amount, description = ""):
    self.ledger_book.append({"amount" : amount, "description" : description})
    self.amount += amount

  #Withdraw method
  def withdraw(self, amount, description = ""):
    if self.check_available_funds(amount) == True:
      self.amount -= amount
      self.ledger_book.append({"amount":-amount,"description":description})  
      return True
    else:
      return False

  #Check balances
  def get_balance(self):
    return self.amount

  #Transfer method
  def transfer(self, amount, budget):
    if self.check_available_funds(amount) == True:
       self.amount -= amount
       self.ledger_book.append({"amount": -amount,"description": "Transfer to "+ budget.budget})
       budget.ledger_book.append({"amount": amount,"description": "Transfer from "+ self.budget}) 
       return True
    else:
       return False

#Instances of a class (objects)      
Food = Budget("amount")
Clothing = Budget("amount")
Entertainment = Budget("amount")