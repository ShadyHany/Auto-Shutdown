from tkinter import *
import subprocess

time=60

def shutdown(event):
    getTime()
    global time
    subprocess.call(["shutdown", "-s","-f" ,"-t", "{}".format(time)])
    
def restart(event):
    getTime()
    global time 
    subprocess.call(["shutdown", "-r", "-t", "{}".format(time)])
    
def abort(event):
    subprocess.call(["shutdown", "-a"])

def getTime():
    global time
    ttext=text.get()
    time=int(ttext)
    return

def Exit(event):
    exit()
    
    
root = Tk()
root.title('Shutdown')

text=StringVar()

f1 =Frame(root,width=200,height=200,bg='lightblue')
f2 =Frame(root,width=200,height=130,bg='lightblue')
b1 =Button(f1,text='shutdown after:',fg='red', bg ='white')
b2 =Button(f1,text='restart after:',fg='blue',bg ='white')
b3 =Button(f1,text='abort:',fg='green',bg ='white')
b5 =Button(f1,text='Exit',fg='purple',bg ='white')
entry=Entry(f2,width=10,textvariable=text)
l1= Label(f2,text='Enter The Time In Minute:',bg='lightblue')

l1.grid(row = 0, column=0,pady=18)
entry.grid(padx=50,pady=28)
f2.pack(side=RIGHT)
f1.pack(fill=BOTH)
b1.pack(fill=BOTH)
b2.pack(fill=BOTH)
b3.pack(fill=BOTH)
b5.pack(fill=BOTH)

b1.bind("<Button-1>",shutdown)
b2.bind("<Button-1>",restart)
b3.bind("<Button-1>",abort)
b5.bind("<Button-1>",Exit)

root.mainloop()

