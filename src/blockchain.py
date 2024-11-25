from block import Block
from proof_of_work import ProofOfWork

class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = []
        self.current_transactions = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Creates and adds the genesis block to the blockchain.

        The genesis block is the first block in the blockchain and has special properties:
        - Its index is 0
        - Its previous hash is "0"
        - It contains no transactions
        - Its timestamp is 0

        This method initializes the blockchain by creating the genesis block,
        computing its proof of work, and adding it to the chain.

        Returns:
            None
        """
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
        """
    Retrieves the most recent block in the blockchain.

    This property dynamically returns the last block added to the chain, which is
    necessary for operations like mining a new block or validating the chain.

    The use of @property allows it to be accessed like an attribute, improving readability
    and encapsulating the logic for fetching the last block.

    Returns:
        Block: The last block in the blockchain.
    """
        return self.chain[-1]


