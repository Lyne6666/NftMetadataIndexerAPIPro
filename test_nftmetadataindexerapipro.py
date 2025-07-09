# test_nftmetadataindexerapipro.py
"""
Tests for NftMetadataIndexerAPIPro module.
"""

import unittest
from nftmetadataindexerapipro import NftMetadataIndexerAPIPro

class TestNftMetadataIndexerAPIPro(unittest.TestCase):
    """Test cases for NftMetadataIndexerAPIPro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NftMetadataIndexerAPIPro()
        self.assertIsInstance(instance, NftMetadataIndexerAPIPro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NftMetadataIndexerAPIPro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
