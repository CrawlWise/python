from tkinter import *
import os
import time
from tkinter import font
from typing import NoReturn
import wmi

btn_state = "DISABLED"
window = Tk() #initializing the window class
window.title("Shutdown Scheduler") #Display the title of my window
window.geometry("350x250") #Set the size of my window
label_top = Label(bg="white",fg="white", width= 100, height=20).pack() #Arranging the content of my windows
#time Text entry value
time_label = Label(text="Enter Time: h for hrs: m for min(5h or 5m)")
time_label.place(x=60, y=5)
time_entry = Entry(window)

#-----------------------------------Defining Functions--------------------------------------------------------
#Getting the value of morning
def schedule():
    """
        Use powershell to schedule the shutdown
    """
    #Setting the timer to either minute or hours
    mylistval = []
    user_input = time_entry.get()
    user_input.lower()
    confirm_user_input = 'h' in user_input
    if confirm_user_input:
        selected = time_entry.get()
        user_time = selected.replace('h','')
        time_call = 60*60*int(user_time)
        timer= str(time_call)
        os.system('shutdown /s /t ' + timer)
        
    else:
        selected = time_entry.get()
        selected = time_entry.get()
        user_time = selected.replace('m','')
        time_call = 60*int(user_time)
        timer= str(time_call)
        os.system('shutdown /s /t ' + timer)

def btn_cancel():
    conn = wmi.WMI() #Establish wmi connection
    for proc in conn.win32_Process(name="python.exe"): #loop through my process and search for python process
        cid = os.getpid() # Get my current python process
        if proc.ProcessId == cid: #Check against the python process i got
            proc.terminate() #Call wmi terminate function to kill application


def reschedule_button():#Function to reschedule
    os.system('shutdown /a')
    schedule()

def changestate(): #Function to enable schedule button
    if var.get() == 1:
        btn_Schedular['state'] = NORMAL
    else:
        btn_Schedular['state'] = DISABLED

#-----------------------------------End of Function Body--------------------------------------------------------

time_entry.place(x=50, y=30, width= 250, height=25)
#Creating Check button strict and Mild
var = IntVar()
strict = Checkbutton(window, text="Set Recurrent Shutdown", variable=var, onvalue=1, offvalue=0, command=changestate)
strict.place(x=130, y=90)
#Creating the schedule button
button_submit = Button(text="Schedule", background="green", fg="white",font=12, command=schedule).place(x=12, y=150)
button_reschedule = Button(text="Reschedule", background="grey", fg="white", font=12, command=reschedule_button).place(x=120, y=150)
close_cancel = Button(text="Close", bg="red",fg="black", font=12, command=btn_cancel).place(x=140, y=198)
btn_Schedular = Button(window, text="Schedule", bg="orange",fg="white",font=12, state=DISABLED)
btn_Schedular.place(x= 250, y=150)
label = Label(window)
label.pack()
window.resizable(False,False)

window.mainloop()