class Cellphone:
    def __init__(self, cellphone_num):
        self.cellphone_num = cellphone_num

class Tickets:
    def __init__(self, soccer, movie, theater):
        self.soccer = soccer
        self.movie = movie
        self.theater = theater

tickets = Tickets("Soccer", "Movie", "Theater")

class Number_Tickets:
    def __init__(self, num_tickets):
        self.num_tickets = num_tickets

print(tickets.soccer)
print(tickets.movie)
print(tickets.theater)

ticket = PhotoImage(file="ticket1.jpeg")
img = Label(root, image=ticket)
img.place(x=5, y=5)
