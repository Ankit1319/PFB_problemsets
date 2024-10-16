#!/usr/bin/env python3
import sys

Random_Variable = int(sys.argv[1])
if Random_Variable >= 0:
  print('Randam_Variable is a positive intiger')
else:
  print('Random_Variable is not a positive integer')

if Random_Variable == -1:
  print('oops its a negative integer')
elif Random_Variable == 0:
  print('Random_Variable is equal to 0')
else:
  print('Random_variable is not equal to 0')

if Random_Variable >= 0:
  if Random_Variable < 50:
    print('Random_Variable is greater than 0 but less then 50')
  else:
    print('Random_Variable is not greater than 0')

if Random_Variable >= 0:
  if Random_Variable > 50:
    if Random_Variable % 3 == 0:
      print('Random_Variable is greater then 50 and is divisible by 3')
    else:
      print('Random_Variable is greater then 50 but is not divisible by 3')
  else:
    print('Random_Variable is not greater then 50,so sorrry')

  



