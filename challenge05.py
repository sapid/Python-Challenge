#!/usr/bin/env python
# encoding: utf-8
"""
challenge05.py
http://www.pythonchallenge.com/pc/def/peak.html
pickle:
http://www.pythonchallenge.com/pc/def/banner.p

Created by whimsy on 2010-08-31.
Completed on 2010-11-09.
Copyright (c) 2010 Will Crawford. All rights reserved.
"""

import sys
import os
import cPickle as pickle

def main():
	print "This program expects banner.p in the same directory."
	print "It should be named challenge05.p"
	print "The next challenge word is..."
	the_pickle = pickle.load( open("challenge05.p"))
	for element in the_pickle:	# Traverse the first set of lists	
		for subelement in element: # Traverse the lists in the lists
			for i in range(subelement[1]): # The second tuple element contains repetition information
				sys.stdout.write(str(subelement[0])); # The first tuple element contains the character to be repeated.
		sys.stdout.write('\n') # Each element in the_pickle is a separate banner line.
	return 0

if __name__ == '__main__': main()
