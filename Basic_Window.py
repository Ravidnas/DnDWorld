from tkinter import *
from PIL import Image, ImageTk


import Map_Build
import Image_Builder

def faggot():
    print("Douche")

root = Tk()    #Constructor For a BASIC Window
root.geometry(Map_Build.MapAttributes.XYsize)


Menu_Bar = Menu(root)
BM = Menu(Menu_Bar, tearoff=0)
Menu_Bar.add_cascade(label="Tools", menu=BM)
BM.add_command(label="BuildStuff", command=Image_Builder.build())
BM.add_separator()


MapFrame = Frame(root)
duh = Button(MapFrame, text="doucheee", command=faggot())
MapFrame.pack()
map_base = Canvas(root)
img =ImageTk.PhotoImage(Image.open("Map.bmp"))
panel = Label(MapFrame, image= img)
panel.pack(side = "top", fill = "both", expand = "yes")
MapFrame.pack(side=TOP)


print("douche")
#root.config(menu=Menu_Bar)
root.mainloop()                              #Keeps it on the screen




