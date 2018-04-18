from tkinter import *
root = Tk()
import tkinter.messagebox

canv = Canvas(root, width=1200, height=720, bg='white')
canv.grid(row=2, column=3)

img = PhotoImage(file="lastbg.png")
canv.create_image(10,10, anchor=NW, image=img)

class Application:
    def __init__(self,master):
        self.master = master


        self.heading = Label(master, text="Update Appointments",  fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)
        self.namenet = Entry(master, width=30)
        
        self.namenet.place(x=280, y=62)


         
         

mainloop()
