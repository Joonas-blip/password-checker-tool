#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:30:09 2019

@author: joonas
"""

import re
password = input("What is your password? ")
x = True
while x:
    if not re.search("[a-z]",password):
        break
    elif not re.search("[A-Z]",password):
        break
    elif not re.search("[1-9]",password):
        break
    elif not re.search("[$@#]",password):
        break
    else:
        print("Valid Password")
        x = False
        break

if x:
    print("Invalid Password")


