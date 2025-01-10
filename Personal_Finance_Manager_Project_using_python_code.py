from datetime import datetime

class User:
    def user_info(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email

        print("Name: ",self.name)
        print("AGE: ",self.age)
        print("Email: ",self.email)
        print("\n")



class Income:
    def income(self,amount):
        self.account_balance=0
        self.transaction=[]
        self.amount=amount
        self.account_balance=+amount
        self.transaction.append({"Type":"Income","Amount":amount,"Date":datetime.now().strftime("%Y-%M-%D")})
        print(f"Added {amount} to your account.")
        print(self.transaction)
        print("\n")

class Expense(Income):
    def expense(self,category,amount):
      if amount > self.account_balance:
            print("Insufficient Balance")
            return
      self.account_balance -=amount
      self.transaction.append({"Type":"Expanse","Category":category,"Amount":amount,"Date":datetime.now().strftime("%Y,%M,%D")})
      print(f"Expense of {amount} for category of {category}")
      print(f"Now current balance {self.account_balance}")
      print("\n")

class FixedExpense(Expense):
    def fixedexpense(self,house_rent,wifi_bill):
        self.house_rent=house_rent
        self.wifi_bill=wifi_bill
        self.account_balance=self.account_balance - (house_rent + wifi_bill)
        print(f"current balance: {self.account_balance}")
        print("\n")


class VariableExpense(FixedExpense):
    def variableexpense(self,utility_bill,transportation_cost):
        self.account_balance=self.account_balance - (utility_bill + transportation_cost)
        print(f"current balance: {self.account_balance}")
        print("\n")


obj=User()
obj.user_info("Belayet",23,"abc@gmail.com")



obj3=VariableExpense()
obj3.income(5000)
obj3.expense("food",1000)
obj3.fixedexpense(500,500)
obj3.variableexpense(500,500)