#!/usr/bin/env python3

Random_Variable = 13
Random_Variable2 = [20]
for i in Random_Variable2:
  if i >= Random_Variable:
    print('Aye Captain')
  else:
    print('Not True')

if Random_Variable >= 0:
  print('Random_Variable is a positive number')
else:
  print('Random_Variable is a negative number')

if Random_Variable < 0:
  print('Random_Variable is a positive number')
elif Random_Variable == 0:
  print('Random_Variable is equal to 0')
else:
  print('Random_Variable is not equal to 0')

if Random_Variable >= 0:
  if Random_Variable < 50:
    if Random_Variable % 2 == 0:
      print('Random_Variable is a positive number but less than 50 and is an even integer')
    else:
      print('Random_Variable is a positive number but less than 50 but not an even integer')
else:
  print('Random_Variable is a negative number greater then 50 and is an odd integer')

if Random_Variable < 0:
  print('Random_Variable is a positive number')
elif Random_Variable == 0:
  print('Random_Variable is equal to 0')
else:
  print('Random_Variable is not equal to 0')
