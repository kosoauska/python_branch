import sys
import math
from random import *
import string

class func():
    version = 1.0
    def prin(self , input = True):
        try:
            handle = open("e:\\test.txt" , "r+")
            for eachline in handle:
                if input == True:
                    print(eachline)
                else:
                    print("what")
            handle.writelines("haha" * 10)
            handle.close()
        except IOError as e :
                print("file open error : " , e)

    def __init__(self , nm = 'john doe'):
        self.name = nm + " hello "
        print("init %s version = %0.2f " % (self.name , self.version))

a = ('abc' , 'def' , 'ghi')
a = '.'.join(a)
print(a)
print("%#x" % 124)
print(r"\n")
print(id(a))
"""
print(hex(10))
print("hello world")
print(randint(1 , 20))

print(ord("a"))
print(chr(ord('a')))
for i  in range(1 , 5):
    print(round(math.pi , i))
print(divmod(100 , 33))
print(abs(-1))
test = func("mack")
test.prin()
test.prin(123)
sys.stdout.write("hello world \n")
"""
