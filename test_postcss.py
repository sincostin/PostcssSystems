# test_postcss.py
"""
Tests for Postcss module.
"""

import unittest
from postcss import Postcss

class TestPostcss(unittest.TestCase):
    """Test cases for Postcss class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = Postcss()
        self.assertIsInstance(instance, Postcss)
        
    def test_run_method(self):
        """Test the run method."""
        instance = Postcss()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
