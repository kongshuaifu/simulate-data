'''
Created on 2012-5-16

@author: nan.li
'''


from threadcontroller import threadcontroller

import sys
import random
import os

if __name__ == '__main__':
    
    inputdate = sys.argv[1]
    minCount = int(sys.argv[2])
    maxCount = int(sys.argv[3])
    randomCount = random.randint(minCount,maxCount)

    threadcontroller.PostClientdata(inputdate, randomCount)
    raw_input()
    threadcontroller.PostUsinglog(inputdate, randomCount)
    raw_input()
    threadcontroller.PostEvent(inputdate, randomCount)
    raw_input()
    threadcontroller.PostError(inputdate,randomCount/10)
    raw_input()

    pass
