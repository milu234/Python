from tkinter import Tk,Message
root = Tk()
root.geometry("300X150+50+50")
msg = Message(root,text='Hello World')

msg.config(font=('times',48,'italic bold underline'))
msg.pack()
root.mainloop()
