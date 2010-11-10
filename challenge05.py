#!/usr/bin/env python
# encoding: utf-8
"""
challenge05.py
http://www.pythonchallenge.com/pc/def/peak.html
pickle:
http://www.pythonchallenge.com/pc/def/banner.p

Created by whimsy on 2010-08-31.
Copyright (c) 2010 Will Crawford. All rights reserved.
"""

import sys
import os
import cPickle as pickle


# This feels really hack-ish =\
def main():
	print "This program expects banner.p in the same directory."
	print "It should be named challenge05.p"
	print "The next challenge word is:"
	the_pickle = pickle.load( open("challenge05.p"))
#	L = sorted(the_pickle)
	for element in the_pickle:		
		for subelement in element:
			for i in range(subelement[1]):
				sys.stdout.write(str(subelement[0]));
		sys.stdout.write('\n')
	return 0

if __name__ == '__main__': main()
