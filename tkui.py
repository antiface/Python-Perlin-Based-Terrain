from Tkinter import *
from PIL import Image,ImageTk
import tkMessageBox
import pcg
import render
import ttk, threading
import random
import filehandling
class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.mapWidth = 256
        self.mapHeight = 256
        
        
        self.widthLabel = Label(text = "Width")
        self.heightLabel = Label(text = "Height")
        self.widthBox = Spinbox(from_=1,to=1024,increment=16)
        self.heightBox = Spinbox(from_=1,to=1024,increment=16)

        self.detailLabel = Label(text="Detail")
        self.detailBox = Spinbox(from_=1,to=4096,increment=16)

        self.frequencyLabel = Label(text="Frequency")
        self.frequencyBox = Spinbox(from_=0,to=16,increment =0.1)

        self.lacunarityLabel = Label(text="Lacunarity")
        self.lacunarityBox = Spinbox(from_=0,to=16,increment =0.1)

        self.persistenceLabel = Label(text="Persistence")
        self.persistenceBox = Spinbox(from_=0,to=16,increment =0.1)

        self.octavesLabel = Label(text="Octaves")
        self.octavesBox = Spinbox(from_=0,to=8,increment =1)

        self.mountainLabel = Label(text="Mountain Level")
        self.mountainBox = Spinbox(from_=0,to=512,increment =1)

        self.seaLabel = Label(text="Sea Level")
        self.seaBox = Spinbox(from_=0,to=512,increment =1)

        self.biomeSeedLabel = Label(text="Biome Seed")
        self.biomeSeedBox = Spinbox(from_=-65535,to=65535,increment =16)

        self.heightSeedLabel = Label(text="HeightMap Seed")
        self.heightSeedBox = Spinbox(from_=-65535,to =65535,increment =16)

        self.tempSeedLabel = Label(text="TemperatureMap Seed")
        self.tempSeedBox = Spinbox(from_=-65535,to=65535,increment =16)

        self.moistureSeedLabel = Label(text="MoistureMap Seed")
        self.moistureSeedBox = Spinbox(from_=-65535,to=65535,increment =16)

        self.interpolationLabel = Label(text="Interpolation Mode")
        self.interpolationBox = Spinbox(values = ("HERMITE","LINEAR","COSINE") ,state="readonly")

        self.defaultButton = Button(text="Defaults",command=self.defaultButtonClick)
        
        self.renderButton = Button(text="Show Map",command=self.renderButtonClick)

        self.saveButton = Button(text="Save Image",command=self.saveImage)
        self.setMapSize(self.mapWidth,self.mapHeight)
        
        self.widthLabel.pack(side="top")
        self.widthBox.pack(side="top")
        self.heightLabel.pack(side="top")
        self.heightBox.pack(side="top")
        self.detailLabel.pack(side="top")
        self.detailBox.pack(side="top")
        self.frequencyLabel.pack(side="top")
        self.frequencyBox.pack(side="top")
        
        self.lacunarityLabel.pack(side="top")
        self.lacunarityBox.pack(side="top")
        
        self.persistenceLabel.pack(side="top")
        self.persistenceBox.pack(side="top")
        
        self.octavesLabel.pack(side="top")
        self.octavesBox.pack(side="top")
        
        self.mountainLabel.pack(side="top")
        self.mountainBox.pack(side="top")
        
        self.seaLabel.pack(side="top")
        self.seaBox.pack(side="top")

        self.interpolationLabel.pack(side="top")
        self.interpolationBox.pack(side="top")
        
        self.biomeSeedLabel.pack(side="top")
        self.biomeSeedBox.pack(side="top")
        
        self.heightSeedLabel.pack(side="top")
        self.heightSeedBox.pack(side="top")
        
        self.tempSeedLabel.pack(side="top")
        self.tempSeedBox.pack(side="top")
        
        self.moistureSeedLabel.pack(side="top")
        self.moistureSeedBox.pack(side="top")

        self.defaultButton.pack(side="top")

        self.renderButton.pack(side="top")

        self.saveButton.pack(side="top")
        self.defaultButtonClick()
    def saveImage(self):
        filehandling.saveImage(self.mapImg)
    def setMapSize(self,width,height):
        self.mapImg = Image.new("RGB",(width,height),"black")
        self.mapPixels = self.mapImg.load()
        self.mapPhotoImg = ImageTk.PhotoImage(self.mapImg)
        self.mapView = Label(image=self.mapPhotoImg)
        self.mapView.image = self.mapPhotoImg
        self.mapView.pack(side="right")
        
    def generateMap(self):
        #Create ProgressBar

        #Create new thread for map generation
        mapArgs = (self.mapWidth,self.mapHeight,self.detailLevel,(self.frequency,self.lacunarity,self.persistence,self.octaves),self.interpolationMode,self.seaLevel,self.mountainLevel,self.biomeSeed,self.heightSeed,self.tempSeed,self.moistureSeed)
        
        biomeMap = pcg.generateMap(*mapArgs)
        
        
        for i in xrange(self.mapWidth):
            for j in xrange(self.mapHeight):
                colour = render.biomeColour(biomeMap[i][j])
                
                self.mapPixels[i,j] = colour
    def getMapRes(self):
        width = self.widthBox.get()
        height = self.heightBox.get()
        try:
            width = int(width)
            height = int(height)
        except:
            tkMessageBox.showwarning("","Invalid Width or Height Value")
            return True
        
        if width>1024:
            width = 1024
            self.widthBox.delete(0,"end")
            self.widthBox.insert(0,width)
        if width <1:
            width = 1
            self.widthBox.delete(0,"end")
            self.widthBox.insert(0,width)
        if height>1024:
            height = 1024
            self.heightBox.delete(0,"end")
            self.heightBox.insert(0,height)
        if height <1:
            height = 1
            self.heightBox.delete(0,"end")
            self.heightBox.insert(0,height)
        self.mapWidth = width
        self.mapHeight = height
    def getDetailLevel(self):
        detail = self.detailBox.get()

        try:
            detail = int(detail)
        except:
            tkMessageBox.showwarning("","Invalid Detail Value")
            return True

        if detail > 4096:
            detail = 4096
            self.detailBox.delete(0,"end")
            self.detailBox.insert(0,detail)
        if detail <1:
            detail = 1
            self.detailBox.delete(0,"end")
            self.detailBox.insert(0,detail)
        self.detailLevel = detail
    def getFrequency(self):
        frequency = self.frequencyBox.get()

        try:
            frequency = float(frequency)
        except:
            tkMessageBox.showwarning("","Invalid Frequency Value")
            return True

        if frequency > 16:
            frequency = 16
            self.frequencyBox.delete(0,"end")
            self.frequencyBox.insert(0,frequency)
        if frequency <= 0:
            frequency = 0.1
            self.frequencyBox.delete(0,"end")
            self.frequencyBox.insert(0,frequency)
        self.frequency = frequency
    def defaultButtonClick(self):
        self.detailBox.delete(0,"end")
        self.detailBox.insert(0,64)

        self.widthBox.delete(0,"end")
        self.widthBox.insert(0,256)

        self.heightBox.delete(0,"end")
        self.heightBox.insert(0,256)

        self.frequencyBox.delete(0,"end")
        self.frequencyBox.insert(0,16)

        self.lacunarityBox.delete(0,"end")
        self.lacunarityBox.insert(0,2)

        self.persistenceBox.delete(0,"end")
        self.persistenceBox.insert(0,0.5)

        self.octavesBox.delete(0,"end")
        self.octavesBox.insert(0,2)

        self.mountainBox.delete(0,"end")
        self.mountainBox.insert(0,250)

        self.seaBox.delete(0,"end")
        self.seaBox.insert(0,128)

        self.interpolationBox.delete(0,"end")
        self.interpolationBox.insert(0,"HERMITE")

        self.biomeSeedBox.delete(0,"end")
        self.biomeSeedBox.insert(0,int(random.random()*65536))

        self.heightSeedBox.delete(0,"end")
        self.heightSeedBox.insert(0,int(random.random()*65536))

        self.tempSeedBox.delete(0,"end")
        self.tempSeedBox.insert(0,int(random.random()*65536))

        self.moistureSeedBox.delete(0,"end")
        self.moistureSeedBox.insert(0,int(random.random()*65536))
    def renderButtonClick(self):
        #Retrieve/Validate mapWidth/MapHeight
        if self.getMapRes():
            return

        #Retrieve/Validate detail-level
        if self.getDetailLevel():
            return

        #Retrive/Validate frequency
        if self.getFrequency():
            return

        #Retrieve Lacunarity
        self.lacunarity = float(self.lacunarityBox.get())
        #Retrieve Persistence
        self.persistence = float(self.persistenceBox.get())
        #Retrieve Octaves
        self.octaves = int(self.octavesBox.get())
        #Retrieve Mountain/Sea Level
        self.mountainLevel = int(self.mountainBox.get())
        self.seaLevel = int(self.seaBox.get())

        #Retrieve Seeds
        self.biomeSeed = float(self.biomeSeedBox.get())
        self.heightSeed = float(self.heightSeedBox.get())
        self.tempSeed = float(self.tempSeedBox.get())
        self.moistureSeed = float(self.moistureSeedBox.get())

        #Retrive Interpolation Mode
        self.interpolationMode = str(self.interpolationBox.get())
        #Clear Map
        self.mapView.destroy()
        #Initialise Image
        self.mapImg = Image.new("RGB",(self.mapWidth,self.mapHeight),"black")
        self.mapPixels = self.mapImg.load()
        #Render Map
        self.generateMap()
        #Initialise Map Display
        self.mapPhotoImg = ImageTk.PhotoImage(self.mapImg)
        self.mapView = Label(image=self.mapPhotoImg)
        self.mapView.image = self.mapPhotoImg
        self.mapView.pack(side="right")

        
        

root = Tk()
root.resizable(width =False,height=False)
app = App(root)
root.mainloop()

