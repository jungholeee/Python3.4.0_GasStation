'''
	ITP 115
	5/9/14
	Jungho Lee
	Final Project: Gas Station
	Main.py
'''

from tkinter import *
from Application import *

# function: main
# input: none
# output: none
# side-effect: none
# description: main for the program
def main():
    root = Tk()
    root.title("Gas Station")	# set title
    root.geometry("700x500")	# set size
	
    Application(root)	# pass tk to Application class

    root.mainloop()	# start mainloop
main()
