#!/usr/bin/env python3

import unittest
import time

while True:
    x = input("1 for LED on, 0 for LED off: ")
    try:
        y = int(x)   
        if y == 1:
                print("on")
        elif y == 0:
                print("off")
        else:
                print("unknown input, try again")
    except ValueError:
        print ("Not a number")
