# 5. Write a Class ‘Trainʼ which has methods to book a ticket, get status (no of seats) and get
# fare information of train running under Indian Railways.



class Train:

    def __init__(self, trainNo, trainName, seats, fare):

        self.trainNo = trainNo
        self.trainName = trainName
        self.seats = seats
        self.fare = fare


    # Method to book ticket
    def bookTicket(self):

        if self.seats > 0:

            print("Ticket Booked Successfully")
            self.seats = self.seats - 1

        else:

            print("No Seats Available")


    # Method to check train status
    def getStatus(self):

        print("Train Name:", self.trainName)
        print("Available Seats:", self.seats)


    # Method to get fare information
    def getFareInfo(self):

        print("Fare of Train:", self.fare)



# Creating Object
t = Train(12345, "Rajdhani Express", 2, 1500)


# Train Status
t.getStatus()

# Fare Information
t.getFareInfo()

# Booking Tickets
t.bookTicket()
t.bookTicket()
t.bookTicket()

# Checking Updated Status
t.getStatus()