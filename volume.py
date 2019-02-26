import manian


class Volume:

    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other):
        assert isinstance(other, Volume)
        if other.currency == self.currency:
            rate = 1
        else:
            rate = manian.session.rates[other.currency][self.currency]
        return Volume(self.amount + other.amount * rate, self.currency)

    def __sub__(self, other):
        assert isinstance(other, Volume)
        if other.currency == self.currency:
            rate = 1
        else:
            rate = manian.session.rates[other.currency][self.currency]
        return Volume(self.amount - other.amount * rate, self.currency)

    def __mul__(self, other):
        assert isinstance(other, Volume)
        if other.currency == self.currency:
            rate = 1
        else:
            rate = manian.session.rates[other.currency][self.currency]
        return Volume(self.amount * other.amount * rate, self.currency)

    def __divmod__(self, other):
        assert isinstance(other, Volume)
        if other.currency == self.currency:
            rate = 1
        else:
            rate = manian.session.rates[other.currency][self.currency]
        return Volume(self.amount / other.amount * rate, self.currency)

    def __repr__(self):
        return "{} {}".format(self.amount, self.currency)

    def to(self, new_currency):
        if new_currency == self.currency:
            rate = 1
        else:
            rate = manian.session.rates[self.currency][new_currency]
        return Volume(self.amount * rate, new_currency)
