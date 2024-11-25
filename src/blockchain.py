from src.block import Block
from src.proof_of_work import ProofOfWork

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.current_transactions = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", [], 0)
        genesis_block.proof = ProofOfWork.compute_proof_of_work(0, self.difficulty)
        genesis_block_hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_transaction(self, sender, recipient, amount):
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        }
        self.current_transactions.append(transaction)
        return self.last_block.index + 1

    def mine_block(self):
        last_block = self.last_block
        proof = ProofOfWork.compute_proof_of_work(last_block.proof, self.difficulty)
        new_block = Block(len(self.chain), last_block.compute_hash(), self.current_transactions, proof)
        self.chain.append(new_block)
        self.current_transactions = []

    @property
    def last_block(self):
        return self.chain[-1]
