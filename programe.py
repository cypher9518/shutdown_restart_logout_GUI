from tkinter import *
from tkinter import filedialog
import os   

def shutdown():
    time = srlEntry.get()
    x = "\"shutdown /s /t " + time + "\""
    a = os.system(x)
    return a
def restart():
    time = srlEntry.get()
    y = "\"shutdown /r /t " + time + "\""
    b = os.system(y)
    return b
def logout():
    time = srlEntry.get()
    z = "\"shutdown /l /t " + time + "\""
    c = os.system(z)
    return c

#Devloped by Himanshu singh
master = Tk()
master.title("CYP")
master.geometry("230x230")
master.columnconfigure(0,weight = 1)

master.configure(bg = "cadetblue1")

ytdLabel = Label(master,text = "Enter Time in second", bg="olivedrab1", font = ("jost",15))                                #creating a text    
ytdLabel.grid()

srlEntryVar = StringVar()                                                                                                  #creating a text box
srlEntry = Entry(master, width = 25, textvariable = srlEntryVar)
srlEntry.grid()

developerLabel  = Label(master,text = "Choose what you want !!", bg="darkolivegreen1", font = ("jost",8))                  #creating another text    
developerLabel.grid()


Button(master, text = "Shutdown", command = shutdown).place(x = 85, y = 85)
Button(master, text = "Restart", command = restart).place(x = 94, y = 115)
Button(master, text = "Log Out", command = logout).place(x = 90, y = 145)

mainloop()
