from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Ticket Sales")
root.geometry("400x700")
root.config(bg="navy")

canvas = Canvas(root, width=300, height=225)
canvas.pack()
img = PhotoImage(file="ticket1.png")
canvas.create_image(20, 10, anchor=NW, image=img)
canvas.config(bg="navy")

amount_ans = StringVar()
category_ans = StringVar()
ticket_amount = StringVar()
Contact = StringVar()

soccer = 40.00
film = 75.00
theater = 100.00

cellphone_lab = Label(root, text="Enter Cell Number:", bg="white")
cellphone_lab.place(x=15, y=250)

cellphone_entry = Entry(root, width=20)
cellphone_entry.place(x=150, y=250)

Category_lab = Label(root, text="Select Ticket Category:", bg="white")
Category_lab.place(x=15, y=300)

n = StringVar
comboBox = ttk.Combobox(root, textvariable=n)
comboBox['values'] = ('Soccer', 'Movies', 'Theatre')
comboBox.place(x=180, y=300)

Ticket_number = Label(root, text="Number of Tickets Bought", bg="white")
Ticket_number.place(x=15, y=350)

Ticket_spinbox = Spinbox(root, from_=0, to=10, width=3)
Ticket_spinbox.place(x=200, y=350)

def clear():
    cellphone_entry.delete(0, END)
    comboBox.delete(0, END)

def calculate():
    if comboBox.get() == "Soccer":
        result = float(Ticket_spinbox.get()) * 40.00 * 0.14
        amount_ans.set(round(result))

    elif comboBox.get() == "Movies":
        result = float(Ticket_spinbox.get()) * 75.00 * 0.14
        amount_ans.set(round(result))

    elif comboBox.get() == "Theater":
        result = float(Ticket_spinbox.get()) * 100.00 - (0.14 * 100.00)
        amount_ans.set(round(result))


Calculate_btn = Button(root, text="Calculate Ticket", bg="white", command=calculate)
Calculate_btn.place(x=15, y=400)

Clear_btn = Button(root, text="Clear Entries", bg="white", command=clear)
Clear_btn.place(x=150, y=400)

X_lab = Label(root, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", bg="white")
X_lab.place(x=15, y=450)

Amount_lab = Label(root, text="Amount Payable:", bg="white")
Amount_lab.place(x=15, y=500)

Amount = Label(root, bg="white", width=15, height=1, textvariable=amount_ans)
Amount.place(x=150, y=500)

Reservation_lab = Label(root, text="A Reservation for:", bg="white")
Reservation_lab.place(x=15, y=550)

Answer_lab = Label(root, bg="white", width=15, height=1)
Answer_lab.place(x=150, y=550)

Reserved_lab = Label(root, text="Reserved for:", bg="white", width=15, height=1)
Reserved_lab.place(x=15, y=600)

Answer_lab = Label(root, bg="white", width=15, height=1)
Answer_lab.place(x=150, y=600)

X_lab = Label(root, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", bg="white")
X_lab.place(x=15, y=650)

mainloop()
