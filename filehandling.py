from PIL import Image,ImageTk
import tkFileDialog

def saveImage(imageData):
    print imageData
    location = tkFileDialog.asksaveasfilename(defaultextension="bmp",filetypes=[("BMP","*.bmp")])
    ftype = location[-3:]
    print ftype
    imageFile =open(location,"w")
    imageData.format = ftype
    imageData.save(imageFile,format=location[-3:])
    imageFile.close()
