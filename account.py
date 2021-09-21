"""
account.py

Creates the account class with its accompanying functions
"""

class Account(starting_balance):
    def __init__(self):
        self.balance = starting_balance
    
    def withraw(self, amt):
        self.balance -= amt

    def deposit(self, amt):
        self.balance += amt
        

    
