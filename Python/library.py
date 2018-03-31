from tkinter import *
import sqlite3
import time
import datetime
import random
from tkinter import messagebox
import subprocess as s


class Application(Text):
    """docstring for ClassName"""
    def __init__(self, master):
        Text.__init__(self, master)


        #heading for the main window
        self.heading = Label(master, text="Welcome to Library Prototype", font=('arial 40 bold'), bg='#49E3CE')
        self.heading.place(x=0, y=0)

        #labels for name date author genre position
        self.name = Label(master, text="Name of the Book: ", bg='#49E3CE')
        self.author = Label(master, text="Author of the book: ", bg='#49E3CE')
        self.genre = Label(master, text="Genre of the book: ", bg='#49E3CE')
        self.position = Label(master, text="Position of the book: ", bg='#49E3CE')

        self.name.place(x=0, y=60)
        self.author.place(x=0, y=100)
        self.genre.place(x=0, y=140)
        self.position.place(x=0, y=180)

        #entries for labels
        self.book = StringVar()
        self.name_ent = Entry(master, width=30, textvariable=self.book).place(x=150 , y=60)
        self.writer = StringVar()
        self.author_ent = Entry(master, width=30, textvariable=self.writer).place(x=150 , y=100)
        self.tags = StringVar()
        self.genre_ent = Entry(master, width=30, textvariable=self.tags).place(x=150 , y=140)
        self.placed = StringVar()
        self.position_ent = Entry(master, width=30, textvariable=self.placed).place(x=150 , y=180)

        #button to perform
        self.submit = Button(master, text="Add To Database",command=self.dynamic_data_entry, width=20, height=2, bg='#3D6DEE')
        
        self.submit.place(x=150, y=220)
        self.search = Button(master, text="Search Books", width=20, height=2, command=self.search_root, bg='#1DC550').place(x=150, y=300)
        self.quit = Button(master, text="Exit", width=20, height=2, command=master.destroy, bg='#EE3D3D').place(x=350, y=300)

        #textbox to display updates
        self.box = Text(master, height=15, width=60)
        self.box.focus_set()
        self.box.place(x=400, y=60)
    #Now adding the user input to database. 
    global conn
    global c   
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    def dynamic_data_entry(self):
        #creating the database if it doesnot exist
        c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(datestamp TEXT, name TEXT, author TEXT, genre TEXT, position TEXT)")
    

        #adding fields and values to the databse
        unix = time.time()
        datestamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        name = self.book.get()
        author = self.writer.get()
        genre = self.tags.get()
        position = self.placed.get()
        if len(name) == 0 or len(author) == 0 or len(genre) == 0 or len(position) == 0:
            print("Failed. Please Fill up all the information")
            messagebox.showwarning("Failed", "Please don't leave anything blank.")


        else:
            c.execute("INSERT INTO stuffToPlot (datestamp, name, author, genre, position) VALUES (?, ?,?, ?, ?)",(datestamp, name, author, genre, position))
            conn.commit()
            self.box.insert(END, ('Logs: Added ' +name.upper() + " by " + author+ "\n" ))
            messagebox.showinfo("Success", "Successfully added to the database")

    #search funtionality feature.
    def search_root(self):
        class Search(Text):
            def __init__(self, faster):
                Text.__init__(self, faster)

                #labels for window
                self.heading = Label(faster, text="Search Books Here.", font=('arial 25 bold'), bg='#F0AE59')
                self.heading.place(x=0, y=0)
                
                self.name = Label(faster, text="Name of the Book: ", bg='#F0AE59')
                self.name.place(x=0, y=60)

                #self.entrybox

                self.ent = Entry(faster, width=30)
                self.ent.place(x=150, y=60)

                self.sbox = Text(faster, height=15, width=60, bg="white")
                self.sbox.place(x=50, y=130)
                self.sbox.focus_set()



                #button to perform search
                self.bt = Button(faster,text="Search",command=self.get_it ,width=20, height=2, bg='#3D6DEE')
                self.bt.place(x=390, y=50)

                #button to book books
                self.bt1 = Button(faster,text="Issue Book",command=self.book_it ,width=20, height=2, bg='#1DC550')          
                self.bt1.place(x=500, y=150)

                #button to quit
                self.qt = Button(faster,text="Exit",command=faster.destroy ,width=20, height=2, bg='#EE3D3D').place(x=500, y=300)

                #destroy button
            def master_exit(self):
                master.destroy()
            
            #button to book books

            def book_it(self):
                class Stan(Text):
                        def __init__(self, frame):
                            Text.__init__(self, frame)
                        self.hd = Label(frame, text="Book this Book", font=('arial 25 bold'), fg='steelblue')
                        self.hd.place(x=0, y=0)

                        #info of the book taker
                        self.id = Label(frame, text="Name of Student", font=('arial 15'))
                        self.id.place(x=0, y=60)

                        self.book = Label(frame, text="Name of the book", font=('arial 15'))
                        self.book.place(x=0, y=100)

                        self.phone = Label(frame, text="Mobile Number", font=('arial 15'))
                        self.phone.place(x=0, y=140)                   
                        self.number = Label(frame, text="ID Number", font=('arial 15 '))
                        self.number.place(x=0, y=180)                                

                        self.issue = time.strftime("%x")
                        self.date_1 = datetime.datetime.strptime(self.issue, "%m/%d/%y")
                        self.end_date = self.date_1 + datetime.timedelta(days=21)


                        self.dla = Label(frame, text=("Issued Date: " + "                              "+ str(self.date_1)), font=('arial 15'))
                        self.dla.place(x=0, y=220)

                                            
                        self.end = Label(frame, text=("Submission Date: " +"                      " +str(self.end_date)), font=('arial 15'))
                        self.end.place(x=0, y=260)
                        
                        self.email = Label(frame, text="Email Address", font=('aial 15'))
                        self.email.place(x=0, y=300)

                        #entries for the infos
                        self.ide = Entry(frame, width=30)
                        self.ide.place(x=280, y=60)
                        self.booke = Entry(frame, width=30)
                        self.booke.place(x=280, y=100)
                        self.nume = Entry(frame, width=30)
                        self.nume.place(x=280, y=180)
                        self.phe = Entry(frame, width=30)
                        self.phe.place(x=280, y=140)
                        self.eme = Entry(frame, width=30)
                        self.eme.place(x=280, y=300)

                        #button to make issue right

                        self.iss = Button(frame, text="Issue", width=20, height=2, command=self.issues, bg='#1DC550').place(x=0, y=340)
                        self.xt = Button(frame, text="Exit", width=20, height=2, command=frame.destroy, bg='#EE3D3D').place(x=200, y=340)

                        self.mty = Text(frame, height=16, width=45)
                        self.mty.place(x=550, y=60)

                    
                        def issues(self):
                            self.std = self.ide.get()
                        self.bk = self.booke.get()
                        self.num = self.nume.get()
                        self.ph = self.phe.get()
                        self.em = self.eme.get()
                        if self.std == '' or self.bk == '' or self.num == '' or self.ph == '' or self.em == '':
                            messagebox.showwarning("Error", "Please Fill The Missing Boxes")
                        else:

                            content = (self.std + "\n" + self.bk + "\n" + self.num + "\n" + self.ph + "\n" + self.em +"\n" +"=====================" + "\n")
                            self.mty.insert(END, content)
                            s.call(['notify-send', 'A book has been issued', 'Notification-Library'])

                            messagebox.showinfo("Issued", "Successfully Issued  the Book")
                            file = open(self.bk, "w")
                            file.write(content)
                            file.close()


                dw = Tk()
                dw.geometry('900x400')
                dw.resizable(False, False)
                d = Stan(dw)
                dw.mainloop()

            def get_it(self):

                conn = sqlite3.connect('books.db')
                c = conn.cursor()                
                c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(datestamp TEXT, name TEXT, author TEXT, genre TEXT, position TEXT)")
                free = self.ent.get()
                full_proof = '%' + free + '%'
                c.execute("SELECT * FROM stuffToPlot WHERE name LIKE ?", (free,))
                #data = c.fetchall()
                #print(data)
                for self.row in c.fetchall():
                    if self.row == None:
                        messagebox.showinfo("Not Found", "Sorry, No such book found.")
                        self.sbox.insert(END, "No Such book found in the database.")
                    else:

                        self.sbox.insert(END, (self.row[0] +" "+ self.row[1]) +" " + self.row[4]+ "\n")
                #dynamic_data_entry()
                c.close
                conn.close()


        window = Tk()
        window.geometry('900x400')
        window.resizable(False, False)
        window.config(background='#F0AE59')
        c = Search(window)
        window.mainloop()

root = Tk()
root.geometry('900x400')
root.resizable(False, False)
root.config(background='#49E3CE')

b = Application(root)
root.mainloop()
