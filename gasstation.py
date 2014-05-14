'''
	ITP 115
	5/9/14
	Jungho Lee
	Final Project: Gas Station
	gasstation.py
'''

class Station(object):
	# function: __init__
	# input: self
	# output: none
	# side-effect: none
	# description: class initialization
    def __init__(self):
        self.__brand = ''	# gas station brand
        self.__distance = 0.0	# distance from zip code input (distance between zip codes)
        self.__address = ''	# gas station address
        self.__dataTime = 0	# data time stamp
        self.__regular = ''	# regular gasoline price
        self.__plus = ''	# plus gasoline price
        self.__premium = ''	# premium gasoline price
        self.__diesel = ''	# diesel price
        self.__img = ''	# brand image url
	
	# function: __str__
	# input: self
	# output: gas station data string
	# side-effect: none
	# description: return formatted string of gas station data
    def __str__(self):
        txt=''
        txt+="{:15s}{:60s}{:.2f} miles\n".format(self.__brand, self.__address, float(self.__distance))
        reg="Regular: {}".format(self.__regular)
        plus="Plus: {}".format(self.__plus)
        pre="Premium: {}".format(self.__premium)
        die="Diesel: {}".format(self.__diesel)
        txt+="\t{:15s}{:15s}{:15s}{:15s}          {}\n".format(reg,plus,pre,die, self.__dataTime)
        return txt
		
	# function: __repr__
	# input: self
	# output: simplified gas station data string for developer
	# side-effect: none
	# description: return simplified gas station data to identify object in the list
    def __repr__(self):
        return '{} {} {} {} {}'.format(self.__brand, self.__regular, self.__plus, self.__premium, self.__diesel)

    ### setters
    def setBrand(self, brand):
        self.__brand = brand

    def setDistance(self, distance):
        self.__distance = distance

    def setAddress(self, address):
        self.__address = address

    def setDataTime(self, dataTime):
        self.__dataTime = str(dataTime)+' hours ago'

    def setRegular(self, regular):
        self.__regular = str(regular)

    def setPlus(self, plus):
        self.__plus = str(plus)

    def setPremium(self, premium):
        self.__premium = str(premium)

    def setDiesel(self, diesel):
        self.__diesel = str(diesel)

    def setImg(self, img):
        self.__img = img

    ### getters
    def getBrand(self):
        return self.__brand

    def getDistance(self):
        return self.__distance

    def getAddress(self):
        return self.__address

    def getDataTime(self):
        return self.__dataTime

    def getRegular(self):
        return self.__regular

    def getPlus(self):
        return self.__plus

    def getPremium(self):
        return self.__premium

    def getDiesel(self):
        return self.__diesel

    def getImg(self):
        return self.__img
