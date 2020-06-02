import unittest
from main import welcome

class TestHome(unittest.TestCase):
	def test_welcome_return_correct(self):
		self.assertEqual(welcome("Pedro"), "Welcome Pedro, nice to see you!")