'''
Created on 2012-5-16

@author: nan.li
'''
import os

class readfile(object):
    '''
    classdocs
    '''
#    @staticmethod
#    def readtext(filename):
#        f = open("clientdata\\"+filename,"r")
#        lines =f.readlines()
#        f.close()
#        l = []
#        for line in lines:
#            l.append(line.rstrip())
#        return l
    
    @staticmethod
    def readtext(filename,folder="fakedata/"):
        f = open(folder+filename,"r")
        lines =f.readlines()
        f.close()
        l = []
        for line in lines:
            l.append(line.rstrip())
        return l

    @staticmethod
    def readfolder(folder):
        e = []
        fo = os.listdir(folder)
        for filename in fo:
            f= open(folder+filename,"r")
            print "filename=",filename
            lines =f.readlines()
            f.close()
            res = ''.join(line for line in lines)
            e.append(res)
        return e

            
        
        
        
