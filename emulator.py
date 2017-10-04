#last edited on 25.09.2017
#Creator : Prashant

from tkinter import *
import os

root=Tk()
root.title("PyTerm v1.0")

root.geometry("1000x700")

root.resizable(width=False,height=False)

fr_tr=Frame(root,width="700",height="400")
fr_tr.grid(row=0,column=0,columnspan=3,rowspan=2)

fr_output=Frame(root,width="300",height="400")
fr_output.grid(row=0,sticky='s',column=3,rowspan=2)

fr_man=Frame(root,width="1000",height="300")
fr_man.grid(row=2,column=0,sticky='nsew',columnspan=4)


fileList=Listbox(fr_output,width=300,height=33)
fileList.grid(row=0,column=3,rowspan=2,sticky="s")
fileList.config(border=2,relief='sunken')

cwd=os.getcwd()

x=0
color=["gray","white"]
for f in os.listdir(cwd):
    fileList.insert(END,f)
    fileList.itemconfigure(END,background=color[x])
    x=1-x

man_lab=Label(fr_man,text="This will show help for commands after the terminal is ready.")
man_lab.grid(row=2,sticky='nsew',column=0,columnspan=4)

wid=fr_tr.winfo_id()

os.system("xterm -into %d -fa 'Courier' -fs 12 -geometry 80x24  &" % wid)


root.mainloop()
