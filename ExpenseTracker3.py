from tkinter import *
from tkinter import ttk
import sqlite3  as db

from tkcalendar import DateEntry

def init():
    connectionObjn = db.connect("expenseTracker.db")
    curr = connectionObjn.cursor()
    query = '''
    create table if not exists expenses (
        date string,
        name string,
        title string,
        method string,
        expense number
        )
    '''
    curr.execute(query)
    connectionObjn.commit()

def submitexpense():
    values=[dateEntry.get(),Title.get(),Vendor.get(),PaymentMethod.get(),Expense.get()]
    print(values)
    Etable.insert('','end',values=values)

    connectionObjn = db.connect("expenseTracker.db")
    curr = connectionObjn.cursor()
    query = '''
    INSERT INTO expenses VALUES 
    (?, ?, ?, ?, ?)
    '''
    curr.execute(query,(dateEntry.get(),Title.get(),Vendor.get(),PaymentMethod.get(),Expense.get()))
    connectionObjn.commit()

def viewexpense():
    connectionObjn = db.connect("expenseTracker.db")
    curr = connectionObjn.cursor()
    query = '''
     select * from expenses
    '''
    total='''
    select sum(expense) from expenses
    '''
    curr.execute(query)
    rows=curr.fetchall()
    curr.execute(total)
    amount=curr.fetchall()[0]
    print(rows)
    print(amount)
    
    l=Label(root,text="Date\t  Title\t  Vendor\t  Method\t  Expense\t",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white")
    l.grid(row=6,column=0,padx=7,pady=7)

    st=""
    for i in rows:
        for j in i:
            st+=str(j)+'\t'
        st+='\n'
    print(st)
    l=Label(root,text=st,font=('arial',12))
    l.grid(row=8,column=0,padx=7,pady=7)


init()
root=Tk()
root.title("Expense tracker")
root.geometry('1100x600')

dateLabel=Label(root,text="Date",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12)
dateLabel.grid(row=0,column=0,padx=7,pady=7)

dateEntry=DateEntry(root,width=12,font=('arial',15,'bold'))
dateEntry.grid(row=0,column=1,padx=7,pady=7)

Title=StringVar()
titleLabel=Label(root, text="Title",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12)
titleLabel.grid(row=1,column=0,padx=7,pady=7)

TitleEntry=Entry(root,textvariable=Title,font=('arial',15,'bold'))
TitleEntry.grid(row=1,column=1,padx=7,pady=7)

Vendor=StringVar()
vendorLabel=Label(root, text="Vendor",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12)
vendorLabel.grid(row=2,column=0,padx=7,pady=7)

vendorEntry=Entry(root,textvariable=Vendor,font=('arial',15,'bold'))
vendorEntry.grid(row=2,column=1,padx=7,pady=7)

PaymentMethod=StringVar()
PaymentMethodLabel=Label(root, text="Method",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12)
PaymentMethodLabel.grid(row=3,column=0,padx=7,pady=7)

PaymentMethodEntry=Entry(root,textvariable=PaymentMethod,font=('arial',15,'bold'))
PaymentMethodEntry.grid(row=3,column=1,padx=7,pady=7)

Expense=IntVar()
expenseLabel=Label(root,text="Expense",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12)
expenseLabel.grid(row=4,column=0,padx=7,pady=7)

expenseEntry=Entry(root,textvariable=Expense,font=('arial',15,'bold'))
expenseEntry.grid(row=4,column=1,padx=7,pady=7)

submitbtn=Button(root,command=submitexpense,text="Submit",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12 )
submitbtn.grid(row=5,column=0,padx=13,pady=13)

##viewtn=Button(root,command=viewexpense,text="View expenses",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12 )
##viewtn.grid(row=5,column=1,padx=13,pady=13)

# all saved expenses--------------
Elist=['Date','Title','Vendor','Method','Expense']
Etable=ttk.Treeview(root,column=Elist,show='headings',height=3)
for c in Elist:
    Etable.heading(c,text=c.title())
Etable.grid(row=6,column=0,padx=7,pady=7,columnspan=3)

mainloop()
