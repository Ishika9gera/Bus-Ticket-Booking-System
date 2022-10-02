###################################################################################### ISHIKA GERA ##################################################################################################
from tkinter import *
from tkinter import ttk
import sqlite3
main_w = Tk()
main_w.geometry("700x500")
main_w.title("Bus Booking System")
conn=sqlite3.connect('busb.db')
c=conn.cursor()
conn.execute("""CREATE TABLE IF NOT EXISTS BUS(
    "BUS TYPE" VARCHAR(25) NOT NULL, 
    START VARCHAR(25) NOT NULL, 
    END VARCHAR(25) NOT NULL,
    DATE DATE NOT NULL,
    "DEPARTURE TIME" VARCHAR(10) NOT NULL,
    "ARRIVAL TIME" VARCHAR(10) NOT NULL,
    FARE VARCHAR(10) NOT NULL,
    SEATS INT(10) NOT NULL
    );""")
conn.commit()
def add() :
    root1=Tk()
    root1.geometry("750x750")
    Label(root1, text="Add New Buses", pady=10, fg="black",bg="plum1", font="arial").grid(row=0,column=6)
    
    name=StringVar()
    lname=Label(root1, text="Full Name : ").grid(row=1,column=2)
    name=Entry(root1, textvariable=name).grid(row=1,column=4)
    
    
    number=StringVar()
    lnumber=Label(root1, text="Contact Number : ").grid(row=3,column=2)
    number=Entry(root1, textvariable=number).grid(row=3,column=4)
    
    
    address=StringVar()
    laddress=Label(root1,text="Address : ").grid(row=5,column=2)
    address=Entry(root1,textvariable=address).grid(row=5,column=4)
    
    
    b4=Button(root1, text="Details", command=details).grid(row=7,column=3)
    b6=Button(root1, fg="black" ,text="close", command=root1.destroy).grid(row=8,column=20)
def details():
    root2=Tk()
    root2.geometry("750x750")
    bus_type=StringVar()
    lbt=Label(root2, text="Bus Type : ")
    bus_type = Entry(root2)
    
    Start=StringVar()
    lf=Label(root2, text="From : ")
    Start=Entry(root2)
    
    End=StringVar()
    lt=Label(root2, text="To : ")
    End=Entry(root2)
    
    Date=StringVar()
    ld=Label(root2, text="Date : ")
    Date=Entry(root2)
    
    dt=StringVar()
    ldt=Label(root2, text="Departure Time : ")
    dt=Entry(root2)
    
    at=StringVar()
    lat=Label(root2, text="Arrival Time : ")
    at=Entry(root2)
    
    fare=StringVar()
    lfare=Label(root2, text="Fare : ")
    fare=Entry(root2)
    
    seats=StringVar()
    ls=Label(root2, text="Seats : ")
    seats=Entry(root2)
        
    b3=Button(root2, text="Save",command=lambda:savedata(bus_type, Start, End, Date, dt, at, fare, seats)).grid(row=28,column=3)
    b7=Button(root2, fg="black" ,text="close", command=root2.destroy).grid(row=8,column=20)
    lbt.grid(row=10,column=2)
    bus_type.grid(row=10,column=4)
    lf.grid(row=12,column=2)
    Start.grid(row=12,column=4)
    End.grid(row=14,column=4)
    lt.grid(row=14,column=2)
    ld.grid(row=16,column=2)
    Date.grid(row=16,column=4)
    ldt.grid(row=18,column=2)
    dt.grid(row=18,column=4)
    lat.grid(row=20,column=2)
    at.grid(row=20,column=4)
    lfare.grid(row=22,column=2)
    fare.grid(row=22,column=4)
    ls.grid(row=24,column=2)
    seats.grid(row=24,column=4)
def savedata(bus_type,Start,End,Date,dt,at,fare,seats):
    conn=sqlite3.connect('busb.db')
    c=conn.cursor()
    c.execute('''INSERT INTO BUS(
        "BUS TYPE", START, END, DATE, "DEPARTURE TIME", "ARRIVAL TIME", FARE, SEATS)
        VALUES (?,?,?,?,?,?,?,?) ''' ,(
            bus_type.get(),
            Start.get(),
            End.get(),
            Date.get(),
            dt.get(),
            at.get(),
            fare.get(),
            seats.get()
        ))
    conn.commit()
    print("Information stored!")
