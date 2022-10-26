from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

#Connection to database
#ENTER YOUR USER NAME AND PASSWORD TO CONNECT TO DATABASE


#table connection


def addcustomer1():
    Lname = custInfo1.get()
    Rnb = custInfo2.get()
    Date=custInfo3.get()
    Nbr = custInfo4.get()
    P = custInfo5.get()
    
    
    insertRes = "insert into checkin values('"+Lname+"','"+Rnb+"','"+Date+"','"+Nbr+",'"+P+"'')"
    try:
        cur.execute(insertRes)
        con.commit()
        messagebox.showinfo('Success',"Booked successfully")
    except:
        messagebox.showinfo("Error","Already booked")
        
    print(Lname)
    print(Rnb)
    print(Date)
    print(Nbr)
    print(P)



def add_customer_details1():
    global custInfo1, custInfo2, custInfo3, custInfo4, custInfo5, Canvas1, con, cur, cust,root3

root3= Tk()
root3.title("Add Customer details")
root3.minsize(width=400,height=400)
#root3.iconbitmap("icons8_five_of_five_stars.ico")
root3.geometry("600x500")
# root3.iconbitmap("icons8_hotel.ico")

con = sqlite3.connect("Hotel__man.db")
cur = con.cursor()

Canvas1 = Canvas(root3)
Canvas1.config(bg="#E5D4B3")
Canvas1.pack(expand=True,fill=BOTH)


headingFrame1 = Frame(root3,bg="#DDC1A2",bd=5)
headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

headingLabel = Label(headingFrame1, text="Add reservation", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


labelFrame = Frame(root3,bg='black')
labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

#Last Name
lb1 = Label(labelFrame,text="Full Name:",bg='black',fg='white')
lb1.place(relx=0.05,rely=0.2, relheight=0.08)

custInfo1 = Entry(labelFrame)
custInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)


#Room number
lb2 = Label(labelFrame,text="Room number : ", bg='black', fg='white')
lb2.place(relx=0.05,rely=0.35, relheight=0.08)
    
custInfo2 = Entry(labelFrame)
custInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

#Issue Date
lb3 = Label(labelFrame,text="Issue Date : ", bg='black', fg='white')
lb3.place(relx=0.05,rely=0.50, relheight=0.08)
    
custInfo3 = Entry(labelFrame)
custInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

#Number of days
lb4 = Label(labelFrame,text="Number of days : ", bg='black', fg='white')
lb4.place(relx=0.05,rely=0.65, relheight=0.08)
    
custInfo4 = Entry(labelFrame)
custInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)


#Payment method
lb5 = Label(labelFrame,text="Cash/Credit card : ", bg='black', fg='white')
lb5.place(relx=0.05,rely=0.80, relheight=0.08)
    
custInfo5 = Entry(labelFrame)
custInfo5.place(relx=0.3,rely=0.80, relwidth=0.62, relheight=0.08)



#Submit Button
SubmitBtn = Button(root3,text="Add Reservation",bg='#47290F', fg='white',command=addcustomer1)
SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

quitBtn = Button(root3,text="Quit",bg='#47290F', fg='white', command=root3.destroy)
quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

root3.mainloop()
