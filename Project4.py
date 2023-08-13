# Tkinter is the standard GUI library for Python.
# Python when combined with Tkinter provides a fast and easy way to create GUI applications.
# Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

# App for shutdown and restart
from tkinter import *
import os

#Python has a built-in os module with methods for interacting with the operating system,
# like creating files and directories, management of files and directories, input, output,
# environment variables, process management, etc.
# The os module has the following set of methods and constants.

def restart():
    os.system("shutdown /r /t 1")
def restart_time():
    os.system("shutdown /r /t 20")
def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")


st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="orange")

r_button = Button(st, text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button = Button(st, text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button = Button(st, text="Log-Out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=150,y=270,height=50,width=200)

st_button = Button(st, text="ShutDown",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
st_button.place(x=150,y=370,height=50,width=200)


st.mainloop()