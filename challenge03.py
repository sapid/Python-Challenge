#!/usr/bin/env python
# encoding: utf-8
"""
challenge03.py
http://www.pythonchallenge.com/pc/def/equality.html

Created by whimsy on 2010-08-31.
Copyright (c) 2010 Will Crawford. All rights reserved.
"""

import sys
import os
import re


def main():
	equality = file("challenge3.txt").read()
	sieve = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
	gold = sieve.findall(equality)
	print "".join(gold)
	return 0

if __name__ == '__main__': main()