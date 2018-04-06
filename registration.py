from tkinter import*
import mysql.connector;

conn=mysql.connector.connect(host='localhost',database='course',user='root',password='jordanbelfort@123')
cursor=conn.cursor()

root = Tk()
root.geometry('800x800')
root.title("ADMISSION FORM")

#Title
label_0 = Label(root, text="ADMISSION FORM", width=20,font=("bold", 20))
label_0.place(x=90,y=53)
#-----------------------First name design---------------------------------

label_1 = Label(root, text="First Name",width=20,font=("bold",10))
label_1.place(x=80,y=130)

firstname = StringVar()
entry_1 = Entry(root, textvariable=firstname)
entry_1.place(x=240,y=130)
#--------------------------Last Name--------------------------------------

label_2 = Label(root, text="Last Name",width=20,font=("bold",10))
label_2.place(x=80,y=180)

lastname=StringVar()
entry_2 = Entry(root, textvariable=lastname)
entry_2.place(x=240,y=180)

#-----------------------Roll N0.---------------------------------------------------------------
roll_2 = Label(root, text="Roll No",width=20,font=("bold",10))
roll_2.place(x=80,y=230)

roll=IntVar()
entry_2 = Entry(root, textvariable=roll)
entry_2.place(x=240,y=230)
#----------------------------Email-----------------------------------------


label_3 = Label(root, text="Email",width=20,font=("bold",10))
label_3.place(x=68,y=280)

email=StringVar()
entry_3 = Entry(root,textvariable=email)
entry_3.place(x=240,y=280)
#-----------------------------Password------------------------------------

password_1 = Label(root, text="Password",width=20,font=("bold",10))
password_1.place(x=80,y=330)

passwd=StringVar()
entry_4 = Entry(root,show="*",textvariable=passwd)
entry_4.place(x=240,y=330)
#=====================Confirm Password================================

password_2 = Label(root, text="Confirm Password",width=20,font=("bold",10))
password_2.place(x=80,y=380)

cpasswd=StringVar()
entry_5 = Entry(root,show="*",textvariable=cpasswd)
entry_5.place(x=240,y=380)

#----------------------------Gender------------------------------------
label_4 = Label(root, text="Gender",width=20,font=("bold",10))
label_4.place(x=70,y=430)
var = IntVar()
Radiobutton(root, text="Male", padx = 5, variable=var,value=1).place(x=235,y=430)
Radiobutton(root, text="Female", padx = 20, variable=var,value=2).place(x=290,y=430)

#---------------------------Location---------------------------------------
label_5 = Label(root, text="Location",width=20,font=("bold",10))
label_5.place(x=70,y=480)

list1 = ['','Churchgate (S/F)'
,'Marine Lines (S)'
,'Charni Road (S)'
,'Grant Road (S)'
,'Mumbai Central (F/S)'
,'Maha Laxmi (S)'
,'Lower Parel (S)'
,'Elphinstone Road (S)'
,'Dadar (F/S)'
,'Matunga Road (S)'
,'Mahim Junction (S)'
,'Bandra (F/S)'
,'Khar Road (S)'
,'Santacruz (S)'
,'Vile Parle (S)'
,'Andheri (F/S)'
,'Jogeshwari (S)'
,'Goregaon (S)'
,'Malad (S)'
,'Kandivili (S)'
,'Borivali (F/S)'
,'Dahisar (S)'
,'Mira Road (S)'
,'Bhayander (S/F)'
,'Nalgaon (S)'
,'Vasai Road (S/F)'
,'Nala Sopara (S)'
,'Virar (S/F)'
,'Vaitarna'
,'Saphale'
,'Kelve Road'
,'Palghar'
,'Umroli'
,'Boisar'
,'Vangaon'
,'Dahanu Road'
,'Mumbai CST (S/F)'
,'Masjid'
,'Sandhurst Road'
,'Byculla (S/F)'
,'Chinchpokli'
,'Currey Road'
,'Parel'
,'Dadar (S/F)'
,'Matunga'
,'Sion'
,'Kurla (S/F)'
,'Vidyavihar'
,'Ghatkopar (S/F)'
,'Vikhroli'
,'Kanjur Marg'
,'Bhandup'
,'Nahur'
,'Mulund'
,'Thane (S/F)'
,'Kalva'
,'Mumbra'
,'Diva Junction'
,'Kopar'
,'Dombivali (S/F)'
,'Thakurli'
,'Kalyan Junction (S/F))'
,'Shahad'
,'Ambivali'
,'Titwala'
,'Khadavali'
,'Vasind'
,'Asangaon'
,'Atgaon'
,'Thansit'
,'Khardi'
,'Oombermali'
,'Kasara'
,'Vithalwadi'
,'Ulhasnagar'
,'Ambernath'
,'Badlapur'
,'Vangani'
,'Shelu'
,'Nerul'
,'Bhipuri Road'
,'Karjat'
,'Palasdari'
,'Kelavli'
,'Dolavli'
,'Lowjee'
,'Khopoli'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('Select Your Location')
droplist.place(x=240,y=480)

#----------------------------Checkbox----------------------------------
label_5 = Label(root, text="Programming",width=20,font=("bold",10))
label_5.place(x=85,y=580)
var1= IntVar()
Checkbutton(root, text="Java",variable=var1).place(x=235,y=580)
var2= IntVar()
Checkbutton(root, text="Python",variable=var2).place(x=290,y=580)

#------------------------Submit------------------------------------




work=Button(root, text="Submit", width=30,height=5, bg="lightblue", command=lambda:insert_data(int(roll.get())).place(x=390,y=580))

root.mainloop()





