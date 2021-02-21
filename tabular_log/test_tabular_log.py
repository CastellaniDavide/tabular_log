"""Test tabular_log file
"""
from tabular_log import *

__author__ = "help@castellanidavide.it"
__version__ = "2.0 2020-08-18"

def test():
	"""Tests the tabular_log function in the tabular_log class
	Write here all test you want to do.
	REMEMBER to test your programm you can't use __init__ function
	"""
	assert tabular_log.tabular_log() == "tabular_log", "test failed"
	#assert tabular_log.<function>(<values>) == <the result(s) you would like to have>, "<the fail message>"
	
if __name__ == "__main__":
	test()
