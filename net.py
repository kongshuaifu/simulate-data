'''
Created on 2012-5-16

@author: nan.li
'''
import urllib,urllib2
#urlpre = 'http://www.cobub.com/demo/service/index.php'
#urlpre = 'http://192.168.1.199/cobub_v3/index.php?/ums/'
#urlpre = 'http://demo.cobub.com/cobubv3/index.php?/ums/'
urlpre = 'http://DB2.Ali:8008/'
class net:
    
    ok = 0
    error = 0
    ex = 0
    
    @staticmethod
    def PostData(url,postdata,pos):
        
        try:
            #print "POST="+postdata 
            post_data = urllib.urlencode({'content':postdata})
            
            response = urllib2.Request(urlpre+url,post_data) 
            print urlpre+url
            
            f= urllib2.urlopen(response)
            s= f.read()
            print pos+s
            if s.find('''"flag":1''')>0:
                net.ok = net.ok +1
                
            else:
                net.error = net.error +1
            print net.ok,"/",net.error,"/",net.ex

        except Exception,data:
            print data
            net.ex = net.ex+1
            print net.ok,"/",net.error,"/",net.ex

    @staticmethod
    def PostData1(url,postdata):
        
        try:
            post_data = urllib.urlencode({'content':postdata})
            response = urllib2.Request(urlpre+url,post_data) 
            urllib2.urlopen(response)          

        except Exception,data:
            print data
            #print data

    
        
