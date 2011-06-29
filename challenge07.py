#!/usr/bin/env python
# encoding: utf-8
"""
challenge06.py
http://www.pythonchallenge.com/pc/def/oxygen.html
image:
http://www.pythonchallenge.com/pc/def/oxygen.png

Started by whimsy on 2011-6-25.
Completed on... [incomplete]
Copyright (c) 2011 Will Crawford. All rights reserved.
"""

import sys
import os
import Image

def main():
   try:
      im = Image.open('challenge07.png')
   except (IOError):
      try:
         im = Image.open('oxygen.png')
      except:
         print "Couldn't find image."
         return 1
   print "File found. \nBeginning processing...\n"
   print "Size = " + str(im.size) + "px"
   pix = im.load()
   decoded = ''
   for i in range(87):
      j = i*7
      decoded = decoded + chr(pix[j, 43][1])
   print decoded
   print "\nHardcoded answer: "
   ans = [ 105, 110, 116, 101, 103, 114, 105, 116, 121 ]
   answer = ''
   for i in ans:
      answer = answer + chr(i)
   print answer
   return 0

if __name__ == '__main__': main()

