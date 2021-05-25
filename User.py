class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    
    def transfer_money(self, other_user, amount):
        # BONUS
        # let's leverage the fact that we have deposit and withdrawal methods that are available to self and other_user
        # since they're both User objects...You don't have to do it this way though
        other_user.make_deposit(amount) # could also say other_user.account_balance += amount
        self.make_withdrawal(amount) # could also say self.account_balance -= amount


tim = User("Tim", "tim@jake.com")
jake = User("Jake", "jake@jake.com")
me = User("Me", "me@me.com")

tim.make_deposit(100)
tim.make_deposit(100)
tim.make_deposit(100)
tim.make_withdrawal(50)
tim.display_user_balance()

jake.make_deposit(50)
jake.make_deposit(1000)
jake.make_withdrawal(500)
jake.make_withdrawal(100)
jake.display_user_balance()

me.make_deposit(100)
me.make_withdrawal(25)
me.make_withdrawal(25)
me.make_withdrawal(25)
me.display_user_balance()

# BONUS
tim.transfer_money(jake,250)
tim.display_user_balance()
jake.display_user_balance()