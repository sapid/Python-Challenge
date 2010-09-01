#!/usr/bin/env python
# encoding: utf-8
"""
challenge02.py
http://www.pythonchallenge.com/pc/def/ocr.html

Created by whimsy on 2010-08-31.
Copyright (c) 2010 Will Crawford. All rights reserved.

This file references ocr.txt; ensure you grabbed it from the repo.
"""

import sys
import os
from string import maketrans, punctuation


def main():
	ocr = file("challenge2.txt").read()
	symbols = punctuation + "\n"
	eraser = maketrans("","")
	print ocr.translate(eraser,symbols)
	return 0


if __name__ == '__main__':
	main()

