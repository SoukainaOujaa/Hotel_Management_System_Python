import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from addrooms import addrooms
from roomlist import View_Room
from checkin2 import checkin2
from Customerlist1 import View1
from deletereservation import delete_
from modifierreservation import modifier_
from roommd import rooms

root = tk.Tk()
 #setting title
root.title("Hôtel 5 étoiles GETAWAY")
root.iconbitmap("icons8_hotel.ico")
#setting window size
width=701
height=436
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

image1 = tk.PhotoImage(file="C:\\Users\\Soukaina\\OneDrive\\Bureau\\M1\\Python - R\\Hotel\\Mixed Use Bulding.png")
GLabel_159=tk.Label(root)
GLabel_159.image=image1
GLabel_159["image"]=image1
ft = tkFont.Font(family='Times',size=10)
GLabel_159["font"] = ft
GLabel_159["fg"] = "#333333"
GLabel_159["justify"] = "center"
GLabel_159["text"] = ""
GLabel_159.place(x=0,y=0,width=704,height=436)

GLabel_926=tk.Label(root)
GLabel_926["bg"] = "#000000"
ft = tkFont.Font(family='Times',size=10)
GLabel_926["font"] = ft
GLabel_926["fg"] = "#333333"
GLabel_926["justify"] = "center"
GLabel_926["text"] = ""
GLabel_926.place(x=130,y=100,width=440,height=236)

GLabel_816=tk.Label(root)
GLabel_816["bg"] = "#000000"
ft = tkFont.Font(family='Times',size=23)
GLabel_816["font"] = ft
GLabel_816["fg"] = "#ffffff"
GLabel_816["justify"] = "center"
GLabel_816["text"] = "Page d'authentification"
GLabel_816.place(x=210,y=120,width=290,height=40)

GLabel_479=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_479["font"] = ft
GLabel_479["fg"] = "#ffffff"
GLabel_479["bg"]='black'
GLabel_479["justify"] = "center"
GLabel_479["text"] = "Nom d'uitlisateur :"
GLabel_479.place(x=160,y=180,width=130,height=30)

GLabel_705=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_705["font"] = ft
GLabel_705["bg"]='black'
GLabel_705["fg"] = "#ffffff"
GLabel_705["justify"] = "center"
GLabel_705["text"] = "Mot de passe :"
GLabel_705.place(x=150,y=230,width=130,height=30)

