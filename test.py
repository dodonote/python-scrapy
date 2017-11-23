import time
import pdb
import sys

print sys.getdefaultencoding()

print range(17501, 100000)

def test():
    now_time = time.time();
    print now_time
    a= 10
    print a
    # return
    a += 1
    print a
    # exit
    b = 'test string'
    pdb.set_trace
    print pdb
    print b
    print time.time()

if __name__ == '__main__':

    test()
