from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

#connect to database
#ENTER YOUR USER NAME AND PASSWORD TO CONNECT TO DATABASE

#cur.execute("select * from checkin")

#table connection


#list to store all room number 
#allRoomNo = []
global custInfo1, custInfo2, custInfo3, custInfo4, custInfo5, Canvas1, con, cur, cust,root
def modifier():
    Lname = custInfo1.get()
    Rnb = custInfo2.get()
    Date=custInfo3.get()
    Nbr = custInfo4.get()
    Pay = custInfo5.get()
    
    
    modifier = "update checkin set Rnb='"+Rnb+"',Date='"+Date+"',Nbr='"+Nbr+"',P='"+Pay+"' where LNAME='"+Lname+"' "
    try:
        cur.execute(modifier)
        con.commit()
        messagebox.showinfo('Success',"Modifiée avec succès")
    except:
        messagebox.showinfo("Error","Client inexistant")


    # extractRoomNo = "select RoomNo from rooms"
    # cur.execute(extractRoomNo)
    # con.commit()
    # for i in cur:
    #     allRoomNo.append(i[0])
        
        
    # show = "select * from checkin"
    # upadateStatus = "update rooms set status = 'issued' where RoomNo ='"+Rnb+"'"
    # try:
    #     if Rnb in allRoomNo :
    #         cur.execute(upadateStatus)
    #         con.commit()
    #         messagebox.showinfo("Success", "Checked In Succesfully")
    #         root3.destroy()
    #     else:
    #         allRoomNo.clear()
    #         messagebox.showinfo("Failed","Failed to check in")
    #         root3.destroy()
    #         return
    # except:
    #     messagebox.showinfo("Search Error","This value entered is wrong, Try again")
    
    print(Lname)
    print(Rnb)
    print(Date)
    print(Nbr)
    print(Pay)

    #allRoomNo.clear()
def modifier_():
    global custInfo1, custInfo2, custInfo3, custInfo4, custInfo5, Canvas1, con, cur, cust,root

    root3= Tk()
    root3.title("Modifier une réservation")
    root3.minsize(width=400,height=400)
    root3.iconbitmap("icons8_hotel.ico")
    #root3.iconbitmap("icons8_five_of_five_stars.ico")
    root3.geometry("600x500")
    # root3.iconbitmap("icons8_hotel.ico")
    con = sqlite3.connect('Hotel__man.db')
    cur = con.cursor()

    Canvas1 = Canvas(root3)
    Canvas1.config(bg="#E5D4B3")
    Canvas1.pack(expand=True,fill=BOTH)


    headingFrame1 = Frame(root3,bg="#DDC1A2",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Modifier", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root3,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    #Last Name
    lb1 = Label(labelFrame,text="Nom du client:",bg='black',fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)

    custInfo1 = Entry(labelFrame)
    custInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)


    #Room number
    lb2 = Label(labelFrame,text="N° de la chambre : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    custInfo2 = Entry(labelFrame)
    custInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)

    #Issue Date
    lb3 = Label(labelFrame,text="Date de réservation: ", bg='black', fg='white')
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    custInfo3 = Entry(labelFrame)
    custInfo3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)

    #Number of days
    lb4 = Label(labelFrame,text="Nombre de jours : ", bg='black', fg='white')
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
        
    custInfo4 = Entry(labelFrame)
    custInfo4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)


    #Payment method
    lb5 = Label(labelFrame,text="Cash/Credit card : ", bg='black', fg='white')
    lb5.place(relx=0.05,rely=0.80, relheight=0.08)
        
    custInfo5 = Entry(labelFrame)
    custInfo5.place(relx=0.3,rely=0.80, relwidth=0.62, relheight=0.08)



    #Submit Button
    SubmitBtn = Button(root3,text="Modifier",bg='#47290F', fg='white',command=modifier)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root3,text="Quitter",bg='#47290F', fg='white', command=root3.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root3.mainloop()