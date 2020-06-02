import unittest
from main import welcome

class TestHome(unittest.TestCase):
	def test_welcome_return_correct(self):
		self.assertEqual(welcome("Pedro"), "Welcome Pedro, nice to see you!")

	def test_incorrect_welcome_return_correct_not_equal(self):
		self.assertNotEqual(welcome("Juan"), "Welcome Diego, nice to see you!")
