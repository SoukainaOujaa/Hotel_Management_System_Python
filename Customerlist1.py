from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

#Conncect to database
#ENTER YOUR USER NAME AND PASSWORD TO CONNECT TO DATABASE
con = sqlite3.connect("Hotel__man.db")
cur = con.cursor()

#Table connection

def View1(): 
    
    root6 = Tk()
    root6.title("Liste des réservations")
    root6.minsize(width=420,height=400)
    root6.iconbitmap("icons8_hotel.ico")
    root6.geometry("600x500")


    Canvas1 = Canvas(root6) 
    Canvas1.config(bg="#E5D4B3")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root6,bg="#DDC1A2",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Liste des réservations", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root6,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.86,relheight=0.5)
    y = 0.25

    Label(labelFrame, text="%-1s%-15s%-20s%-20s%-20s"%('Full_Name      ','        Room_number   ','     Issue_Date','   Nb days   ','   Payment method'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="--------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getBooks = "select * from checkin"
    try:
        cur.execute(getBooks)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-40s%-15s%-23s%-30s%-100s"%(i[0],i[1],i[2],i[3],i[4]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root6,text="Close",bg='#47290F', fg='white', command=root6.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root6.mainloop()
    