# test_transaction.py

import unittest
from src.transaction import Transaction

class TestTransaction(unittest.TestCase):
    
    def setUp(self):
        """Set up mock transactions for testing."""
        self.transaction = Transaction("address_1", "address_2", 100)
    
    def test_valid_transaction(self):
        """Test if a transaction is valid."""
        self.assertTrue(self.transaction.is_valid(), "Transaction should be valid")
    
    def test_invalid_transaction(self):
        """Test if invalid transaction is rejected."""
        self.transaction.amount = -100
        self.assertFalse(self.transaction.is_valid(), "Transaction should be invalid with negative amount")
        
    def test_transaction_attributes(self):
        """Test that the transaction has the correct attributes."""
        self.assertEqual(self.transaction.sender, "address_1")
        self.assertEqual(self.transaction.receiver, "address_2")
        self.assertEqual(self.transaction.amount, 100)
        
if __name__ == '__main__':
    unittest.main()
