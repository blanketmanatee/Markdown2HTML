#!/usr/bin/python3
""" takes an arg of two strings"""

from sys import argv, stderr
from os import path

if __name__=='__main__':
    if len(argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html", file=stderr)
        exit(1)
    
    if path.exists(argv[1]) == False:
        print("Missing {}".format(argv[1]), file=stderr)
        exit(1)
    