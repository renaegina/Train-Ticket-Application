from tkinter import *
from tkcalendar import *
import tkinter.ttk as ttk
from tkinter import messagebox
import time
import calendar
from datetime import datetime


def move_text():
    current_text = lbl1.cget("text")
    new_text = current_text[1:] + current_text[0]
    lbl1.config(text=new_text)
    jndl.after(200, move_text)

def validate_nohp_input(char):
    return char.isdigit() or char == ""  # Hanya izinkan angka atau string kosong

def change_cursor(event):
    cal.config(cursor="hand2")

def restore_cursor(event):
    cal.config(cursor="")

def change_cursor_hand(event):
    jndl.config(cursor="hand2")

def restore_cursor_default(event):
    jndl.config(cursor="")


jndl = Tk()
jndl.geometry("1500x800")
jndl.title("TRAIN TICKET APPLICATION")


def info():
    nama = tbNama.get()
    nohp = tbNohp.get()

    if nama == "":
        messagebox.showinfo("MDN TRAIN TICKET APK", "Oops! It looks like you forgot to fill in the name, please fill it in first!")
    elif nohp == "":
        messagebox.showinfo("MDN TRAIN TICKET APK", "Hm, your phone number is still empty. Let's fill it in now!")
    else:
        tampilkan(nama, nohp)

        frm5 = Frame(frm1, width="1100", height="450", bd=0, relief="sunken", bg="linen")
        frm5.place(x=300, y=180)
        lblPlh = Label(frm1, text="Explore Your Destinations", font=("Times New Roman", 36, "bold"), fg="black", bg="linen")
        lblPlh.place(x=505, y=165)

        bgbtn1 = Button(frm1, image=bg1, command=rute1)
        bgbtn2 = Button(frm1, image=bg2, command=rute2)
        bgbtn3 = Button(frm1, image=bg3, command=rute3)
        bgbtn1.place(x=350, y=265)
        bgbtn2.place(x=700, y=265)
        bgbtn3.place(x=1050, y=265)

def tampilkan(nama, nohp):
    tbOutputNama.configure(text=nama, anchor="e")
    tbOutputNohp.configure(text=nohp, anchor="e")

