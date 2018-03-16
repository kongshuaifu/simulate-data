'''
Created on 2012-5-16

@author: nan.li
'''
import random

class getfakedata(object):
    '''
    classdocs
    '''
    @staticmethod
    def getdata(list):
        pos = random.randint(0,len(list)-1)
        return list[pos]

    @staticmethod
    def getdeviceid():
        sysrand = random.SystemRandom()
        deviceid = str(sysrand.randint(359990000000000, 359999999999999))
        return deviceid
