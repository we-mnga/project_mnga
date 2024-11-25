# test_blockchain.py

import unittest
from src.blockchain import Blockchain
from src.transaction import Transaction
from src.block import Block

class TestBlockchain(unittest.TestCase):
    
    def setUp(self):
        """Set up a new blockchain with mock data."""
        self.blockchain = Blockchain()
        transaction_1 = Transaction("address_1", "address_2", 100)
        transaction_2 = Transaction("address_2", "address_3", 50)
        block_1 = Block([transaction_1, transaction_2], previous_hash="000000")
        self.blockchain.add_block(block_1)
    
    def test_blockchain_integrity(self):
        """Test if blockchain's integrity is maintained."""
        self.assertTrue(self.blockchain.is_valid(), "Blockchain should be valid")
    
    def test_invalid_blockchain(self):
        """Test if an invalid block breaks the blockchain's integrity."""
        invalid_block = Block([Transaction("address_1", "address_2", 50)], previous_hash=self.blockchain.blocks[-1].hash)
        invalid_block.hash = "tampered_hash"  # Simulating a tampered block
        self.blockchain.add_block(invalid_block)
        self.assertFalse(self.blockchain.is_valid(), "Blockchain should be invalid after tampering")
    
    def test_add_valid_block(self):
        """Test if a new valid block can be added to the blockchain."""
        transaction = Transaction("address_3", "address_4", 200)
        block = Block([transaction], previous_hash=self.blockchain.blocks[-1].hash)
        self.blockchain.add_block(block)
        self.assertEqual(len(self.blockchain.blocks), 2, "Blockchain should have 2 blocks")
        
if __name__ == '__main__':
    unittest.main()
