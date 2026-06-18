class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"You have booked train {self.trainNo} from {fro} to {to}")

    def trainStatus(self, fro, to):
        print(f"The train {self.trainNo} is running from {fro} to {to}")

booking = Train(13340)
booking.book("Lahore", "Quetta")
booking.trainStatus("Lahore", "Quetta")