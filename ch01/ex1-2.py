#!/usr/bin/env python3

import unittest
import time

while True:
    x = input("please enter the secret key: ")
    if x == 'a':   
        print("your answer is right, welcome")
    else:
        print("wrong answer, bye~")
