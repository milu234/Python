from tkinter import *
root=Tk()
#Window Appearancw
root.title("House")
c=Canvas(root,bg='white',height=700,width=1500)

#----------------------------------House Front------------------------------------------------

c.create_polygon(600,250,700,150,800,250,800,400,600,400,width=2,fill="yellow",outline='black')

c.create_rectangle(650,275,750,390,fill="pink")#------------------House door--------------------------
c.create_polygon(800,250,900,150,1000,250,1000,400,800,400,width=2,fill="blue",outline='black')#-------------------house side------------------------------------

c.create_rectangle(850,275,900,327,fill="grey")#----------------------------Window-------------------------------------
c.create_polygon(700,150,800,250,1000,250,900,150,width=2,fill="brown",outline='black')
c.create_oval(680,180,725,250, width=0.5, fill='red')#--------------------------circlr above the door------------------------------------------------------------
c.pack()
root.mainloop()
