'''
Created on 2012-5-16

@author: nan.li
'''


from threadcontroller import threadcontroller
import sys


if __name__ == '__main__':
    
    #sys.argv[1]: date
    #sys.argv[2]: repeat times
    

    

    threadcontroller.PostClientdata(sys.argv[1], sys.argv[2])
    #controller.PostUsinglog(sys.argv[1], min,sys.argv[2],max)
    #controller.PostEvent(sys.argv[1], min,sys.argv[2],max)
    #controller.PostError(sys.argv[1], min,sys.argv[2],max)


    
    
    pass