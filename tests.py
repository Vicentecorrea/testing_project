import unittest
import home_tests

def main():
	print("Running tests...")
	home_tester = unittest.TestLoader().loadTestsFromModule(home_tests)
	results = unittest.TextTestRunner(verbosity=2).run(home_tester)
	if len(results.failures) > 0:
		print("Error, {} tests failed".format(len(results.failures)))
		return 1/0
	print("No test failed")

if __name__ == '__main__':
	main()