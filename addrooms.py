from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3


def addroomss():
    RoomNO = custInfo1.get()
    RoomType = custInfo2.get()
    Status = custInfo3.get()
    
    
    insertCust = "insert into rooms values('"+RoomNO+"','"+RoomType+"','"+Status+"')"
    try:
        cur.execute(insertCust)
        con.commit()
        messagebox.showinfo('Success',"Chambre ajoutée avec succès")
    except:
        messagebox.showinfo("Error","Chambre déjà existante")
        
    print(RoomNO)
    print(RoomType)
    print(Status)




    
def addrooms():
    global custInfo1, custInfo2, custInfo3, custInfo4, Canvas1, con, cur, roomTable,root

    root5= Tk()
    root5.title("Ajouter une chambre")
    root5.minsize(width=400,height=400)
    root5.iconbitmap("icons8_hotel.ico")
    root5.geometry("600x500")


    #Connection to database
    #ENTER YOUR USER NAME AND PASSWORD TO CONNECT TO DATABASE
    con = sqlite3.connect("Hotel__man.db")
    cur = con.cursor()

    #table connection
    roomTable= "rooms" #customer table
    
    Canvas1 = Canvas(root5)
    
    Canvas1.config(bg="#E5D4B3")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root5,bg="#DDC1A2",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Ajouter une chambre", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root5,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    #Room Number
    lb1 = Label(labelFrame,text="N° de la chambre :",bg='black',fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)

    custInfo1 = Entry(labelFrame)
    custInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
    

    #Room Type
    lb2 = Label(labelFrame,text="Type de la chambre : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    custInfo2 = Entry(labelFrame)
    custInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
    
    #Status
    lb3 = Label(labelFrame,text="Disponible/Réservée : ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
    


    custInfo3 = Entry(labelFrame)
    custInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

   
    #Submit Button
    SubmitBtn = Button(root5,text="Ajouter",bg='#47290F', fg='white',command=addroomss)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root5,text="Quitter",bg='#47290F', fg='white', command=root5.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root5.mainloop()
