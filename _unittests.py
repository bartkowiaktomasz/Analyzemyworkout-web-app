"""
Script for unit testing.
Ignore warnings with:
python -W ignore _unittests.py
"""

import requests
import unittest
from main import index

from config import *

class TestMain(unittest.TestCase):

    def test_index(self):
        response = requests.get(IP_LOCAL)
        # Get method not allowed, should return 405
        self.assertEqual(response.status_code, 405)

        response = requests.post(IP_LOCAL, {'activity': 'Test'})
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()
