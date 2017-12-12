from tkinter import *
from tkinter import messagebox
import subprocess

time=60

def shutdown(event):
    global time
    if getTime() == 1:
        return
    subprocess.call(["shutdown", "-s","-f" ,"-t", "{}".format(time*60)])
    Time_Of_Shutdown('shutdown')
    
def restart(event):
    global time
    if getTime() == 1:
        return
    subprocess.call(["shutdown", "-r", "-t", "{}".format(time*60)])
    Time_Of_Shutdown('restart')
    
def abort(event):
    subprocess.call(["shutdown", "-a"])
    l2.config(text='User aborted the operation')
    
def getTime():
    global time
    ttext=text.get()
    try:
        time=int(ttext)
    except:
        messagebox.showerror('Error','Please, enter an integer!')
        entry.delete(0,END)
        return 1

def Time_Of_Shutdown(operation):
    if entry.get() == '':
        return
    else:
        l2.config(text='Your Computer Will {} after: {} MIN'.format(operation,time))
        entry.delete(0,END)
        return

def Exit(event):
    msg=messagebox.askyesno('Exit','Are you sure you want exit?')
    if msg is True:
        root.destroy()
  
root = Tk()
root.title('Shutdown')

text=StringVar()

f1 =Frame(root,width=200,height=200,bg='lightblue')
b1 =Button(f1,text='shutdown after:',fg='red', bg ='white')
b2 =Button(f1,text='restart after:',fg='blue',bg ='white')
b3 =Button(f1,text='abort:',fg='green',bg ='white')
b5 =Button(f1,text='Exit',fg='purple',bg ='white')
entry=Entry(root,width=10,textvariable=text)
l1= Label(root,text='Enter The Time In Minute:')

f2=Frame(root)
l2=Label(f2,text='Enter Time!',relief=GROOVE)

f2.pack(side=BOTTOM)
entry.pack(side=RIGHT)
l1.pack(side=RIGHT)
l2.pack(side=BOTTOM)

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

