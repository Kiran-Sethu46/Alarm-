from datetime import date
from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        Current_time = datetime.datetime.now()
        now = Current_time.strftime("%H:%M:%S")
        date = Current_time.strftime("%d/%m/%Y")
        print("set the date and time",date)
        print(now)
        if now == set_alarm_timer:
           print("Time to wake up") 
           winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
           break 
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
clock =Tk()
clock.title("Alarm by ks")
clock.geometry("400x200")
clock.configure(bg="Black")

time_format = Label(clock, text ="Enter the time in 24 hours Format !", fg= "black", bg = "Grey", font="Arial" ).place(x=60,y = 120)
addTime = Label(clock,text="Hour Min Sec", font= 60).place(x=150)
setYourAlarm = Label(clock,text="When to wake you up", fg="Black", relief ="solid", font=("helevetica",10, "bold")).place(x=0, y=30)

hour = StringVar
min =  StringVar
sec =  StringVar

hourTime = Entry(clock, textvariable=hour, bg="Dark Grey",
                 width=15).place(x=150, y=30)
minTime = Entry(clock, textvariable=min, bg="Dark Grey",
                width=15).place(x=200, y=30)
secTime = Entry(clock, textvariable=sec, bg="Dark Grey",
                width=15).place(x=250, y=30)

submit = Button(clock, text="Set Alarm", fg="Black",bg="Grey", width=20,
                command=actual_time).place(x=110, y=70)
clock.mainloop()
