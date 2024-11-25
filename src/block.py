import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, transactions, proof, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.proof = proof
        self.timestamp = timestamp or time.time()

    def compute_hash(self):
        """
        Computes the SHA-256 hash of the block's contents.
        """
        block_content = f"{self.index}{self.previous_hash}{self.transactions}{self.proof}{self.timestamp}"
        return hashlib.sha256(block_content.encode()).hexdigest()

    def to_dict(self):
        """
        Serialize the block into a dictionary for easy storage or transmission.
        """
        return {
            'index': self.index,
            'previous_hash': self.previous_hash,
            'transactions': self.transactions,
            'proof': self.proof,
            'timestamp': self.timestamp
        }
