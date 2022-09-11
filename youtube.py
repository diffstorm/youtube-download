import os
from pytube import YouTube
from tkinter import *

tfont = "verdana 15 bold"
userdir = os.path.join(os.path.join(os.environ['USERPROFILE']))
targetdir = userdir + '\\Desktop'

root = Tk()
root.geometry("320x170")
root.resizable(0,0)
root.title("Youtube Video Downloader")

link = StringVar()
Label(root,text="Video Link:", font=tfont).place(x=10,y=20)
Entry(root,width=50,textvariable=link).place(x=10,y=50)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download(targetdir)
    Label(root,text="Done!",font=tfont).place(x=10,y=130)
    
Button(root,text="Download",font=tfont,padx=2,command=Downloader).place(x=10,y=80)

root.mainloop()
