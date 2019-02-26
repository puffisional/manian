import manian


class Transaction:
    base_currency = None
    quoted_currency = None

    def __init__(self, amount, base_currency, quoted_currency):
        self.amount = amount
        self.base_currency = base_currency
        self.quoted_currency = quoted_currency

    def output(self):
        return manian.session.exchange(self.amount, self.base_currency, self.quoted_currency)