def book():
    root3=Tk()
    root3.geometry("750x750")
    Label(root3, text="USER PORTAL: SEARCH BUSES", pady=10, fg="black",bg="plum1", font="arial").grid(row=0,column=5)
    Label(root3, text="Enter Details ->", font="default 14 bold").grid(row=4,column=5)
    
    
    Label(root3, text="Bus Type").grid(row=5,column=0)
    selected=StringVar()
    selected.set("Bus Type")
    drop=OptionMenu(root3, selected, "AC", "Non-AC", "AC-SLeeper", "Non-AC Sleeper", "All Types")
    
    a1=StringVar()
    a=Label(root3, text="Start :")
    a1=Entry(root3)
    
    b1=StringVar()
    b=Label(root3, text="End : ")
    b1=Entry(root3)
    
    c1=StringVar()
    c=Label(root3, text="Date")
    c1=Entry(root3)
    
    bt1= Button(root3, text="book", command=lambda:fltr(selected.get(), a1.get(), b1.get(), c1.get()))
    b8=Button(root3, fg="black" ,text="close", command=root3.destroy).grid(row=8,column=20)
    drop.grid(row=5,column=3)
    a.grid(row=6,column=0)
    b.grid(row=7,column=0)
    c.grid(row=8,column=0)
    a1.grid(row=6,column=3)
    b1.grid(row=7,column=3)
    c1.grid(row=8,column=3)
    bt1.grid(row=12,column=5)

def fltr(selected,a1,b1,c1):
    root4=Tk()
    root4.geometry("750x750")
    
    Label(root4,text="Bus Booking Service", bg= "hot pink", fg="white",pady=20, font="arial").grid(row=1,column=5)
    Label(root4, text="BUSES AVAILABLE ->", pady=10, fg="blue", font="default 16 bold ").grid(row=3,column=5)

    c.execute('''SELECT * FROM BUS WHERE("BUS TYPE"=? AND START=? AND END=? AND DATE=?) ''' ,(
        selected,
        a1,
        b1,
        c1
    ))
    buses=c.fetchall()

    dis_bt_label = Label(root4, text="BUS TYPE", font="bold")
    dis_bt_label.grid(row=7,column=1)
    dis_s_label = Label(root4, text="START", font="bold")
    dis_s_label.grid(row=7,column=2)
    dis_e_label = Label(root4, text="END", font="bold")
    dis_e_label.grid(row=7,column=3)
    dis_date_label = Label(root4, text="DATE", font="bold")
    dis_date_label.grid(row=7,column=4)
    dis_dt_label = Label(root4, text="DEPARTURE TIME", font="bold")
    dis_dt_label.grid(row=7,column=5)
    dis_at_label = Label(root4, text="ARRIVAL TIME", font="bold")
    dis_at_label.grid(row=7,column=6)
    dis_fare_label = Label(root4, text="FARE", font="bold")
    dis_fare_label.grid(row=7,column=7)
    dis_seats_label = Label(root4, text="SEATS", font="bold")
    dis_seats_label.grid(row=7,column=8)
    
    print_buses = ''
    for row in buses[0]:
        print_buses += str(row) + " "
    bus_label = Label(root4, text=print_buses).grid(row=8,column=1)


    conn.commit()
Label(text="Bus Booking Service", bg= "hot pink", fg="black",pady=20, font="arial")
main_w.configure(bg="plum1")
a=PhotoImage(file="bus1.gif")
a=a.subsample(1,1)
Label(main_w,image=a,bg="plum1").grid(row=7,column=25) 



b1= Button(main_w, fg="black" ,text="Add", command=add).grid(row=8,column=10)

b2=Button(main_w, fg="black" ,text="close", command=main_w.destroy).grid(row=8,column=20)
b3=Button(main_w, fg="black" ,text="book", command=book).grid(row=8,column=30)




main_w.mainloop()
