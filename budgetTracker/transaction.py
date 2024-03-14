class Transaction:
    def __init__(self, name, category, amount, transaction_type, date) -> None:
        self.name = name
        self.category = category
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = date

    
    def __repr__(self):
        return f"<Transaction: {self.name}, {self.category}, ${self.amount:.2f}, {self.transaction_type}, {self.date}>"