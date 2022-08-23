class bank_account:
    def __init__(self, interest_rate, acc_balance):
        self.interest = interest_rate
        self.balance = acc_balance
        self.personal_account = None

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Balance:" + "$" + str(self.balance))

    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance >= 1:
            print("Balance:" + "$" + str(self.balance))
        elif self.balance <=0:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")   
                

    def displayAccInfo(self):
        print("Balance:" + "$" + str(self.balance) + " " + "Interest Rate:" + str(self.interest))

    def yield_interests(self, percent):
        self.balance = self.balance * (1 + percent)
        print("Balance after Interests:" + "$" + str(self.balance))


class User:
    def __init__(self, user_name, user_age, user_email):
        self.name = user_name
        self.age = user_age
        self.email = user_email

    def user_deposit(self, amount):
        self.personal_account.deposit(amount)

    def user_withdraw(self, amount):
        self.personal_account.withdraw(amount)

    def display_user_info(self):
        self.personal_account.displayAccInfo()

    def user_interests_yield(self, percent):
        self.personal_account.yield_interests()           


savings_acc = bank_account(0.074, 100)
checkings_acc = bank_account(0.031, 640)

savings_acc.deposit(50)
savings_acc.deposit(15)
savings_acc.deposit(25)
savings_acc.withdraw(80) #change numbers to see $5 deducted
savings_acc.displayAccInfo()
savings_acc.yield_interests(savings_acc.interest)

checkings_acc.deposit(100)
checkings_acc.deposit(65)
checkings_acc.withdraw(80)
checkings_acc.withdraw(25)
checkings_acc.withdraw(30)
checkings_acc.withdraw(40)
checkings_acc.displayAccInfo()
checkings_acc.yield_interests(checkings_acc.interest)

Mr_Shelby = User("Thomas Shelby", 42, "tom_shelby@yahoo.com")
chase_bank = bank_account(0.032, 8000)
Mr_Shelby.personal_account = chase_bank

print(Mr_Shelby.name)
print(Mr_Shelby.personal_account.balance)
print(Mr_Shelby.personal_account.interest)

Mr_Shelby.personal_account.deposit(1000)
Mr_Shelby.personal_account.withdraw(500)
Mr_Shelby.personal_account.displayAccInfo()
Mr_Shelby.personal_account.yield_interests(Mr_Shelby.personal_account.interest)
