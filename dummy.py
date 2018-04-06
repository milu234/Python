1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
"""*****************************************************************************
                            MODULES USED IN PROJECT
*****************************************************************************"""

import pickle
import os


"""*****************************************************************************
                            CLASS USED IN PROJECT
*****************************************************************************"""

class account(object):
    def __init__(s):
        s.acno=0
        s.name=""
        s.deposit=0
        s.type=""

    def create_account(s):  #function to get data from user
        name=raw_input("\n\nEnter the name of the account holder: ")
        s.name=name.capitalize()
        type=raw_input("\nEnter type of the account (C/S): ")
        s.type=type.upper()
        s.deposit=input("\nEnter initial amount\n(>=500 for Saving and >=1000 for Current): ")

    def show_account(s):    #function to show data on screen
        print "\nAccount No. :", s.acno
        print "\nAccount holder name: ", s.name
        print "\nType of account", s.type
        print "\nBalance amount: ", s.deposit

    def modify(s):          #function to get new data from user
        print "\nAccount No. : ", s.acno
        s.name=raw_input("\n\nEnter the name of account holder: ")
        type=raw_input("\n\nEnter type of account (C/S): ")
        s.type=type.upper()
        s.deposit=input("\nEnter the amount: ")

    def dep(s,x):           #function to accept amount and add to balance
        s.deposit+=x

    def draw(s,x):          #function to accept amount and subtract from balance amount
        s.deposit-=x

    def report(s):          #function to show data in tabular format
        print "%-10s"%s.acno,"%-20s"%s.name,"%-10s"%s.type,"%-6s"%s.deposit

    def retacno(s):         #function to return account number
        return s.acno

    def retdeposit(s):      #function to return balance amount
        return s.deposit

    def rettype(s):         #function to return type of account
        return s.type


"""*****************************************************************************
                    FUNCTION TO GENERATE ACCOUNT NUMBER
*****************************************************************************"""

def gen_acno():
    try:
        inFile=open("account2.dat","rb")
        outFile=open("text2.dat","wb")
        n=inFile.read()
        n=int(n)
        while True:
            n+=1
            outFile.write(str(n))
            inFile.close()
            outFile.close()
            os.remove("account2.dat")
            os.rename("text2.dat","account2.dat")
            yield n

    except IOError:
        print "I/O error occured"


"""*****************************************************************************
                    FUNCTION TO WRITE RECORD IN BINARY FILE
*****************************************************************************"""

def write_account():
    try:
        ac=account()
        outFile=open("account.dat","ab")
        ch=gen_acno()
        ac.acno=ch.next()
        ac.create_account()
        pickle.dump(ac,outFile)
        outFile.close()
        print "\n\n Account Created Successfully"
        print "\n\n YOUR ACCOUNT NUMBER IS: ",ac.retacno()
    except:
        pass


"""*****************************************************************************
                FUNCTION TO DISPLAY ACCOUNT DETAILS GIVEN BY USER
*****************************************************************************"""

def display_sp(n):
    flag=0
    try:
        inFile=open("account.dat","rb")
        print "\nBALANCE DETAILS\n"
        while True:
            ac=pickle.load(inFile)

            if ac.retacno()==n:
                ac.show_account()
                flag=1

    except EOFError:
        inFile.close
        if flag==0:
            print "\n\nAccount number not exist"

    except IOError:
        print "File could not be open !! Press any Key..."


"""*****************************************************************************
                        FUNCTION TO MODIFY RECORD OF FILE
*****************************************************************************"""

