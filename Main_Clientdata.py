'''
Created on 2012-5-16

@author: nan.li
'''


from controller import controller
import sys
import time
import datetime
import random

if __name__ == '__main__':
    
    #sys.argv[1]: date
    #sys.argv[2]: repeat times

    #startDate = sys.argv[1]
    endDate = sys.argv[1]
    #minRandom = int(sys.argv[3])
    #maxRandom = int(sys.argv[4])
    

    controller.PostClientdata(endDate)
    
    pass
