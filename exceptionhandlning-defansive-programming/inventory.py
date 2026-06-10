from custom_exception import NegativeAmountException
class Inventory:
    def update_stock(self, amount:int):
        if amount < 0:
            raise NegativeAmountException(amount)
        self.amount = amount
        return self.amount
