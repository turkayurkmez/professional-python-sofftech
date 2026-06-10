class NegativeAmountException(Exception):
    """Amount değeri negatif olamaz!!"""

    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Geçersiz miktar: {amount}. Miktar negatif olamaz.")