# 6. Can you change the self-parameter inside a class to something else (say
#    “abhi”). Try changing self to “slf” or “abhi” and see the effects.

from random import randint
class Train:
    def __init__(slf, train_number, name, from_station, to_station):   # self replaced with slf
        slf.train_number = train_number
        slf.name = name
        slf.from_station = from_station
        slf.to_station = to_station
        slf.fare = randint(100, 800)

    def book(slf):                                                      #self replaced with slf
        print(f"Your ticket has been booked on Train {slf.train_number} ({slf.name}) "
              f"from {slf.from_station} to {slf.to_station}")

    def status(abhi):                                                   #self replaced with abhi
        print(f"Train {abhi.train_number} ({abhi.name}) is running on time")

    def fare_info(self):
        print(f"Ticket fare from {self.from_station} to {self.to_station} is ₹{self.fare}")


t = Train(12346, "Delhi Express", "Delhi", "Mumbai")
print(t.train_number, t.name, t.from_station, t.to_station, t.fare)

t.book()
t.status()
t.fare_info()

#changing self to “slf” or “abhi” and there are no changes