def rute1():
    v = IntVar()
    v.set(v.get())
    jasa = 2000

    def back():
        frm4.destroy()
        img5.destroy()
        lbl4.destroy()
        backbtn.destroy()
        nextbtn.destroy()

    def next():
        global harga
        namaa = tbNama.get()
        nohpp = tbNohp.get()
        jlh = scl.get()
        tgl = cal.get_date()
        plh = v.get()

        def cancel():
            frm5.destroy()
            tbOutputNama2.destroy()
            tbOutputNohp2.destroy()
            tbOutputTkt.destroy()
            outputcal.destroy()
            outputHrg.destroy()
            outputTtl.destroy()
            lblOutputNohp2.destroy()
            lblOutputNama2.destroy()
            lblOutputTkt.destroy()
            lblcal.destroy()
            lblHrg.destroy()
            lblTtl.destroy()
            rute1()

        def done():
            messagebox.askokcancel("MDN Train Ticket APK", "If all the data is correct, please proceed with the payment by showing this receipt.\n"
                                    "Thank you")

        if plh == 0:
            messagebox.showinfo("MDN Train Ticket APK", "Please choose your destination and train.\n"
                                "If your choice is not listed, please wait for the next schedule.\n"
                                "Thank you")
        elif plh == 1:
            harga = 170000
        elif plh == 2:
            harga = 150000

        Ttl = jlh * harga
        frm5 = Frame(jndl, width="600", height="652", bd=0, relief="sunken", bg="slategrey")
        tbOutputNama2 = Label(frm5, width=42, text="", font=("Times New Roman", 16, "bold"), fg="black", bg="linen")
        tbOutputNohp2 = Label(frm5, width=42, text="", font=("Times New Roman", 16, "bold"), fg="black", bg="linen")
        tbOutputTkt = Label(frm5, width=42, text="", font=("Times New Roman", 16, "bold"), fg="black", bg="linen")
        outputcal = Label(frm5, width=42, text="", font=("Times New Roman", 16, "bold"), fg="black", bg="linen")
        outputHrg = Label(frm5, width=42, text=harga, font=("Times New Roman", 16, "bold"), fg="black", bg="linen", anchor="w")
        outputTtl = Label(frm5, width=42, text="", font=("Times New Roman", 16, "bold"), fg="black", bg="linen", anchor="w")
        tbOutputNama2.configure(text=namaa, anchor="w")
        tbOutputNohp2.configure(text=nohpp, anchor="w")
        tbOutputTkt.configure(text=jlh, anchor="w")
        outputcal.configure(text=tgl, anchor="w")
        outputTtl.configure(text=Ttl, anchor="w")

        frm5.place(x=840, y=85)
        lblstrk = Label(frm5, text="PAYMENT", font=("Times New Roman", 16, "bold"), fg="Black", bg="slategrey")
        lblstrk.place(x=230, y=0)

        lblOutputNohp2 = Label(frm5, text="No.Hp", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblOutputNohp2.place(x=10, y=125)
        tbOutputNohp2.place(x=10, y=165)
        lblOutputNama2 = Label(frm5, text="Name", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblOutputNama2.place(x=10, y=45)
        tbOutputNama2.place(x=10, y=85)
        lblOutputTkt = Label(frm5, text="Tickets", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblOutputTkt.place(x=10, y=205)
        tbOutputTkt.place(x=10, y=245)
        lblcal = Label(frm5, text="Departure day", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblcal.place(x=10, y=285)
        outputcal.place(x=10, y=325)
        lblHrg = Label(frm5, text="Ticket Price", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblHrg.place(x=10, y=365)
        outputHrg.place(x=10, y=405)
        lblTtl = Label(frm5, text="Total Payment", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblTtl.place(x=10, y=445)
        outputTtl.place(x=10, y=485)
        proceedbtn = Button(frm5, width=12, text="CANCEL", font=("IMPACT", 17), fg="white", bg="midnightblue", activebackground="white", bd=0, command=cancel)
        proceedbtn.place(relx=0.33, rely=0.9, anchor="center")
        proceedbtn.bind("<Enter>", change_cursor_hand)
        proceedbtn.bind("<Leave>", restore_cursor_default)
        cancelbtn = Button(frm5, width=12, text="DONE", font=("IMPACT", 17), fg="white", bg="darkorange", activebackground="white", bd=0, command=done)
        cancelbtn.place(relx=0.67, rely=0.9, anchor="center")
        cancelbtn.bind("<Enter>", change_cursor_hand)
        cancelbtn.bind("<Leave>", restore_cursor_default)

    frm4 = Frame(frm1, width="1100", height="450", bd=0, relief="sunken", bg="linen")
    frm4.place(x=300, y=180)
    img5 = Label(frm4, image=tabl1, relief="flat")
    img5.place(x=100, y=200)
    lbl4 = Label(frm4, text="Please Choose a Train That Fits Your Destination", font=("Times New Roman", 20, "bold"),bg="linen")
    lbl4.place(x=170, y=50)
    backbtn = Button(frm4, width=7, text="<Back", font=("IMPACT", 18, "italic"), fg="slategray", bg="linen", bd=0, command=back)
    backbtn.place(x=100, y=125)
    Radiobutton(img5, text="", font=("Times New Roman", 12, "bold"), variable=v, value=1, bg="snow", command=lambda: clicked(v.get())).place(x=800, y=43)
    Radiobutton(img5, text="", font=("Times New Roman", 12, "bold"), variable=v, value=2, bg="snow", command=lambda: clicked(v.get())).place(x=800, y=80)
    nextbtn = Button(frm4, width=7, text="Next>", font=("IMPACT", 18, "italic"), fg="slategray", bg="linen", bd=0, command=next)
    nextbtn.place(x=875, y=125)


def rute2():
    v = IntVar()
    v.set(v.get())
    jasa = 2000

    def back():
        frm4.destroy()
        img5.destroy()
        lbl4.destroy()
        backbtn.destroy()
        nextbtn.destroy()

    def next():
        global harga
        namaa = tbNama.get()
        nohpp = tbNohp.get()
        jlh = scl.get()
        tgl = cal.get_date()
        plh = v.get()

        def cancel():
            frm5.destroy()
            tbOutputNama2.destroy()
            tbOutputNohp2.destroy()
            tbOutputTkt.destroy()
            outputcal.destroy()
            outputHrg.destroy()
            outputTtl.destroy()
            lblOutputNohp2.destroy()
            lblOutputNama2.destroy()
            lblOutputTkt.destroy()
            lblcal.destroy()
            lblHrg.destroy()
            lblTtl.destroy()
            rute2()
        
        
        def done():
            messagebox.askokcancel("MDN Train Ticket APK", "If all the data is correct, please proceed with the payment by showing this receipt.\n"
                                    "Thank you")

        if plh == 0:
            messagebox.showinfo("MDN Train Ticket APK", "Please choose your destination and train.\n"
                                "If your choice is not listed, please wait for the next schedule.\n"
                                "Thank you")
        elif plh == 1:
            harga = 24000
        elif plh == 2:
            harga = 125000
        elif plh == 3:
            harga = 150000

        Ttl = jlh * harga
        frm5 = Frame(jndl, width="600", height="652", bd=0, relief="sunken", bg="slategrey")
        tbOutputNama2 = Label(frm5, width=42, text="", font=("Times New Roman", 16, "bold"), fg="black", bg="linen")
        tbOutputNohp2 = Label(frm5, width=42, text="", font=("Times New Roman", 16, "bold"), fg="black", bg="linen")
        tbOutputTkt = Label(frm5, width=42, text="", font=("Times New Roman", 16, "bold"), fg="black", bg="linen")
        outputcal = Label(frm5, width=42, text="", font=("Times New Roman", 16, "bold"), fg="black", bg="linen")
        outputHrg = Label(frm5, width=42, text=harga, font=("Times New Roman", 16, "bold"), fg="black", bg="linen", anchor="w")
        outputTtl = Label(frm5, width=42, text="", font=("Times New Roman", 16, "bold"), fg="black", bg="linen", anchor="w")
        tbOutputNama2.configure(text=namaa, anchor="w")
        tbOutputNohp2.configure(text=nohpp, anchor="w")
        tbOutputTkt.configure(text=jlh, anchor="w")
        outputcal.configure(text=tgl, anchor="w")
        outputTtl.configure(text=Ttl, anchor="w")

        frm5.place(x=840, y=85)
        lblstrk = Label(frm5, text="PAYMENT", font=("Times New Roman", 16, "bold"), fg="Black", bg="slategrey")
        lblstrk.place(x=230, y=0)

        lblOutputNohp2 = Label(frm5, text="No.Hp", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblOutputNohp2.place(x=10, y=125)
        tbOutputNohp2.place(x=10, y=165)
        lblOutputNama2 = Label(frm5, text="Name", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblOutputNama2.place(x=10, y=45)
        tbOutputNama2.place(x=10, y=85)
        lblOutputTkt = Label(frm5, text="Tickets", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblOutputTkt.place(x=10, y=205)
        tbOutputTkt.place(x=10, y=245)
        lblcal = Label(frm5, text="Departure day", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblcal.place(x=10, y=285)
        outputcal.place(x=10, y=325)
        lblHrg = Label(frm5, text="Ticket Price", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblHrg.place(x=10, y=365)
        outputHrg.place(x=10, y=405)
        lblTtl = Label(frm5, text="Total Payment", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblTtl.place(x=10, y=445)
        outputTtl.place(x=10, y=485)
        proceedbtn = Button(frm5, width=12, text="CANCEL", font=("IMPACT", 17), fg="white", bg="midnightblue",
                            activebackground="white", bd=0, command=cancel)
        proceedbtn.place(relx=0.33, rely=0.9, anchor="center")
        proceedbtn.bind("<Enter>", change_cursor_hand)
        proceedbtn.bind("<Leave>", restore_cursor_default)
        cancelbtn = Button(frm5, width=12, text="DONE", font=("IMPACT", 17), fg="white", bg="darkorange", activebackground="white", bd=0, command=done)
        cancelbtn.place(relx=0.67, rely=0.9, anchor="center")
        cancelbtn.bind("<Enter>", change_cursor_hand)
        cancelbtn.bind("<Leave>", restore_cursor_default)

    frm4 = Frame(frm1, width="1100", height="450", bd=0, relief="sunken", bg="linen")
    frm4.place(x=300, y=180)
    img5 = Label(frm4, image=tabl2, relief="flat")
    img5.place(x=100, y=200)
    lbl4 = Label(frm4, text="Please Choose a Train That Fits Your Destination", font=("Times New Roman", 20, "bold"), bg="linen")
    lbl4.place(x=170, y=50)
    backbtn = Button(frm4, width=7, text="<Back", font=("IMPACT", 18, "italic"), fg="slategray", bg="linen", bd=0, command=back)
    backbtn.place(x=100, y=125)
    Radiobutton(img5, text="", font=("Times New Roman", 12, "bold"), variable=v, value=1, bg="snow",
                command=lambda: clicked(v.get())).place(x=800, y=43)
    Radiobutton(img5, text="", font=("Times New Roman", 12, "bold"), variable=v, value=2, bg="snow",
                command=lambda: clicked(v.get())).place(x=800, y=80)
    Radiobutton(img5, text="", font=("Times New Roman", 12, "bold"), variable=v, value=3, bg="snow",
                command=lambda: clicked(v.get())).place(x=800, y=117)
    nextbtn = Button(frm4, width=7, text="Next>", font=("IMPACT", 18, "italic"), fg="slategray", bg="linen", bd=0, command=next)
    nextbtn.place(x=875, y=125)


def rute3():
    v = IntVar()
    v.set(v.get())
    jasa = 2000

    def back():
        frm4.destroy()
        img5.destroy()
        lbl4.destroy()
        backbtn.destroy()
        nextbtn.destroy()

    def next():
        global harga
        namaa = tbNama.get()
        nohpp = tbNohp.get()
        jlh = scl.get()
        tgl = cal.get_date()
        plh = v.get()

        def cancel():
            frm5.destroy()
            tbOutputNama2.destroy()
            tbOutputNohp2.destroy()
            tbOutputTkt.destroy()
            outputcal.destroy()
            outputHrg.destroy()
            outputTtl.destroy()
            lblOutputNohp2.destroy()
            lblOutputNama2.destroy()
            lblOutputTkt.destroy()
            lblcal.destroy()
            lblHrg.destroy()
            lblTtl.destroy()
            rute3()

        def done():
            messagebox.askokcancel("MDN Train Ticket APK", "If all the data is correct, please proceed with the payment by showing this receipt.\n"
                                    "Thank you")

        if plh == 0:
            messagebox.showinfo("MDN Train Ticket APK", "Please choose your destination and train.\n"
                                "If your choice is not listed, please wait for the next schedule.\n"
                                "Thank you")
        elif plh == 1:
            harga = 22000
        elif plh == 2:
            harga = 24000
        elif plh == 3:
            harga = 70000
        elif plh == 4:
            harga = 100000
        elif plh == 5:
            harga = 100000

        Ttl = jlh * harga
        frm5 = Frame(jndl, width="600", height="652", bd=0, relief="sunken", bg="slategrey")
        tbOutputNama2 = Label(frm5, width=42, text="", font=("Times New Roman", 16, "bold"), fg="black", bg="linen")
        tbOutputNohp2 = Label(frm5, width=42, text="", font=("Times New Roman", 16, "bold"), fg="black", bg="linen")
        tbOutputTkt = Label(frm5, width=42, text="", font=("Times New Roman", 16, "bold"), fg="black", bg="linen")
        outputcal = Label(frm5, width=42, text="", font=("Times New Roman", 16, "bold"), fg="black", bg="linen")
        outputHrg = Label(frm5, width=42, text=harga, font=("Times New Roman", 16, "bold"), fg="black", bg="linen", anchor="w")
        outputTtl = Label(frm5, width=42, text="", font=("Times New Roman", 16, "bold"), fg="black", bg="linen", anchor="w")
        tbOutputNama2.configure(text=namaa, anchor="w")
        tbOutputNohp2.configure(text=nohpp, anchor="w")
        tbOutputTkt.configure(text=jlh, anchor="w")
        outputcal.configure(text=tgl, anchor="w")
        outputTtl.configure(text=Ttl, anchor="w")

        frm5.place(x=840, y=85)
        lblstrk = Label(frm5, text="PAYMENT", font=("Times New Roman", 16, "bold"), fg="Black", bg="slategrey")
        lblstrk.place(x=230, y=0)

        lblOutputNohp2 = Label(frm5, text="No.Hp", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblOutputNohp2.place(x=10, y=125)
        tbOutputNohp2.place(x=10, y=165)
        lblOutputNama2 = Label(frm5, text="Name", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblOutputNama2.place(x=10, y=45)
        tbOutputNama2.place(x=10, y=85)
        lblOutputTkt = Label(frm5, text="Tickets", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblOutputTkt.place(x=10, y=205)
        tbOutputTkt.place(x=10, y=245)
        lblcal = Label(frm5, text="Departure day", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblcal.place(x=10, y=285)
        outputcal.place(x=10, y=325)
        lblHrg = Label(frm5, text="Ticket Price", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblHrg.place(x=10, y=365)
        outputHrg.place(x=10, y=405)
        lblTtl = Label(frm5, text="Total Payment", font=("Times New Roman", 16, "bold"), fg="black", bg="slategrey")
        lblTtl.place(x=10, y=445)
        outputTtl.place(x=10, y=485)
        proceedbtn = Button(frm5, width=12, text="CANCEL", font=("IMPACT", 17), fg="white", bg="midnightblue",
                            activebackground="white", bd=0, command=cancel)
        proceedbtn.place(relx=0.33, rely=0.9, anchor="center")
        proceedbtn.bind("<Enter>", change_cursor_hand)
        proceedbtn.bind("<Leave>", restore_cursor_default)
        cancelbtn = Button(frm5, width=12, text="DONE", font=("IMPACT", 17), fg="white", bg="darkorange", activebackground="white", bd=0, command=done)
        cancelbtn.place(relx=0.67, rely=0.9, anchor="center")
        cancelbtn.bind("<Enter>", change_cursor_hand)
        cancelbtn.bind("<Leave>", restore_cursor_default)

    frm4 = Frame(frm1, width="1100", height="450", bd=0, relief="sunken", bg="linen")
    frm4.place(x=300, y=180)
    img5 = Label(frm4, image=tabl3, relief="flat")
    img5.place(x=100, y=200)
    lbl4 = Label(frm4, text="Please Choose a Train That Fits Your Destination", font=("Times New Roman", 20, "bold"), bg="linen")
    lbl4.place(x=170, y=50)
    backbtn = Button(frm4, width=7, text="<Back", font=("IMPACT", 18, "italic"), fg="slategray", bg="linen", bd=0, command=back)
    backbtn.place(x=100, y=125)
    Radiobutton(img5, text="", font=("Times New Roman", 12, "bold"), variable=v, value=1, bg="snow",
                command=lambda: clicked(v.get())).place(x=800, y=43)
    Radiobutton(img5, text="", font=("Times New Roman", 12, "bold"), variable=v, value=2, bg="snow",
                command=lambda: clicked(v.get())).place(x=800, y=80)
    Radiobutton(img5, text="", font=("Times New Roman", 12, "bold"), variable=v, value=3, bg="snow",
                command=lambda: clicked(v.get())).place(x=800, y=117)
    Radiobutton(img5, text="", font=("Times New Roman", 12, "bold"), variable=v, value=4, bg="snow",
                command=lambda: clicked(v.get())).place(x=800, y=154)
    Radiobutton(img5, text="", font=("Times New Roman", 12, "bold"), variable=v, value=5, bg="snow",
                command=lambda: clicked(v.get())).place(x=800, y=191)
    nextbtn = Button(frm4, width=7, text="Next>", font=("IMPACT", 18, "italic"), fg="slategray", bg="linen", bd=0, command=next)
    nextbtn.place(x=875, y=125)

MAC = PhotoImage(file="MACC.png")
img = Label(image=MAC, relief="flat")
img.place(x=0, y=0)

tabl1 = PhotoImage(file="Aeklobaa.png")
tabl2 = PhotoImage(file="Bandarkalipaah.png")
tabl3 = PhotoImage(file="Tebing Tinggi.png")

frm1 = Frame(jndl, width="1377", height="682", bd=0, relief="sunken", bg="linen")
frm1.place(x=62, y=55)
frm2 = Frame(jndl, width="330", height="682", bd=0, relief="flat", bg="slategray")
frm2.place(x=62, y=55)
frm3 = Frame(jndl, width="1379", height="30", bd=0, relief="ridge", bg="black")
frm3.place(x=62,y=55)
frm4 = Frame(frm1, width="1100", height="450", bd=0, relief="sunken", bg="linen")

bg1 = PhotoImage(file="AEKLOBA.png")
img2 = Label(frm1, image=bg1, relief="flat")
bg2 = PhotoImage(file="BANDARKALIPAH.png")
img3 = Label(frm1, image=bg2, relief="flat")
bg3 = PhotoImage(file="TBINGTINGGI.png")
img4 = Label(frm1, image=bg3, relief="flat")

lbl1 = Label(jndl, text="M E D A N  R A I L W A Y  S T A T I O N  -  M D N", font=("Rubik Burned", 12, "bold"), fg="green", bg="black")
lbl1.pack(pady=55)
lbl2 = Label(frm2, text="Purchaser Details", font=("Times New Roman", 18, "bold"), bg="slategray")
lbl2.place(x=50, y=60)

lblNama = Label(frm2, text="Name", font=("Times New Roman", 14, "bold"), fg="black", bg="slategray")
tbNama = Entry(frm2, width=27, font=("Times New Roman", 12, "bold"), bg="white")
lblNama.place(x=20, y=120)
tbNama.place(x=23, y=150)


lblNohp = Label(frm2, text="No.Hp", font=("Times New Roman", 14, "bold"), fg="black", bg="slategray")
tbNohp = Entry(frm2, width=27, font=("Times New Roman", 12, "bold"), bg="white", validate="key", validatecommand=(validate_nohp_input, '%S'))
lblNohp.place(x=20, y=190)
tbNohp.place(x=23, y=220)

lblPenumpang = Label(frm2, text="Tickets", font=("Times New Roman", 14, "bold"), fg="black", bg="slategray")
lblPenumpang.place(x=20, y=260)
scl = Scale(frm2, from_=1, to=50, orien=HORIZONTAL, bg="darkorange")
scl.set(1)
scl.place(x=23, y=290)

lblHari = Label(frm2, text="Departure Day", font=("Times New Roman", 14, "bold"), fg="black", bg="slategray")
lblHari.place(x=20, y=360)

tbOutputNohp = Label(frm1, width=66, text="", font=("Times New Roman", 10, "bold"), fg="slategray", bg="linen")
tbOutputNohp.place(x=900, y=65)
tbOutputNama = Label(frm1, width=42, text="", font=("Times New Roman", 14, "bold"), fg="slategray", bg="linen")
tbOutputNama.place(x=900, y=40)

tblSubmit = Button(frm2, width=34, text="SUBMIT", font=("IMPACT", 14), bg="darkorange", command=info)
tblSubmit.configure(cursor="hand2")
tblSubmit.place(x=-35, y=640)

localtime = time.asctime( time.localtime(time.time()) )
lblTime = Label(frm1, text=localtime, font=("Times New Roman", 13, "bold"), fg="black", bg="linen")
lblTime.place(x=1130, y=645)

cal_date = datetime.now().date()
cal = Calendar(frm2, selectmode="day", year=cal_date.year, month=cal_date.month, day=cal_date.day)
cal.place(x=25, y=400)

cal.bind("<Enter>", change_cursor)
cal.bind("<Leave>", restore_cursor)

# Panggil fungsi move_text untuk memulai pergerakan teks
move_text()
jndl.mainloop()
