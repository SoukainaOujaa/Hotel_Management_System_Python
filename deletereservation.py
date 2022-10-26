from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

#ENTER YOUR USER NAME AND PASSWORD TO CONNECT TO DATABASE
con = sqlite3.connect("Hotel__man.db")
cur = con.cursor()
c=con.cursor()

# Enter Table Names here

def delete():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,quitBtn,Canvas1,status
    
    Fname = bookInfo1.get()

    Delete = "delete from checkin where LNAME='"+Fname+"' "
    #select="select Rnb from checkin where LNAME='"+Fname+"'"
    
    try:
        cur.execute(Delete)
        con.commit()
        messagebox.showinfo("Error","Supprimée avec succès")
        # c.execute(select)
        # rows=c.fetchall()
        # for row in rows :
        #     y=row
        # con.commit
        # updateroom="update rooms set status='avail' where RoomNo IN (select Rnb from checkin where LNAME='"+Fname+"')"
        # cur.execute(updateroom)
        # con.commit()
        # messagebox.showinfo('Success',"Room's status changed ")
    except:
        messagebox.showinfo("Error","Client inexistant")
    
    
def delete_(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,labelFrame, lb1
    
    root4 = Tk()
    root4.title("Annuler réservation")
    root4.minsize(width=400,height=400)
    root4.iconbitmap("icons8_hotel.ico")
    root4.geometry("600x500")

    
    Canvas1 = Canvas(root4)
    
    Canvas1.config(bg="#E5D4B3")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root4,bg="#DDC1A2",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Annuler une réservation", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root4,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Name to Delete
    lb1 = Label(labelFrame,text="Nom complet : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root4,text="Annuler",bg='#47290F', fg='white',command=delete)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root4,text="Quitter",bg='#47290F', fg='white', command=root4.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root4.mainloop()