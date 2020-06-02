import unittest
import home_tests

def main():
	print("Running test...")
	home_tester = unittest.TestLoader().loadTestsFromModule(home_tests)
	unittest.TextTestRunner(verbosity=2).run(home_tester)
	print("Done testing")

if __name__ == '__main__':
	main()