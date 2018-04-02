from tkinter import *
from tkinter import messagebox
from datetime import datetime ,timedelta
import subprocess

time = 60 #temprory time changes on calling getTime() function

def shutdown():
    
    if getTime() == 'dontOperate':
        return
    elif getTime() == 'shutdown_now':
        l2.config(text='Your Computer Will shutdown now!')
 
    subprocess.call(["shutdown", "-s","-f" ,"-t", "{}".format(time*60)])
    dt = computer_shutdown_on(time)
    
    if getTime() != 'shutdown_now':
        Time_Of_Shutdown_label('shutdown',dt)

    
def restart():
    
    if getTime() == 'dontOperate':
        return
    elif getTime() == 'shutdown_now':
        l2.config(text='Your Computer Will restart now!')
    
    subprocess.call(["shutdown", "-r", "-t", "{}".format(time*60)])
    dt = computer_shutdown_on(time)

    if getTime() != 'shutdown_now':
        Time_Of_Shutdown_label('restart',dt)

    
def abort():
    
    subprocess.call(["shutdown", "-a"])
    l2.config(text='User aborted the operation')


def errors(msg):
    
    messagebox.showerror('Error','{}'.format(msg))
    entry.delete(0,END)


def getTime():
    
    time_from_entry_box=entry.get()
    try:
        time=int(time_from_entry_box)
    except:
        messagebox.showerror('Error','Please, enter an integer!')
        entry.delete(0,END)
        return 'dontOperate'
    
    if time > 60*60*24*30:
        errors('Sorry the program don\'t support more than 30 days')
        return 'dontOperate'
    elif time == 0:
        return 'shutdown_now'


def Time_Of_Shutdown_label(operation,t):
    
    if entry.get() == '':
        return
    else:
        l2.config(text='Your Computer Will {} on: {}'.format(operation,t))
        entry.delete(0,END)
        return


def HourMinuteSecond(t):
    
    '''this function return time enterd into tuple
    contianing time in secs,mins,hour and day '''
    mins, secs = divmod(t, 60)                                                
    hour, mins = divmod(mins,60)                                             
    day, hour = divmod(hour,24)
    timer = (secs,mins,hour,day) #Notice the order of the tuple  
    return timer


def computer_shutdown_on(t):
    
    '''return the time which the computer will shutdown on'''                                                                  
    ET = HourMinuteSecond(t) #ET is Entered Time                               
    now = datetime.now()                                                      
    tdelta = timedelta(days=ET[3],hours=ET[2],minutes=ET[1],seconds=ET[0])
    final = tdelta + now
    return final.strftime('%Y-%m-%d %H:%M:%S') 


def Exit():
    
    msg=messagebox.askyesno('Exit','Are you sure you want exit?')
    if msg is True:
        root.destroy()

  
root = Tk()
root.title('Shutdown')
root.minsize(330,155)
root.maxsize(330,155)

b1 =Button(root,text='shutdown after:',
           fg='red', bg ='white',command =shutdown)
b1.grid(row=0, column=0,sticky=W+E+N+S,
        padx=5, pady=3)


b2 =Button(root,text='restart after:',
           fg='blue',bg ='white',command =restart)
b2.grid(row=1, column=0,sticky=W+E+N+S,
        padx=5, pady=3)


b3 =Button(root,text='abort:',fg='green',
           bg ='white',command =abort)
b3.grid(row=2, column=0,sticky=W+E+N+S,
        padx=5, pady=3)


b4 =Button(root,text='Exit',fg='purple',
           bg ='white',command =Exit)
b4.grid(row=3, column=0,sticky=W+E+N+S,
        padx=5, pady=3)


entry=Entry(root,width=10)
entry.grid(row=1, column=3,padx=5,
           pady=5,rowspan=2)

l1= Label(root,
text='Enter The Time In Minute: \nNote: " 0 " means now.')
l1.grid(row=1, column=2,rowspan=2)


l2=Label(root,text='Enter Time!',
         relief=GROOVE)
l2.grid(row=4, column=0,padx=5, pady=5,sticky=S,
        columnspan=4)

root.mainloop()
