'''
Created on 2012-5-16

@author: nan.li
'''
from net import net
import json

class service():
    '''
    classdocs
    '''
    
    @staticmethod
    def postclientdata(c,pos="clientdata"):
        jsondata = json.dumps(c)
        net.PostData("clientdata", jsondata,"clientdata")
        
    @staticmethod
    def postusinglog(c,pos="usinglog"):
        jsondata = json.dumps(c)
        net.PostData("usinglog", jsondata,"usinglog")
        
    @staticmethod
    def posterrorlog(c,pos="errorlog"):
        print c
        jsondata = json.dumps(c)
        
        net.PostData("errorlog", jsondata,"errorlog")
  
    @staticmethod
    def posteventlog(c,pos="eventlog"):
        jsondata = json.dumps(c)
        net.PostData("eventlog", jsondata,"eventlog")      
        
        
