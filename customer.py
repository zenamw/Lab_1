"""
customer.py

Creates the customer class
"""

class Customer(first_name, last_name, age, sex):
    def __init__(self):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = '{fn} {ln}'.format(fn = first_name,
                                            ln = last_name)
        self.unqualified_for_loan = self.qualify_for_loan(age)
        self.accounts = list()

    def qualify_for_loan(age):
        if age < 18:
            qualifies = False
        else:
            qualifies = True
        
        return qualifies

    def add_account(self, account):
        self.accounts.append(account)

            
