class Session:

    def __init__(self):
        self.rates = self.get_rates()

    @staticmethod
    def get_rates():
        rates = dict()
        rates["USD"] = dict()
        rates["EUR"] = dict()
        rates["EUR"]["USD"] = 1.2
        rates["USD"]["EUR"] = 1 / 1.2
        return rates