def modify_account(n):
    found=0
    try:
        inFile=open("account.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.retacno()==n:
                print 30*"-"
                ac.show_account()
                print 30*"-"
                print "\n\nEnter The New Details of Account"
                ac.modify()
                pickle.dump(ac,outFile)
                print "\n\n\tRecord Updated"
                found=1
            else:
                pickle.dump(ac,outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print "\n\nRecord Not Found "

    except IOError:
        print "File could not be open !! Press any Key..."

    os.remove("account.dat")
    os.rename("temp.dat","account.dat")


"""*****************************************************************************
                    FUNCTION TO DELETE RECORD OF FILE
*****************************************************************************"""

def delete_account(n):
    found=0

    try:
        inFile=open("account.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.retacno()==n:
                found=1
                print "\n\n\tRecord Deleted .."
            else:
                pickle.dump(ac,outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print "\n\nRecord Not Found"

    except IOError:
        print "File could not be open !! Press any Key..."

    os.remove("account.dat")
    os.rename("temp.dat","account.dat")


"""*****************************************************************************
                    FUNCTION TO DISPLAY ALL ACCOUNT DETAILS
*****************************************************************************"""

def display_all():
    print "\n\n\tACCOUNT HOLDER LIST\n\n"
    print 60*"="
    print "%-10s"%"A/C No.","%-20s"%"Name","%-10s"%"Type","%-6s"%"Balance"
    print 60*"=","\n"
    try:
        inFile=open("account.dat","rb")
        while True:
            ac=pickle.load(inFile)
            ac.report()

    except EOFError:
        inFile.close()

    except IOError:
        print "File could not be open !! Press any Key..."


"""*****************************************************************************
            FUNCTION TO DEPOSIT/WITHDRAW AMOUNT FOR GIVEN ACCOUNT
*****************************************************************************"""

def deposit_withdraw(n,option):
    found=0

    try:
        inFile=open("account.dat","rb")
        outFile=open("temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.retacno()==n:
                ac.show_account()
                if option==1:
                    print "\n\n\tTO DEPOSIT AMOUNT"
                    amt=input("Enter the amount to be deposited: ")
                    ac.dep(amt)
                elif option==2:
                    print "\n\n\tTO WITHDRAW AMOUNT"
                    amt=input("Enter amount to be withdraw: ")
                    bal=ac.retdeposit()-amt
                    if((bal<500 and ac.rettype()=="S")or(bal<1000 and ac.rettype()=="C")):
                        print "Insufficient balance"
                    else:
                        ac.draw(amt)
                pickle.dump(ac,outFile)
                found=1
                print "\n\n\tRecord Updated"
            else:
                pickle.dump(ac,outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print "\n\nRecord Not Found"

    except IOError:
        print "File could not be open !! Press any Key..."

    os.remove("account.dat")
    os.rename("temp.dat","account.dat")


"""*****************************************************************************
                        INTRODUCTORY FUNCTION
*****************************************************************************"""

def intro():
    print "\n\n\tBANK"
    print "\n\tMANAGEMENT"
    print "\n\n\nMADE BY : Enter your name"
    print "\nSCHOOL : Enter your school name"


"""*****************************************************************************
                        THE MAIN FUNCTION OF PROGRAM
*****************************************************************************"""

intro()

while True:
    print 3*"\n",60*"="
    print """MAIN MENU

    1. New Account
    2. Deposit Amount
    3. Withdraw Amount
    4. Balance Enquiry
    5. All Account Holder List
    6. Close An Account
    7. Modify An Account
    8. Exit
    """

    try:
        ch=input("Enter Your Choice(1~8): ")
        if ch==1:
            write_account()

        elif ch==2:
            num=input("\n\nEnter Account Number: ")
            deposit_withdraw(num,1)

        elif ch==3:
            num=input("\n\nEnter Account Number: ")
            deposit_withdraw(num,2)

        elif ch==4:
            num=input("\n\nEnter Account Number: ")
            display_sp(num)

        elif ch==5:
            display_all()

        elif ch==6:
            num=input("\n\nEnter Account Number: ")
            delete_account(num)

        elif ch==7:
            num=input("\n\nEnter Account Number: ")
            modify_account(num)

        elif ch==8:
            break

        else:
            print "Input correcr choice...(1-8)"

    except NameError:
        print "Input correct choice...(1-8)"



raw_input("\n\n\n\n\nTHANK YOU\n\nPress any key to exit...")

"""*****************************************************************************
                END OF PROJECT
*****************************************************************************"""
