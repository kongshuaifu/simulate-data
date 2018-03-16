'''
Created on 2012-5-17

@author: nan.li
'''
from service import service
from readfile import readfile
from getfakedata import getfakedata
import time
import random
import uuid
import datetime


class controller(object):
    '''
    classdocs
    '''
    @staticmethod
    def PostClientdata(edate):
        list_platform = readfile.readtext("platform.txt")

        list_appkey_android = readfile.readtext("android_appkey.txt")
        list_appkey_iphone = readfile.readtext("iphone_appkey.txt")
        list_appkey_winphone = readfile.readtext("winphone_appkey.txt")

        list_osversion_android = readfile.readtext("android_os_version.txt")
        list_osversion_iphone = readfile.readtext("iphone_os_version.txt")
        list_osversion_winphone=readfile.readtext("winphone_os_version.txt")
        
        list_deviceid_android = readfile.readtext("android_deviceid.txt")
        list_deviceid_iphone = readfile.readtext("iphone_deviceid.txt")
        list_deviceid_winphone=readfile.readtext("winphone_deviceid.txt")
        
        
        list_devicename_android = readfile.readtext("android_devicename.txt")
        list_devicename_iphone = readfile.readtext("iphone_devicename.txt")
        list_devicename_winphone=readfile.readtext("winphone_devicename.txt")

        '''
        list_defaultbrowser = readfile.readtext("defaultbrowser.txt")
        list_javasupport = readfile.readtext("javasupport.txt")
        list_flashversion = readfile.readtext("flashversion.txt")
        '''
        list_modulename_android = readfile.readtext("android_modulename.txt")
        list_modulename_iphone = readfile.readtext("iphone_modulename.txt")
        list_modulename_winphone=readfile.readtext("winphone_modulename.txt")

        '''list_imei = readfile.readtext("imei.txt")'''
        list_version = readfile.readtext("version.txt")
        list_language = readfile.readtext("language.txt")
        list_resolution = readfile.readtext("resolution.txt")
        list_ismobiledevice = readfile.readtext("ismobiledevice.txt")
        list_imsi = readfile.readtext("imsi.txt")
        list_phonenumber = readfile.readtext("phonenumber.txt")
        list_haveGPS = readfile.readtext("havegps.txt")
        list_haveBT = readfile.readtext("havebt.txt")
        list_havegravity = readfile.readtext("havegravity.txt")
        list_havewifi = readfile.readtext("havewifi.txt")
        list_wifimac = readfile.readtext("wifimac.txt")
        list_longilati = readfile.readtext("longitude_latitude.txt")
        list_cellid = readfile.readtext("cellid.txt")
        list_mccmnc = readfile.readtext("mccmnc.txt")
        list_lac = readfile.readtext("lac.txt")
        list_network = readfile.readtext("network.txt")
        list_jbreak = readfile.readtext("iphonrjbreak.txt")
        list_hours = readfile.readtext("hour.txt")

        list_activities_android = readfile.readtext("android_activities.txt")
        list_activities_iphone = readfile.readtext("iphone_activities.txt")
        list_activities_winphone = readfile.readtext("winphone_activities.txt")

        list_event_android = readfile.readtext("android_event.txt")
        list_event_iphone = readfile.readtext("iphone_event.txt")
        list_event_winphone = readfile.readtext("winphone_event.txt")

        list_error_android = readfile.readfolder("error/android_error/")
        list_error_iphone = readfile.readfolder("error/iphone_error/")
        list_error_winphone = readfile.readfolder("error/winphone_error/")


        list_duration = readfile.readtext("duration.txt")

        
        edate = time.strptime(edate,"%Y-%m-%d")
        enddate = datetime.date(edate[0],edate[1],edate[2])
    
        currentDay = datetime.datetime.now().date()
        
        '''Loop each day until enddate'''
        while (currentDay <= enddate):            
            print '['+currentDay.strftime("%Y-%m-%d")+']'+"Start Post Data..." 
    
            tmpDate = currentDay
            i = 0
            while (currentDay == tmpDate):


                '''Clientdata'''
                '''================================================================================================='''

                clientdata = {'data':[]}
                for k in range(0, random.randint(1, 3)):
                    c = {}
                    c["platform"] = getfakedata.getdata(list_platform)
                    c["version"] = getfakedata.getdata(list_version)
                    c["language"] = getfakedata.getdata(list_language)
                    c["resolution"] = getfakedata.getdata(list_resolution)
                    c["ismobiledevice"] = getfakedata.getdata(list_ismobiledevice)
                    c["imsi"] = getfakedata.getdata(list_imsi)
                    c["phonenumber"] = getfakedata.getdata(list_phonenumber)
                    c["havebt"] = getfakedata.getdata(list_haveBT)
                    c["havegps"] = getfakedata.getdata(list_haveGPS)
                    c["havegravity"] = getfakedata.getdata(list_havegravity)
                    c["havewifi"] = getfakedata.getdata(list_havewifi)
                    c["wifimac"] = getfakedata.getdata(list_wifimac)
                    temp_l = getfakedata.getdata(list_longilati)
                    l = temp_l.split("_")
                    
                    c["latitude"] = l[1]
                    c["longitude"] = l[0]
                    c["cellid"] = getfakedata.getdata(list_cellid)
                    c["mccmnc"] = getfakedata.getdata(list_mccmnc)
                    c["lac"] = getfakedata.getdata(list_lac)
                    c["network"] = getfakedata.getdata(list_network)
                    '''simulate date '''
                    hour = datetime.datetime.now().hour
                    minute = datetime.datetime.now().minute
                    second = datetime.datetime.now().second
                    demodate = time.strptime(currentDay.strftime("%Y-%m-%d") + " " + str(hour) + ":" + str(minute) + ":" + str(second), "%Y-%m-%d %H:%M:%S")
                    c["time"] = time.strftime("%Y-%m-%d %H:%M:%S", demodate)


                    if c["platform"] == "Android":
                        c["appkey"] = getfakedata.getdata(list_appkey_android)
                        c["os_version"] = getfakedata.getdata(list_osversion_android)
                        c["devicename"] = getfakedata.getdata(list_devicename_android)
                        c["modulename"] = getfakedata.getdata(list_modulename_android)
                        c["deviceid"] = getfakedata.getdeviceid()
                        c["isjailbreak"] = "1"
                        list_activities = list_activities_android
                        c["event_identifier"] = getfakedata.getdata(list_event_android)
                        list_event = list_event_android
                        list_error = list_error_android

                        
                    elif(c["platform"]=="iOS"):
                        c["appkey"] = getfakedata.getdata(list_appkey_iphone)
                        c["os_version"] = getfakedata.getdata(list_osversion_iphone)
                        c["devicename"] = getfakedata.getdata(list_devicename_iphone)
                        c["modulename"] = getfakedata.getdata(list_modulename_iphone)
                        c["deviceid"] = getfakedata.getdeviceid()
                        c["isjailbreak"] = getfakedata.getdata(list_jbreak)
                        list_activities = list_activities_iphone
                        c["event_identifier"] = getfakedata.getdata(list_event_iphone)
                        list_event = list_event_iphone
                        list_error = list_error_iphone

                    else:
                        c["appkey"] = getfakedata.getdata(list_appkey_winphone)
                        c["os_version"] = getfakedata.getdata(list_osversion_winphone)
                        c["devicename"] = getfakedata.getdata(list_devicename_winphone)
                        c["modulename"] = getfakedata.getdata(list_modulename_winphone)
                        c["deviceid"] = getfakedata.getdeviceid()
                        c["isjailbreak"] = "1"
                        list_activities = list_activities_winphone
                        c["event_identifier"] = getfakedata.getdata(list_event_winphone)
                        list_event = list_event_winphone
                        list_error = list_error_winphone
                    clientdata['data'].append(c)
        
                service.postclientdata(clientdata)


                '''Usinglog'''
                '''========================================================================================================='''

                usinglog = {'data':[]}
                for k in range(0, random.randint(1, 3)):
                    d = {}
                    
                    d["version"] = c["version"]
                    d["session_id"] = str(uuid.uuid4().hex)
                    d["appkey"] = c["appkey"]
                    d["deviceid"] = c["deviceid"]
                    d["devicename"] = c["devicename"]
        

                    endtime = time.strptime(currentDay.strftime("%Y-%m-%d") + " " + str(hour) + ":" + str(minute) + ":" + str(second), "%Y-%m-%d %H:%M:%S")
                    d["end_millis"] = time.strftime("%Y-%m-%d %H:%M:%S", endtime)
                    enddate2 = datetime.datetime(endtime[0],endtime[1],endtime[2],endtime[3],endtime[4],endtime[5])


                    '''Make activities, separate with "|"'''
                    d["activities"] = ""
                    d["sd"] = ""
                    d["duration"] = "0"
                    usepages = random.randint(1,len(list_activities))
                    startdate = enddate2
                    for j in range(0,usepages):
                        random_second = random.randint(1,len(list_duration))
                        d["sd"] += str(random_second*1000)
                        d["duration"] = str(int(d["duration"]) + random_second*1000)
                        startdate -= datetime.timedelta(seconds=random_second)
                        d["activities"] += getfakedata.getdata(list_activities)
                        if (j < usepages-1):
                            d["activities"] += "|"
                            d["sd"] += "|"
                            
                    d["start_millis"]=str(startdate)
                    usinglog['data'].append(d)

                service.postusinglog(usinglog)


                '''
                end post usinglog
                '''

                ''' Event '''
                ''' ========================================================================= '''

                event = {'data':[]}
                session_id = str(uuid.uuid4().hex)
                for k in range(0, random.randint(1, 3)):
                    e = {}
                    e["version"] = c["version"]
                    e["appkey"] = c["appkey"]
                    e["deviceid"] = c["deviceid"]
                    e["session_id"] = session_id
                    for j in range(0,usepages/2):
                        e["activity"] = getfakedata.getdata(list_activities)
                        loop = len(list_event)
                        enddate3 = c["time"]
                        
                        lloop = random.randint(1,loop)
                        for m in range(0,lloop/3):
                            #random_second = random.randint(1,120)
                            #enddate3 = startdate+datetime.timedelta(seconds=random_second)
                            enddate3 = c["time"]
                            e["time"] = c["time"]
                            
                            e["event_identifier"] = getfakedata.getdata(list_event)
                            e["label"] = "label"
                            e["acc"]=random.randint(1,5)
                            event['data'].append(e)

                if event['data']:
                    service.posteventlog(event)
                            #print "-------->["+str(enddate3)+"]"+"Post Event " + str(k+1)+"/"+str(lloop)+" OK!"
                        #print "----->["+str(enddate3)+"]"+"Post Event Activity" + str(j)+"/"+str(usepages)+" OK!"
                    #print "-->["+currentDay.strftime("%Y-%m-%d")+"]"+"Post Event "

                '''Post Error'''
                ''' =================================================================== '''

                error = {'data':[]}
                for k in range(0, random.randint(1, 3)):
                    roll = random.randint(1, 20)
                    if (roll == 1):
                        f={}
                        f["version"] = c["version"]
                        f["appkey"] = c["appkey"]
                        f["activity"] =  getfakedata.getdata(list_activities)
                        f["os_version"] = c["os_version"]
                        f["deviceid"] = c["deviceid"]
                        f["devicename"] = c["devicename"]
                        f["stacktrace"] = getfakedata.getdata(list_error)
                        f["time"] = c["time"]
                        error['data'].append(f)

                if error['data']:
                    service.posterrorlog(error)
                        #print "-->["+c["time"]+"]"+"Post Error "

                time.sleep(0.1)
                i += 1
                currentDay = datetime.datetime.now().date()

            '''start next day's data'''
            #currentDay = datetime.datetime.now().date()
            print "loop end",currentDay
