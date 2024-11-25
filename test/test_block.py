# test_block.py

import unittest
from src.block import Block
from src.transaction import Transaction

class TestBlock(unittest.TestCase):
    
    def setUp(self):
        """Create a block with mock transactions for testing."""
        self.transaction_1 = Transaction("address_1", "address_2", 50)
        self.transaction_2 = Transaction("address_2", "address_3", 150)
        self.block = Block([self.transaction_1, self.transaction_2], previous_hash="000000")
    
    def test_block_hash(self):
        """Test if the block's hash is generated correctly."""
        expected_hash = self.block.calculate_hash()
        self.assertEqual(self.block.hash, expected_hash, "Block hash should match the calculated hash")
        
    def test_block_transactions(self):
        """Test that transactions are correctly assigned to a block."""
        self.assertEqual(len(self.block.transactions), 2)
        self.assertEqual(self.block.transactions[0].amount, 50)
        self.assertEqual(self.block.transactions[1].amount, 150)
    
if __name__ == '__main__':
    unittest.main()
