"""
Script for Flask app unit testing.
Ignore warnings with:
python -W ignore main.py

Coverage:
coverage run --source . --omit=preprocessing.py, test_main.py
"""

import unittest
import pexpect
import sys
sys.path.append("..")

import pandas as pd
from flask import Flask

import main
from main import app
from config import *

class TestMain(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def tearDown(self):
        pass

    def test_index(self):
        response = self.app.get('/', follow_redirects=True)
        # Get method not allowed
        self.assertEqual(response.status_code, 405)

        # Bad request
        response = self.app.post('/', data={})
        self.assertEqual(response.status_code, 400)

        # Proper payload
        df = pd.read_json('dummy_json.JSON')
        df_json = df.to_json()
        payload = {'payload_json': df_json}
        response = self.app.post('/', data=payload)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
