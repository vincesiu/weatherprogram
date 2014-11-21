# Vincent Siu
# 20140623
# GUI module

from Tkinter import *
import weather_m_APIwork    
import tkMessageBox

class WeatherApp:
   def __init__(self, parent=0):
   	  #setting up the initial frames
      self.mainWindow = Frame(parent,width = 300, height = 100)
      self.mainWindow.pack_propagate(0)

      self.top = Frame(self.mainWindow)
      self.bottom = Frame(self.mainWindow, relief = "sunken", border = 1)

      self.top.pack(side = "top", fill = X, expand = 1)
      self.bottom.pack(side = "top")


      # Create the entry region
      self.label1 = Label(self.top, text = "Zip: ")
      self.entry = Entry(self.top)

      self.label1.pack(side = "left")
      self.entry.pack(side = "left", fill=X, expand = 1)
      

      # now add the 2 buttons, use a grooved effect 
      bEnter = Button(self.bottom, text="Enter", width=8, height=1, command=self.bEnterPress)
      bQuit = Button(self.bottom, text="Quit", width=8, height=1, command=self.mainWindow.quit)
      bEnter.pack(side="left", padx=15, pady=1)
      bQuit.pack(side="left", padx=15, pady=1)

      self.mainWindow.pack(side = "top", anchor = 'nw')#, fill = X, expand = 1

      # set the title
      self.mainWindow.master.title("The Weather Box")
   


   def retrieve_input(self):
   		return self.entry.get()

   def checkValidZip(self, zip):
   		if len(zip) != 5:
   			return 0
   		else:
   			return 1

   def errorBox(self, errorCode):
   		errorText = "You just broke my code. Unknown bug D:"
   		if errorCode == 1:
   			errorText = "Invalid zip provided, \n please try again."
   		if errorCode == 2:
   			errorText = "Please provide a 5 digit zip code, \n and try again."
   		tkMessageBox.showinfo("Error: Code %s!!!" % errorCode, errorText)

   def bEnterPress(self):
   		zip = self.retrieve_input()
   		if self.checkValidZip(zip) == 0:
   			self.errorBox(2)
   			return
   		wList = weather_m_APIwork.getCurrentWeather(zip)
   		if wList[0] == -1:
   			self.errorBox(1)
   		else:
   			tkMessageBox.showinfo(	"Weather", "Currently in %s:\n%s degrees Celcius \n%s degrees Farenheit\nConditions: %s" % (wList[2], wList[0], wList[1], wList[3]))

      
app = WeatherApp()
app.mainWindow.mainloop()