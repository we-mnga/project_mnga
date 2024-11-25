import time

class Transaction:
    def __init__(self, sender, recipient, amount):
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = time.time()

    def to_dict(self):
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp
        }
