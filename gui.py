from metainfo import metainfo
from exifupdater import exifupdater
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os

full = tk.Tk()
full.title( 'Metainfo' )
full.geometry("600x400")
frame = Frame(full)  
frame.pack()  
name = Label(full, text = "Enter Image Directory").place(x = 5,y = 50)
Message(full,bg='white',width=500,padx=280,pady=5).place(x=10,y=15)
# Message(full,width= 500,bg='white',padx=140,pady=160).place(x=300,y=30)
# file = None
def askDir():
    global file
    global allfiles
    global image_dir
    file = filedialog.askdirectory()
    try:
    # Change the current working Directory    
        os.chdir(file)
        print("Directory changed")
    except OSError:
        print("Can't change the Current Working Directory") 
    allfiles , image_dir = metainfo(file)
    print(allfiles)
    print(image_dir)
    # print(allfiles,image_dir)
    # print ('\n\n\n','Images:', allfiles,'\n\n\n','Meta Info:',image_dir)
    Message(full,text = file,bg='white',width=750,padx=5,pady=5).place(x=10,y=15)
    for item in allfiles:
        lbox.insert(tk.END, item)


scrollbar = tk.Scrollbar(full, orient= 'vertical')
scrollbar.pack(side= RIGHT, fill= BOTH)
lbox = Listbox(full,height=20,width=46,bg='white',yscrollcommand = scrollbar.set)
lbox.place(x =294, y = 50)
scrollbar.config(command= lbox.yview)

def exif():
    exifupdater(allfiles,image_dir)
    Message(full, text = "Successful!",width= 300).place(x=140,y=90)

Button(full,text = "Browse",command = lambda:askDir(),padx=50).place(x = 140, y = 50) 
Button(full,text = "Start",command = lambda:exif(),padx=29).place(x = 140, y = 80) 




# allfiles , image_dir = metainfo(file)

# exifupdater(allfiles,image_dir)
full.mainloop()  


