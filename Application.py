'''
	ITP 115
	5/9/14
	Jungho Lee
	Final Project: Gas Station
	Application.py
'''

from tkinter import *
from tkinter import messagebox
import urllib.request
import json
import time
import datetime
from gasstation import *

class Application(Frame):
	# function: __init__
	# input: self, master (root)
	# output: none
	# side-effect: none
	# description: UI initial setup
	def __init__(self, master):
		super().__init__(master)
		self.grid()	# draw frame

		self.sortedList=[]	# sorted list of gas station
		self.strSortBy=''	# string sort option
		
		# -----------------------------GUI-------------------------------------
		self.strSortRadio = StringVar()
		self.strSortRadio.set("regular")	# set initial radio button option to 'regular'
		
		self.strZipCode = StringVar()
		
		self.labelTitle = Label(self, text="Gas Station")	# set label (UI title)
		self.labelTitle.grid(row=0, column=2)
		
		self.labelE = Label(self, text='')	# empty space
		self.labelE.grid(row=1, column=0)

		self.labelZip = Label(self, text="Zip Code : ")	# zip code input label
		self.labelZip.grid(row=2, column=0)

		self.entryZip = Entry(self, textvariable=self.strZipCode)	# zip code entry
		self.entryZip.grid(row=2, column=1)

		self.labelSort = Label(self, text="Sort by : ")	# sort option label
		self.labelSort.grid(row=2, column=2)
		
		self.rdbRegular = Radiobutton(self, text="regular", value="regular", variable=self.strSortRadio)	# sort option: regular
		self.rdbRegular.grid(row=2, column=3)
		self.rdbRegular = Radiobutton(self, text="plus", value="plus", variable=self.strSortRadio)	# sort option: plus
		self.rdbRegular.grid(row=2, column=4)
		self.rdbRegular = Radiobutton(self, text="premium", value="premium", variable=self.strSortRadio)	# sort option: premium
		self.rdbRegular.grid(row=2, column=5)
		self.rdbRegular = Radiobutton(self, text="diesel", value="diesel", variable=self.strSortRadio)	# sort option: diesel
		self.rdbRegular.grid(row=2, column=6)
		self.rdbDistance = Radiobutton(self, text="distance", value="distance", variable=self.strSortRadio)	# sort option: distance
		self.rdbDistance.grid(row=2, column=7)
		
		self.btnSearch = Button(self, text="Search", command=self.searchData)	# search button
		self.btnSearch.grid(row=2, column=8)
		
		self.txtSearchResult = Text(self, width=100, height=30)	# result screen
		self.txtSearchResult.grid(row=3, column=0, columnspan=9)
		
		# page selection
		# initial state is disabled
		# change to normal when the program has valid data
		self.labelPage = Label(self, text="Page : ", state=DISABLED)	# page label
		self.labelPage.grid(row=4, column=1)
		self.btnP1 = Button(self, text="1", state=DISABLED, command=self.page1)	# page 1 button / disabled
		self.btnP1.grid(row=4, column=2)
		self.btnP2 = Button(self, text="2", state=DISABLED, command=self.page2)	# page 2 button / disabled
		self.btnP2.grid(row=4, column=3)
		self.btnP3 = Button(self, text="3", state=DISABLED, command=self.page3)	# page 3 button / disabled
		self.btnP3.grid(row=4, column=4)
		self.btnP4 = Button(self, text="4", state=DISABLED, command=self.page4)	# page 4 button / disabled
		self.btnP4.grid(row=4, column=5)
		self.btnP5 = Button(self, text="5", state=DISABLED, command=self.page5)	# page 5 button / disabled
		self.btnP5.grid(row=4, column=6)
		
		self.btnSave = Button(self, text="Save", state=DISABLED, command=self.saveData)	# save button
		self.btnSave.grid(row=4, column=8)
		# ----------------------------GUI END-------------------------------
		
	# function: readURL
	# input: self
	# output: data decoded to string or error message
	# side-effect: none
	# description: take zip code input and save json string from mshd.net or error message
	def readURL (self):
		try:
			# take data from mshd.net and decode to string
			data = urllib.request.urlopen('http://www.mshd.net/api/gasprices/'+str(self.strZipCode.get())).read().decode()
			if (len(data)<20):	# zip code validation. if zip code input is not right, data from the url should be short
				return "No Data"
			else:	# if data from url is long enough, save the data
				return data
		except urllib.error.URLError:	# bad internet connection exception
			return "Internet Connection Error"

	# function: jsonHandler
	# input: self, dataString
	# output: gas station object list
	# side-effect: none
	# description: convert string data to json, and generate gas station object list
	def jsonHandler(self, dataString):
		stationList=[]
		obj = json.loads(dataString)	# load json object from string
		item = obj['item']	# load json array. assume that an array has 50 json objects
		
		# read json object from json array
		for it in item:
			station = Station()	# create gas station object
			station.setBrand(it['brand'])	# set gas station brand
			station.setDistance(it['distance'])	# set gas station distance by zip code
			station.setAddress(it['address'])	# set gas station address
			# set data time: calculate time difference by subtracting data time stamp from current time stamp. convert sec to hr
			station.setDataTime(int(round((time.time()-it['pupdate'])/3600)))
			station.setRegular(it['regular'])	# set regular gasoline price
			station.setPlus(it['plus'])	#set plus gasoline price
			station.setPremium(it['premium'])	# set premium gasoline price
			station.setDiesel(it['diesel'])	# set diesel price
			#station.setImg(it['img']) # set image url with escape characters
			station.setImg(it['img'].replace('\\',''))	# set image url
			stationList.append(station)	# add gas station object to list
		return stationList
		
	### sorting keys
	# function: getKey
	# input: self, station(gas station object)
	# output: price or distance string
	# side-effect: none
	# description: return sort keys
	def getKeyRegular(self, station):
		return station.getRegular()
	def getKeyPlus(self, station):
		return station.getPlus()
	def getKeyPremium(self, station):
		return station.getPremium()
	def getKeyDiesel(self, station):
		return station.getDiesel()
	def getKeyDistance(self, station):
		return station.getDistance()
				
	# function: sortList
	# input: self, dataList
	# output: none
	# side-effect: none
	# description: sort gas station object as radio button selected
	def sortList(self, dataList):
		if self.strSortBy == "regular":
			self.sortedList = sorted(dataList, key=self.getKeyRegular)	# sort by regular price
		elif self.strSortBy == "plus":
			self.sortedList = sorted(dataList, key=self.getKeyPlus)	# sort by plus price
		elif self.strSortBy == "premium":
			self.sortedList = sorted(dataList, key=self.getKeyPremium)	# sort by premium price
		elif self.strSortBy == "diesel":
			self.sortedList = sorted(dataList, key=self.getKeyDiesel)	# sort by diesel price
		else:
			self.sortedList = sorted(dataList, key=self.getKeyDistance)	# sort by distance

	### button command
	# function: page
	# input: self
	# output: none
	# side-effect: none
	# description: call print function
	def page1(self):
		self.printPage(0)
	def page2(self):
		self.printPage(10)
	def page3(self):
		self.printPage(20)
	def page4(self):
		self.printPage(30)
	def page5(self):
		self.printPage(40)
		
	# function: printPage
	# input: self, start(start item number)
	# output: none
	# side-effect: none
	# description: print gas station objects in sorted list with item index
	def printPage(self, start):
		txt=''
		end=start+10	# 10 items per page
		
		# 10 sorted list items from the start number
		for i in range(start,end):
			txt+="{:2d}. ".format(i+1)	# item index
			txt+=str(self.sortedList[i])	# gas station object in sorted list
			txt+="--------------------------------------------------------------------------------------------"
			if i != end-1:	# if it is not last
				txt+='\n'	# change line
			else:	# if it is last
				txt+="   "+str(int(end/10))	# print page number
		self.txtSearchResult.delete(0.0, END)	# clear page
		self.txtSearchResult.insert(0.0, txt)	# print string
		
	# function: saveData
	# input: self
	# output: none
	# side-effect: none
	# description: append search result to file
	def saveData(self):
		txt=''
		fout = open("record.txt","a")	# open output file
		txt+="Date & Time: "+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')	# current time stamp
		txt+="\tZip Code: "+str(self.strZipCode.get())+"\tSort by: "+self.strSortBy+'\n\n'	# zip code, sort option
		
		# sorted list items
		for i in range(len(self.sortedList)):
			txt+="{:2d}. ".format(i+1)	# item index
			txt+=str(self.sortedList[i])	# gas station object in sorted list
			if i != len(self.sortedList)-1:	# single line except last item
				txt+="--------------------------------------------------------------------------------------------\n"
		# double line for last item
		txt+="=========================================================================================END\n\n"
		print(txt, file=fout)	# print in file
		fout.close()	# close output file
		messagebox.showinfo("Gas Station","Data Saved Successfully!")	# show message box after file output
		
	# function: searchData
	# input: self
	# output: none
	# side-effect: none
	# description: search gas price data and print on UI
	def searchData(self):
		dataString = self.readURL()	# call readURL function
		self.strSortBy = self.strSortRadio.get()	# save sort option.
		if dataString != "No Data" and dataString != "Internet Connection Error":	# if string data is valid
			self.sortList(self.jsonHandler(dataString))	# call sortList function
			self.page1()	# call page1 function
			self.labelPage.config(state=NORMAL)	# enabled
			self.btnP1.config(state=NORMAL)	# enabled
			self.btnP2.config(state=NORMAL)	# enabled
			self.btnP3.config(state=NORMAL)	# enabled
			self.btnP4.config(state=NORMAL)	# enabled
			self.btnP5.config(state=NORMAL)	# enabled
			self.btnSave.config(state=NORMAL)	# enabled
		else:	# if string data is invalid
			self.labelPage.config(state=DISABLED)	# disabled
			self.btnP1.config(state=DISABLED)	# disabled
			self.btnP2.config(state=DISABLED)	# disabled
			self.btnP3.config(state=DISABLED)	# disabled
			self.btnP4.config(state=DISABLED)	# disabled
			self.btnP5.config(state=DISABLED)	# disabled
			self.btnSave.config(state=DISABLED)	# disabled
			self.txtSearchResult.delete(0.0, END)	# clear page
			self.txtSearchResult.insert(0.0, dataString)	# print string error message