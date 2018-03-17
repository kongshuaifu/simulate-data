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
import threading
import thread


class myThread_clientdata(threading.Thread):
    def __init__(self, pos, postcontent):
        threading.Thread.__init__(self)
        self.postcontent = postcontent
        self.pos = pos

    def run(self):
        return service.postclientdata(self.postcontent, self.pos)


class myThread_usinglog(threading.Thread):
    def __init__(self, pos, postcontent):
        threading.Thread.__init__(self)
        self.postcontent = postcontent
        self.pos = pos

    def run(self):
        return service.postusinglog(self.postcontent, self.pos)


class myThread_event(threading.Thread):
    def __init__(self, pos, postcontent):
        threading.Thread.__init__(self)
        self.postcontent = postcontent
        self.pos = pos

    def run(self):
        return service.posteventlog(self.postcontent, self.pos)


class myThread_error(threading.Thread):
    def __init__(self, pos, postcontent):
        threading.Thread.__init__(self)
        self.postcontent = postcontent
        self.pos = pos

    def run(self):
        return service.posterrorlog(self.postcontent, self.pos)


class threadcontroller(object):
    '''
    classdocs
    '''

    @staticmethod
    def PostClientdata(date, count):
        list_platform = readfile.readtext("platform.txt")
        list_appkey_android = readfile.readtext("android_appkey.txt")
        list_appkey_iphone = readfile.readtext("iphone_appkey.txt")
        list_osversion_android = readfile.readtext("android_os_version.txt")
        list_osversion_iphone = readfile.readtext("iphone_os_version.txt")
        list_version = readfile.readtext("version.txt")
        list_language = readfile.readtext("language.txt")
        list_resolution = readfile.readtext("resolution.txt")
        list_deviceid_android = readfile.readtext("android_deviceid.txt")
        list_deviceid_iphone = readfile.readtext("iphone_deviceid.txt")

        list_ismobiledevice = readfile.readtext("ismobiledevice.txt")
        list_devicename_android = readfile.readtext("android_devicename.txt")
        list_devicename_iphone = readfile.readtext("iphone_devicename.txt")
        '''
        list_defaultbrowser = readfile.readtext("defaultbrowser.txt")
        list_javasupport = readfile.readtext("javasupport.txt")
        list_flashversion = readfile.readtext("flashversion.txt")
        '''
        list_modulename_android = readfile.readtext("android_modulename.txt")
        list_modulename_iphone = readfile.readtext("iphone_modulename.txt")
        '''list_imei = readfile.readtext("imei.txt")'''
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

        sdate = time.strptime(date, "%Y-%m-%d")
        startdate = datetime.datetime(sdate[0], sdate[1], sdate[2])

        d = startdate

        postitems = []
        for ii in range(0, int(count)):
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
            hour = getfakedata.getdata(list_hours)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            # demodate = time.strptime(d.strftime("%Y-%m-%d") + " " + str(hour) + ":" + str(minute) + ":" + str(second), "%Y-%m-%d %H:%M:%S")

            # c["time"] = time.strftime("%Y-%m-%d %H:%M:%S", demodate)
            c["time"] = d.strftime("%Y-%m-%d") + " " + str(hour) + ":" + str(minute) + ":" + str(second)
            if c["platform"] == "android":
                c["appkey"] = getfakedata.getdata(list_appkey_android)
                c["os_version"] = getfakedata.getdata(list_osversion_android)
                c["devicename"] = getfakedata.getdata(list_devicename_android)
                c["modulename"] = getfakedata.getdata(list_modulename_android)
                c["deviceid"] = getfakedata.getdata(list_deviceid_android)
                c["isjailbreak"] = "1"

            else:
                c["appkey"] = getfakedata.getdata(list_appkey_iphone)
                c["os_version"] = getfakedata.getdata(list_osversion_iphone)
                c["devicename"] = getfakedata.getdata(list_devicename_iphone)
                c["modulename"] = getfakedata.getdata(list_modulename_iphone)
                c["deviceid"] = getfakedata.getdata(list_deviceid_iphone)
                c["isjailbreak"] = getfakedata.getdata(list_jbreak)

            postitems.append(c)

        for ii in range(0, int(count)):
            print  ii, "Clientdata Start"
            thread = myThread_clientdata(ii, postitems[ii])
            thread.start()

    @staticmethod
    def PostUsinglog(date, count):
        list_platform = readfile.readtext("platform.txt", "fakedata/")
        list_appkey_android = readfile.readtext("android_appkey.txt", "fakedata/")
        list_appkey_iphone = readfile.readtext("iphone_appkey.txt", "fakedata/")
        list_activities_android = readfile.readtext("android_activities.txt", "fakedata/")
        list_activities_iphone = readfile.readtext("iphone_activities.txt", "fakedata/")
        list_version = readfile.readtext("version.txt", "fakedata/")
        list_hours = readfile.readtext("hour.txt", "fakedata/")

        sdate = time.strptime(date, "%Y-%m-%d")
        startdate = datetime.datetime(sdate[0], sdate[1], sdate[2])
        d = startdate
        print d.strftime("%Y-%m-%d") + "UsingLog"

        for i in range(0, int(count)):
            postitems = []
            c = {}
            platform = getfakedata.getdata(list_platform)
            c["version"] = getfakedata.getdata(list_version)
            c["session_id"] = str(uuid.uuid4().hex)
            if platform == "android":
                c["appkey"] = getfakedata.getdata(list_appkey_android)
            else:
                c["appkey"] = getfakedata.getdata(list_appkey_iphone)

            usepages = random.randint(1, 12)
            tempdate = ""
            for j in range(0, usepages):
                if platform == "android":
                    c["activities"] = getfakedata.getdata(list_activities_android)
                else:
                    c["activities"] = getfakedata.getdata(list_activities_iphone)

                hour = getfakedata.getdata(list_hours)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                if (j == 0):
                    starttime = time.strptime(
                        d.strftime("%Y-%m-%d") + " " + str(hour) + ":" + str(minute) + ":" + str(second),
                        "%Y-%m-%d %H:%M:%S")
                    c["start_millis"] = time.strftime("%Y-%m-%d %H:%M:%S", starttime)
                    startdate = datetime.datetime(starttime[0], starttime[1], starttime[2], starttime[3], starttime[4],
                                                  starttime[5])
                else:
                    starttime = tempdate
                    c["start_millis"] = str(tempdate)
                    startdate = tempdate

                random_second = random.randint(1, 220)
                enddate = startdate + datetime.timedelta(seconds=random_second)
                tempdate = enddate
                c["end_millis"] = str(enddate)

                c["duration"] = str(random_second * 1000)
                postitems.append(c)

                print "       [" + c["start_millis"] + "]-[" + c["end_millis"] + "]" + "Activity Usage:" + str(
                    j) + "/" + str(usepages)
                # end activities loop
            print i, "/", count, " Usinglog start"
            for ii in range(0, usepages):
                print ii, "Usinglog Start thread"
                thread = myThread_usinglog(ii, postitems[ii])
                thread.start()
            print "    [" + d.strftime("%Y-%m-%d") + "]" + "Post UsingLog One Time Usage" + str(i) + "/" + str(count)

    @staticmethod
    def PostEvent(date, count):
        list_platform = readfile.readtext("platform.txt", "fakedata/")
        list_appkey_android = readfile.readtext("android_appkey.txt", "fakedata/")
        list_appkey_iphone = readfile.readtext("iphone_appkey.txt", "fakedata/")
        list_event_android = readfile.readtext("android_event.txt", "fakedata/")
        list_event_iphone = readfile.readtext("iphone_event.txt", "fakedata/")
        list_activities_android = readfile.readtext("android_activities.txt", "fakedata/")
        list_activities_iphone = readfile.readtext("iphone_activities.txt", "fakedata/")
        list_version = readfile.readtext("version.txt", "fakedata/")
        list_hours = readfile.readtext("hour.txt", "fakedata/")

        sdate = time.strptime(date, "%Y-%m-%d")
        startdate = datetime.datetime(sdate[0], sdate[1], sdate[2])
        d = startdate

        for i in range(0, int(count)):
            postitems = []
            c = {}
            platform = getfakedata.getdata(list_platform)
            c["version"] = getfakedata.getdata(list_version)
            if platform == "android":
                c["appkey"] = getfakedata.getdata(list_appkey_android)
                usepages = random.randint(0, len(list_activities_android))
            else:
                c["appkey"] = getfakedata.getdata(list_appkey_iphone)
                usepages = random.randint(0, len(list_activities_iphone))

            hour = getfakedata.getdata(list_hours)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)

            starttime = time.strptime(d.strftime("%Y-%m-%d") + " " + str(hour) + ":" + str(minute) + ":" + str(second),
                                      "%Y-%m-%d %H:%M:%S")
            # c["time"] = time.strftime("%Y-%m-%d %H:%M:%S", starttime)
            startdate = datetime.datetime(starttime[0], starttime[1], starttime[2], starttime[3], starttime[4],
                                          starttime[5])

            label_list = ("label%s" %i for i in range(25))

            for j in range(0, usepages):
                print "-----------------------"
                print j
                random_second = random.randint(1, 120)
                enddate = startdate + datetime.timedelta(seconds=random_second)
                if platform == "android":
                    c["activity"] = getfakedata.getdata(list_activities_android)
                    loop = len(list_event_android)
                else:
                    c["activity"] = getfakedata.getdata(list_activities_iphone)
                    loop = len(list_event_iphone)

                lloop = random.randint(1, loop)
                for k in range(0, lloop):
                    random_second = random.randint(1, 120)
                    enddate = startdate + datetime.timedelta(seconds=random_second)
                    c["clientdate"] = str(enddate)
                    if platform == "android":
                        c["event_identifier"] = getfakedata.getdata(list_event_android)
                    else:
                        c["event_identifier"] = getfakedata.getdata(list_event_iphone)
                    c["label"] = random.choice(list(label_list))
                    c["acc"] = random.randint(1, 5)
                    postitems.append(c)

                    # service.posteventlog(c)
                    print "            [" + str(enddate) + "]" + "Post Event " + str(k) + "/" + str(lloop) + " OK!"
                print "        [" + str(enddate) + "]" + "Post Event Activity" + str(j) + "/" + str(usepages) + " OK!"

            for ii in range(0, len(postitems)):
                print ii, "Event Start thread"
                thread = myThread_event(ii, postitems[ii])
                thread.start()

            print "    [" + d.strftime("%Y-%m-%d") + "]" + "Post Event " + str(i) + "/" + str(count) + " OK!"
        print "----------------End Event Post Data----------------------"

    @staticmethod
    def PostError(date, count):
        list_platform = readfile.readtext("platform.txt", "fakedata/")
        list_appkey_android = readfile.readtext("android_appkey.txt", "fakedata/")
        list_appkey_iphone = readfile.readtext("iphone_appkey.txt", "fakedata/")
        list_activities_android = readfile.readtext("android_activities.txt", "fakedata/")
        list_activities_iphone = readfile.readtext("iphone_activities.txt", "fakedata/")
        list_version = readfile.readtext("version.txt", "fakedata/")
        list_hours = readfile.readtext("hour.txt", "fakedata/")
        list_osversion_android = readfile.readtext("android_os_version.txt", "fakedata/")
        list_osversion_iphone = readfile.readtext("iphone_os_version.txt", "fakedata/")
        list_devicename_android = readfile.readtext("android_devicename.txt", "fakedata/")
        list_devicename_iphone = readfile.readtext("iphone_devicename.txt", "fakedata/")
        list_error_android = readfile.readfolder("error/android_error/")
        list_error_iphone = readfile.readfolder("error/iphone_error/")

        sdate = time.strptime(date, "%Y-%m-%d")

        startdate = datetime.datetime(sdate[0], sdate[1], sdate[2])

        d = startdate

        print d.strftime("%Y-%m-%d") + "Error"
        postitems = []
        for i in range(0, int(count)):

            c = {}
            platform = getfakedata.getdata(list_platform)
            c["version"] = getfakedata.getdata(list_version)
            if platform == "android":
                c["appkey"] = getfakedata.getdata(list_appkey_android)
                c["activity"] = getfakedata.getdata(list_activities_android)
                c["os_version"] = getfakedata.getdata(list_osversion_android)
                c["deviceid"] = getfakedata.getdata(list_devicename_android)
                c["stacktrace"] = getfakedata.getdata(list_error_android)
            else:
                c["appkey"] = getfakedata.getdata(list_appkey_iphone)
                c["activity"] = getfakedata.getdata(list_activities_iphone)
                c["os_version"] = getfakedata.getdata(list_osversion_iphone)
                c["deviceid"] = getfakedata.getdata(list_devicename_iphone)
                c["stacktrace"] = getfakedata.getdata(list_error_iphone)
            hour = getfakedata.getdata(list_hours)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            # starttime = time.strptime(d.strftime("%Y-%m-%d") + " " + str(hour) + ":" + str(minute) + ":" + str(second), "%Y-%m-%d %H:%M:%S")
            # c["time"] = time.strftime("%Y-%m-%d %H:%M:%S", starttime)
            c["time"] = d.strftime("%Y-%m-%d") + " " + str(hour) + ":" + str(minute) + ":" + str(second)

            # service.posterrorlog(c)
            postitems.append(c)

        for ii in range(0, len(postitems)):
            print ii, "Event Start thread"
            thread = myThread_error(ii, postitems[ii])
            thread.start()
            # print "    ["+c["time"]+"]"+"Post Error " + str(i)+"/"+str(int(count))
