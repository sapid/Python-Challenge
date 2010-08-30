#!/usr/bin/env python
# encoding: utf-8
"""
challenge2.py
http://www.pythonchallenge.com/pc/def/map.html

Created by whimsy on 2010-08-29.
Copyright (c) 2010 Will Crawford. All rights reserved.

I think the answer is this:
http://www.pythonchallenge.com/pc/def/ocr.html
"""

import sys
import os


def main():
	a = list("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")
	for i in range(0,len(a)):
		if a[i] not in [" ", "(", ")", ".", "'"]:
			a[i] = chr(ord(a[i]) + 2)
			if ord(a[i]) > ord('z'):
				a[i] = chr(ord(a[i]) - 26)
	s = ''.join(a)
	print s
	return 0


if __name__ == '__main__':
	main()

