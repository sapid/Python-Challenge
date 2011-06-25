#!/usr/bin/env python
# encoding: utf-8
"""
challenge06.py
http://www.pythonchallenge.com/pc/def/channel.html
zip:
http://www.pythonchallenge.com/pc/def/channel.zip

Started by whimsy on 2010-11-10.
Completed on... [incomplete]
Copyright (c) 2010 Will Crawford. All rights reserved.
"""

import sys
import os
import re
import zipfile


def main():
   print "Thus begins challenge 6!"
   print "The provided hint is:\n"
   print "welcome to my zipped list"
   print "start from 90052"
   print "answer is inside the zip"
   print "\n"
   
   the_zip = None
   print "Trying ./channel.zip"
   try:
      the_zip = zipfile.ZipFile('channel.zip', 'r')
   except (IOError, RuntimeError):
      print "Trying ./challenge06.zip"
      try:
         the_zip = zipfile.ZipFile('challenge06.zip', 'r')
      except (IOError, RuntimeError):
            print "Couldn't find zipfile."
            return 1

   print "File found. \n\nBeginning scan."
   pattern = re.compile(r'(\d+)')
   next_file = '90052'
   next_file = next_file + '.txt'
   while next_file:
      text = the_zip.read(next_file)
      next_file = None
      print text
      try:
         next_file = (pattern.search(text)).group(0)
         next_file = next_file + '.txt'
      except TypeError:
         return 1
      except AttributeError:
         break
      text = None

   return 0

if __name__ == '__main__': main()
