"""Test tabular_log file
"""
import __init__

__author__ = "help@castellanidavide.it"
__version__ = "2.0 2020-08-18"

def test():
	"""Tests the tabular_log function(s)
	"""
	assert __init__.__author__ == "help@castellanidavide.it" , "Sanity test failed"
	assert __init__.tabular_log() != "", "__init__ test failed"
	assert (__init__.tabular_log()).print("Test") != "", "print test failed"
	assert (__init__.tabular_log()).prints(["Test1","Test2"]) != "", "prints test failed"
	
if __name__ == "__main__":
	test()
