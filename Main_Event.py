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
    


    min = int(sys.argv[3])
    max = int(sys.argv[4])
    

    #controller.PostClientdata(sys.argv[1], min,sys.argv[2],max)
    #controller.PostUsinglog(sys.argv[1], min,sys.argv[2],max)
    controller.PostEvent(sys.argv[1], min,sys.argv[2],max)
    #controller.PostError(sys.argv[1], min,sys.argv[2],max)


    
    
    pass