#!/usr/bin/python3
lookup = __import__('0-lookup').lookup


class MyClass2(object):
      my_attr1 = 3

print(lookup(MyClass2))
