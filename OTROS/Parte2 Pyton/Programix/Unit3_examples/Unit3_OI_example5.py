#! /usr/bin/python3 
# HPBBM, Unit 3, example 5: redirect input

# reads data from the standard input (stdin)
# data can be feed by keyboard: python3 Unit3_OI_explample5.py
# or redirected from a file: python3 Unit3_OI_explample5.py < anyfile

import sys

UserInput=sys.stdin.read()

print("You gave me:\n",UserInput)