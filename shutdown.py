from tkinter import *
from tkinter import messagebox
import subprocess

time=60

def shutdown():
    global time
    if getTime() == 1:
        return
    subprocess.call(["shutdown", "-s","-f" ,"-t", "{}".format(time*60)])
    Time_Of_Shutdown_label('shutdown')
    
def restart():
    global time
    if getTime() == 1:
        return
    subprocess.call(["shutdown", "-r", "-t", "{}".format(time*60)])
    Time_Of_Shutdown_label('restart')
    
def abort():
    subprocess.call(["shutdown", "-a"])
    l2.config(text='User aborted the operation')
    
def getTime():
    global time
    ttext = entry.get()
    try:
        time=int(ttext)
    except:
        messagebox.showerror('Error','Please, enter an integer!')
        entry.delete(0,END)
        return 1

def Time_Of_Shutdown_label(operation):
    if entry.get() == '':
        return
    else:
        l2.config(text='Your Computer Will {} after: {} MIN'.format(operation,time))
        entry.delete(0,END)
        return

def Exit():
    msg=messagebox.askyesno('Exit','Are you sure you want exit?')
    if msg is True:
        root.destroy()
  
root = Tk()
root.title('Shutdown')

f1 =Frame(root,width=200,height=200,bg='lightblue')
b1 =Button(f1,text='shutdown after:',fg='red', bg ='white',command =shutdown)
b2 =Button(f1,text='restart after:',fg='blue',bg ='white',command =restart)
b3 =Button(f1,text='abort:',fg='green',bg ='white',command =abort)
b5 =Button(f1,text='Exit',fg='purple',bg ='white',command =Exit)
entry=Entry(root,width=10)
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

root.mainloop()
