# # 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# # and get fare information of train running under Indian Railways.

from random import randint
class Train:
    def __init__(self, train_number, name, from_station, to_station):
        self.train_number = train_number
        self.name = name
        self.from_station = from_station
        self.to_station = to_station
        self.fare = randint(100, 800)

    def book(self):
        print(f"Your ticket has been booked on Train {self.train_number} ({self.name}) "
              f"from {self.from_station} to {self.to_station}")

    def status(self):
        print(f"Train {self.train_number} ({self.name}) is running on time")

    def fare_info(self):
        print(f"Ticket fare from {self.from_station} to {self.to_station} is ₹{self.fare}")

t = Train(12346, "Delhi Express", "Delhi", "Mumbai")
print(t.train_number, t.name, t.from_station, t.to_station, t.fare)
t.book()
t.status()
t.fare_info()