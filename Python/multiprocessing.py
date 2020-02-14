#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      No
#
# Created:     06/12/2019
# Copyright:   (c) No 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from multiprocessing import Process

def f(name):
    print("Hello", name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
