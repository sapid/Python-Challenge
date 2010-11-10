#!/usr/bin/env python
# encoding: utf-8
"""
challenge04.py
http://www.pythonchallenge.com/pc/def/linkedlist.php

Created by whimsy on 2010-08-31.
Copyright (c) 2010 Will Crawford. All rights reserved.
"""

import sys
import os
import urllib
import re


# This feels really hack-ish =\
def main():
	print "You must be connected to the internet to run this challenge solution."
	nugget ='12345'
	page = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nugget)
	nugget = re.search(r"(\d+)", page.read())
	previousnugget = nugget
	while nugget:
		page = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nugget.group(0))
		previousnugget = nugget
		nugget = re.search(r"(\d+)$", page.read())
		if nugget:
			print nugget.group(0)
	# We have an edge case here.
	page = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(int(previousnugget.group(0))/2))
	nugget = re.search(r"(\d+)$", page.read())
	
	while nugget:
		print nugget.group(0)
		page = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nugget.group(0))
		previousnugget = nugget
		nugget = re.search(r"(\d+)$", page.read())

	# We're done now.
	page = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + previousnugget.group(0))	
	print page.read()
	return 0

if __name__ == '__main__': main()
