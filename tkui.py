from Tkinter import *
from PIL import Image,ImageTk
import tkMessageBox
import pcg
import render
import ttk, threading

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.mapWidth = 256
        self.mapHeight = 256
        
        
        self.widthLabel = Label(text = "Width")
        self.heightLabel = Label(text = "Height")
        self.widthBox = Spinbox(from_=1,to=1024)
        self.heightBox = Spinbox(from_=1,to=1024)

        self.detailLabel = Label(text="Detail")
        self.detailBox = Spinbox(from_=1,to=1024)

        self.renderButton = Button(text="Show Map",command=self.renderButtonClick)

        self.setMapSize(self.mapWidth,self.mapHeight)
        
        self.widthLabel.pack(side="top")
        self.widthBox.pack(side="top")
        self.heightLabel.pack(side="top")
        self.heightBox.pack(side="top")
        self.detailLabel.pack(side="top")
        self.detailBox.pack(side="top")
        self.renderButton.pack(side="bottom")
    def setMapSize(self,width,height):
        self.mapImg = Image.new("RGB",(width,height),"black")
        self.mapPixels = self.mapImg.load()
        self.mapPhotoImg = ImageTk.PhotoImage(self.mapImg)
        self.mapView = Label(image=self.mapPhotoImg)
        self.mapView.image = self.mapPhotoImg
        self.mapView.pack(side="left")
        
    def generateMap(self):
        #Create ProgressBar

        #Create new thread for map generation
        mapArgs = (self.mapWidth,self.mapHeight,self.detailLevel,(64.0,2.0,0.5,4),"HERMITE",128,500,2434,4567546,23452345,345786)
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
            tkMessageBox.showwarning("","Invalid Width or Height Value")
            return True

        if detail > 1024:
            detail = 1024
            self.detailBox.delete(0,"end")
            self.detailBox.insert(0,detail)
        if detail <1:
            detail = 1
            self.detailBox.delete(0,"end")
            self.detailBox.insert(0,detail)
        self.detailLevel = detail
            
    def renderButtonClick(self):
        #Retrieve/Validate mapWidth/MapHeight
        if self.getMapRes():
            return

        #Retrieve/Validate detail-level
        if self.getDetailLevel():
            return
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
        self.mapView.pack(side="bottom")

        
        

root = Tk()
root.resizable(width =False,height=False)
app = App(root)
root.mainloop()

