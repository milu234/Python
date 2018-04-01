from tkinter import*

root = Tk()
root.geometry('800x800')
root.title("ADMISSION FORM")

label_0 = Label(root, text="ADMISSION FORM", width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="First Name",width=20,font=("bold",10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Last Name",width=20,font=("bold",10))
label_2.place(x=80,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Email",width=20,font=("bold",10))
label_3.place(x=68,y=230)

entry_3 = Entry(root)
entry_3.place(x=240,y=230)

password_1 = Label(root, text="Password",width=20,font=("bold",10))
password_1.place(x=80,y=280)

entry_4 = Entry(root,show="*")
entry_4.place(x=240,y=280)

password_2 = Label(root, text="Confirm Password",width=20,font=("bold",10))
password_2.place(x=80,y=330)

entry_5 = Entry(root,show="*")
entry_5.place(x=240,y=330)

label_4 = Label(root, text="Gender",width=20,font=("bold",10))
label_4.place(x=70,y=380)
var = IntVar()
Radiobutton(root, text="Male", padx = 5, variable=var,value=1).place(x=235,y=380)
Radiobutton(root, text="Female", padx = 20, variable=var,value=2).place(x=290,y=380)

label_5 = Label(root, text="Location",width=20,font=("bold",10))
label_5.place(x=70,y=430)

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
droplist.place(x=240,y=430)

label_5 = Label(root, text="Programming",width=20,font=("bold",10))
label_5.place(x=85,y=530)
var1= IntVar()
Checkbutton(root, text="Java",variable=var1).place(x=235,y=530)
var2= IntVar()
Checkbutton(root, text="Python",variable=var2).place(x=290,y=530)

Button(root, text='Submit',width = 20, bg='brown' ,fg='white').place(x=180,y=580)

mainloop()