GLineEdit_860=tk.Entry(root)
GLineEdit_860["bg"] = "#ffffff"
GLineEdit_860["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_860["font"] = ft
GLineEdit_860["fg"] = "#333333"
GLineEdit_860["justify"] = "center"
GLineEdit_860["text"] = ""
GLineEdit_860.place(x=310,y=180,width=221,height=33)

GLineEdit_375=tk.Entry(root)
GLineEdit_375["bg"] = "#ffffff"
GLineEdit_375["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_375["font"] = ft
GLineEdit_375["fg"] = "#333333"
GLineEdit_375["justify"] = "center"
GLineEdit_375["text"] = ""
GLineEdit_375.config(show="*")
GLineEdit_375.place(x=310,y=230,width=222,height=30)


def login():
    uname=GLineEdit_860.get()
    password=GLineEdit_375.get()
    if uname=="" and password =="" :
        messagebox.showinfo("","Champs vides!")
    elif uname=='Manager' and password=='Hotel':
        messagebox.showinfo("Authentifié avec succès", "     Bienvenue!    ")
        root.destroy()
        #Connect to myql
        #ENTER YOUR USER NAME AND PASSWORD TO CONNECT TO DATABASE
        
        #creating a database if not exist;
        con = sqlite3.connect("Hotel__man.db")
        mycursor = con.cursor()
        
        #Creating tables
        # mycursor.execute("CREATE TABLE cust (FNAME VARCHAR(20) PRIMARY KEY NOT NULL, LNAME VARCHAR(20) NOT NULL, PHNO int NOT NULL)")
        # mycursor.execute("CREATE TABLE issued_rooms (RoomNo int AUTO_INCREMENT PRIMARY KEY NOT NULL, issuedto VARCHAR(30) NOT NULL, status VARCHAR(30) NOT NULL)")
        # mycursor.execute("CREATE TABLE rooms (RoomNo int AUTO_INCREMENT PRIMARY KEY NOT NULL, RoomType VARCHAR(30) NOT NULL, status VARCHAR(30) NOT NULL)")
        # mycursor.execute("CREATE TABLE checkin (LNAME VARCHAR(20) PRIMARY KEY NOT NULL, Rnb int NOT NULL, Date VARCHAR(20), Nbr int NOT NULL,P VARCHAR(20) NOT NULL)")
        # mycursor = con.cursor()
        root1 = Tk()
        root1.title("Hôtel 5 étoiles GETAWAY")
        #root1.minsize(width=400,height=400)
        root1.geometry("800x600")
        root1.iconbitmap("icons8_hotel.ico")
        same=True
        n=0.25

        # Adding a background image

        photo=PhotoImage(file="C:\\Users\\Soukaina\\OneDrive\\Bureau\\M1\\Python - R\\Hotel\\Mixed Use Bulding.png")
        label = Label(root1,image = photo)
        label.image = photo # keep a reference!
        label.grid(row=0,column=0,columnspan=20,rowspan=20)

        headingFrame1 = Frame(root1,bg="#CCB993",bd=5)
        headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

        headingLabel = Label(headingFrame1, text="Welcome to 5 stars GETAWAY Hotel", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


        #Frame addc
        headingFrame2 = Frame(root1,bg="#CCB993",bd=3)
        headingFrame2.place(relx=0.28,rely=0.3,relwidth=0.45,relheight=0.1)
        # add customer details

        # btn1 = Button(headingFrame2, text="Add Customer Details", bg='Black',fg='white',command =add_customer_details)
        # btn1.place(relx=0.28,rely=0.3,relwidth=0.45,relheight=0.1)

        # add customer details
        btn1 = Button(headingFrame2, text="Réserver", bg='Black',fg='white',command =checkin2)
        btn1.place(relx=0,rely=0,relwidth=1,relheight=1)

        #Frame Check in
        headingFrame3 = Frame(root1,bg="#CCB993",bd=3)
        headingFrame3.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)

        #Check in
        # btn2 = Button(root1, text="Check In", bg='Black',fg='white',command=checkin)
        # btn2.place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)
        btn2 = Button(headingFrame3, text="Annuler réservation", bg='Black',fg='white',command=delete_)
        btn2.place(relx=0,rely=0,relwidth=1,relheight=1)
        #Frame Check out
        headingFrame4 = Frame(root1,bg="#CCB993",bd=3)
        headingFrame4.place(relx=0.28,rely=0.5,relwidth=0.45,relheight=0.1)

        #check out
        # btn3 = Button(root1,text="Check Out",bg='black', fg='white',command=checkout)
        # btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

        btn3 = Button(headingFrame4,text="Modifier réservation",bg='black', fg='white',command=modifier_)
        btn3.place(relx=0,rely=0,relwidth=1,relheight=1)

 #Frame Customer list
        headingFrame5 = Frame(root1,bg="#CCB993",bd=3)
        headingFrame5.place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1)
        # View Customer List
        # btn4 = Button(root1,text="View Customer List",bg='black', fg='white',command =View)
        # btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
        btn4 = Button(headingFrame5,text="Liste des réservations",bg='black', fg='white',command =View1)
        btn4.place(relx=0,rely=0,relwidth=1,relheight=1)


#Frame ADD ROOM
        headingFrame6 = Frame(root1,bg="#CCB993",bd=3)
        headingFrame6.place(relx=0.28,rely=0.7,relwidth=0.45,relheight=0.1)
        #Add Room(Connect it to rooms table)
        # btn5 = Button(root1,text="Add Rooms",bg='black', fg='white',command =addrooms)
        # btn5.place(relx=0,rely=0,relwidth=1,relheight=1)

        btn5 = Button(headingFrame6,text="Ajouter une chambre",bg='black', fg='white',command =addrooms)
        btn5.place(relx=0,rely=0,relwidth=1,relheight=1)


#Frame Room list
        headingFrame7 = Frame(root1,bg="#CCB993",bd=3)
        headingFrame7.place(relx=0.28,rely=0.8,relwidth=0.45,relheight=0.1)
        #Room List
        
        btn6 = Button(headingFrame7,text="Liste des chambres",bg='black', fg='white',command =View_Room)
        btn6.place(relx=0,rely=0,relwidth=1,relheight=1)
        
###
        headingFrame8 = Frame(root1,bg="#CCB993",bd=3)
        headingFrame8.place(relx=0.28,rely=0.9,relwidth=0.45,relheight=0.1)
        #Room List
        
        btn6 = Button(headingFrame8,text="Supprimer/Modifier une chambre",bg='black', fg='white',command =rooms)
        btn6.place(relx=0,rely=0,relwidth=1,relheight=1)
        root1.mainloop()

    else :
        messagebox.showwarning("Authentification échouée !", "   Réessayez    ")
GButton_908=tk.Button(root)
GButton_908["bg"] = "#47290F" 
ft = tkFont.Font(family='Times',size=10)
GButton_908["font"] = ft
GButton_908["fg"] = "#ffffff"
GButton_908["justify"] = "center"
GButton_908["text"] = "Se connecter"
GButton_908.place(x=310,y=280,width=118,height=30)
GButton_908["command"] =login

GButton_131=tk.Button(root)
GButton_131["bg"] = "#47290F"
ft = tkFont.Font(family='Times',size=10)
GButton_131["font"] = ft
GButton_131["fg"] = "#ffffff"
GButton_131["justify"] = "center"
GButton_131["text"] = "Fermer"
GButton_131.place(x=440,y=280,width=95,height=30)
GButton_131["command"] = root.destroy



root.mainloop()
