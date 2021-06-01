#!/usr/bin/python3

import re
import collections


LOG_FILE = 'access_log.txt'

###########################
# log pattern
CLIENT = r'(.*?)'
SPACE = r'\s'
IDENTITY = r'\S+'
USER = r'\S+'
TIMESTAMP = r'\[(.*?)\s.*?\]'
PAGE = r'\"(.*?)\"'
STATUS = r'([\d]{3})'
SIZE = r'(.*?)'
logPattern = CLIENT+SPACE+IDENTITY+SPACE+ \
                     USER+SPACE+TIMESTAMP+SPACE+ \
                     PAGE+SPACE+ \
                     STATUS+SPACE+SIZE+SPACE
###################################

parserList = []

with open(LOG_FILE) as fh:
    for logLine in fh:
        result = re.search(logPattern,logLine)
        result = re.search(logPattern,logLine)
        logline_IP = result.group(1)
        logline_TIMESTAMP = result.group(2)
        logline_PAGE = result.group(3)
        logline_STATUS = result.group(4)
        logline_SIZE = result.group(5)
        parserList.append( ( logline_IP,logline_TIMESTAMP,logline_PAGE,logline_STATUS,logline_SIZE) )
 
# ('163.172.65.184', '24/Mar/2017:21:40:44',  'GET /calendar.php?c=1&week=1396137600 HTTP/1.1', '404', '10120')
def func_01_uniqClientAddress():
    uniqIpList = []
    for logTuple in parserList:
        clientAddress = logTuple[0]
        if clientAddress not in uniqIpList:
            uniqIpList.append(clientAddress)
    for ip in uniqIpList:
        print(ip)


# ('163.172.65.184', '24/Mar/2017:21:40:44',  'GET /calendar.php?c=1&week=1396137600 HTTP/1.1', '404', '10120')
def func_02_totalHitFromOneIp():
    uniqIpList = []
    for logTuple in parserList:
        clientAddress = logTuple[0]
        uniqIpList.append(clientAddress)
    
    counter = collections.Counter()
    counter.update(uniqIpList)    
    for ip,count in sorted(counter.items(),key=lambda t: t[1])[-10:] :
        print('{:<16}{:^3}{}'.format(ip,':',count))

# ('163.172.65.184', '24/Mar/2017:21:40:44',  'GET /calendar.php?c=1&week=1396137600 HTTP/1.1', '404', '10120')
def func_03_totalStatusPerIp(status):
    statusCounter = {}
    for logTuple in parserList:
        clientAddress = logTuple[0]
        clientStatus = logTuple[3]
        if clientStatus == status:
            if clientAddress not in statusCounter:
                statusCounter[clientAddress] = 1
            else:
                statusCounter[clientAddress] += 1
    for ip,count in sorted(statusCounter.items(),key=lambda t: t[1])[-10:] :
        print('{:<16}{:^3}{}'.format(ip,':',count))

# ('163.172.65.184', '24/Mar/2017:21:40:44',  'GET /calendar.php?c=1&week=1396137600 HTTP/1.1', '404', '10120')
def func_04_totalRequestPerDay():
    dayStatusCounter = {}
    for logTuple in parserList:
        date = logTuple[1][:11]
        if date not in dayStatusCounter:
            dayStatusCounter[date] = 1
        else:
            dayStatusCounter[date] += 1         
    for ip,count in sorted(dayStatusCounter.items(),key=lambda t: t[1]):
        print('{:<16}{:^3}{}'.format(ip,':',count))

# ('163.172.65.184', '24/Mar/2017:21:40:44',  'GET /calendar.php?c=1&week=1396137600 HTTP/1.1', '404', '10120')
def func_05_totalUniqStatusPerDay(status):
    dayStatusCounter = {}
    for logTuple in parserList:
        clientStatus = logTuple[3]
        date = logTuple[1][:11]
        if clientStatus == status:
            if date not in dayStatusCounter:
                dayStatusCounter[date] = 1
            else:
                dayStatusCounter[date] += 1         
    for ip,count in sorted(dayStatusCounter.items(),key=lambda t: t[1]):
        print('{:<16}{:^3}{}'.format(ip,':',count))

def func_06_dataUsagePerDay():
    dataUsageDict = {}
    for logTuple in parserList:
        date = logTuple[1][:11]
        data = logTuple[4]
        if date not in dataUsageDict:
            dataUsageDict[date] = 0
            if data.isdigit():
                dataUsageDict[date] =  dataUsageDict[date] + int(data)
        else:
             if data.isdigit():
                dataUsageDict[date] = dataUsageDict[date] + int(data)          
    for date,totalsize in sorted(dataUsageDict.items(),key=lambda t: t[1]):
        print('{:<16}{:^3}{}'.format(date,':',totalsize))                  

ipDataUsageDict = {}
def func_07_ipDataUsagePerDay():    
    for logTuple in parserList:
        ip      = logTuple[0]
        date = logTuple[1][:11]
        data = logTuple[4]
        if date not in ipDataUsageDict:
            ipDataUsageDict[date] = {}
            if ip not in ipDataUsageDict[date]:
                ipDataUsageDict[date][ip] = 0
                if data.isdigit():
                    ipDataUsageDict[date][ip] += int(data)            
        else:
            if ip not in ipDataUsageDict[date]:
                ipDataUsageDict[date][ip] = 0
                if data.isdigit():
                    ipDataUsageDict[date][ip] += int(data)
            else:
                if data.isdigit():
                    ipDataUsageDict[date][ip] += int(data)
                
    for date,ipDataDict in ipDataUsageDict.items():   
            print(date)                 
            for  ip,data in sorted(ipDataDict.items() , key=lambda t : t[1])[-5:]:
                print('\t','{:<16}{:^3}{}'.format(ip,':',data))   

# ('163.172.65.184', '24/Mar/2017:21:40:44',  'GET /calendar.php?c=1&week=1396137600 HTTP/1.1', '404', '10120')
def func_08_perUrlCount(rank):
    urlDict = {}
    for logTuple in parserList:
        url = logTuple[2]
        if  url not in urlDict:
            urlDict[url] = 1
        else:
            urlDict[url] += 1

    for url , count in  sorted(urlDict.items() , key=lambda t : t[1])[-int(rank):]:
        print('{:<7}{:^3}{}'.format(count,':',url))
     

# ('163.172.65.184', '24/Mar/2017:21:40:44',  'GET /calendar.php?c=1&week=1396137600 HTTP/1.1', '404', '10120')


def func_09_urlToperPerDay(rank):
    dayUrlDict = {}    
    for logTuple in parserList:
        date = logTuple[1][:11]
        url    = logTuple[2]

        if date not in dayUrlDict :
            dayUrlDict [date] = {}
            if url not in dayUrlDict[date]:
                dayUrlDict [date][url]  = 1            
        else:
            if url not in dayUrlDict[date]:
                dayUrlDict [date][url] = 1
            else:
                dayUrlDict [date][url] += 1
                
    for date,urlCountDict in dayUrlDict.items():  
            print('') 
            print(date) 
            print('')                
            for  url,count in sorted(urlCountDict.items() , key=lambda t : t[1])[-int(rank):]:
                print('{:<7}{:^3}{}'.format(count,':',url))  


#func_01_uniqClientAddress()
#func_02_totalHitFromOneIp()
#func_03_totalStatusPerIp('301')
#func_04_totalRequestPerDay()
#func_05_totalUniqStatusPerDay('301')
#func_06_dataUsagePerDay()
#func_07_ipDataUsagePerDay()
#func_08_perUrlCount(5)
func_09_urlToperPerDay(3)
