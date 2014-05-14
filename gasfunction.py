'''
    Independent text-based prototype
    4/30/14
    Jungho Lee
'''
import urllib.request
import json
import time
from gasstation import *

# return user input
def userInput():
    zipInput = input("Enter zip code: ")
    return zipInput

# takes zip code, return json string
def readURL(zipCode):
    try:
        data = urllib.request.urlopen('http://www.mshd.net/api/gasprices/'+str(zipCode)).read().decode()
        if (len(data)<20):
            return "No Data"
        else:
            return data
    except urllib.error.URLError:
        return "Internet Connection Error"

# takes json string, return station list
def jsonHandler(data):
    stationList=[]
    if data != "No Data":
        obj = json.loads(data)
        item = obj['item']
        for i in range(5):
            it=item[i]
            station = Station()
            station.setBrand(it['brand'])
            station.setDistance(it['distance'])
            station.setAddress(it['address'])
            station.setDataTime(int(round((time.time()-it['pupdate'])/3600)))
            station.setRegular(it['regular'])
            station.setPlus(it['plus'])
            station.setPremium(it['premium'])
            station.setDiesel(it['diesel'])
            #station.setImg(it['img'])
            station.setImg(it['img'].replace('\\',''))

            stationList.append(station)
            
    return stationList

# sorting key
def getKeyRegular(station):
    return station.getRegular()

def getKeyPlus(station):
    return station.getPlus()

def getKeyPremium(station):
    return station.getPremium()

def getKeyDiesel(station):
    return station.getDiesel()

# test
def getTest():
    txt=''
    data = jsonHandler(readURL(userInput()))
    #print(sorted(data, key=getKeyRegular))
    #print(sorted(data, key=getKeyPlus))
    #print(sorted(data, key=getKeyPremium))
    #print(sorted(data, key=getKeyDiesel))
    for i in sorted(data, key=getKeyDiesel):
        txt+=i.getBrand()+i.getAddress()+i.getDistance()+"\n"
    print(txt)

def getResult(zipCode):
    urlData = readURL(zipCode)
    data=[]
    if urlData == "Internet Connection Error":
        print(urlData)
    else:
        data = jsonHandler(urlData)
    
    for i in data:
        print(i.getBrand()+" "+i.getAddress())

getResult(userInput())
