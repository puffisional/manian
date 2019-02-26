from manian.transaction import Transaction


class Node:
    transactions = []
    balance = None
    currency = None

    def __init__(self, balance, currency):
        self.balance = balance
        self.currency = currency

    def buy(self, amount, quoted_currency):
        transaction = Transaction(amount, self.currency, quoted_currency)

    def sell(self, amount, quoted_currency):
        transaction = Transaction(amount, self.currency, quoted_currency)
