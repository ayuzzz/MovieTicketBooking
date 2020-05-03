from Models.slots import slots
from Repository.TheatresRepository import TheatreRepository


class TheatreService:
    theatreRepo = TheatreRepository()

    def getalltheatres(self):
        return self.theatreRepo.getalltheatredetails()

    def insertSlotDetails(self, slotArray):
        slotsList = []

        for row in slotArray:
            slotObject = slots()
            slotObject.MovieId = int(row['MovieId'])
            slotObject.TheatreId = int(row['TheatreId'])
            slotObject.RateOfTickets = row['RateOfTickets']
            slotObject.StartTime = row['StartTime']
            slotObject.EndTime = row['EndTime']
            slotsList.append(slotObject)

        return self.theatreRepo.insertSlotDetails(slotsList)
