
class DayPlan:
    # Constructor
    location = ""
    event = []
    destination = []
    data = {'location': location, 'event':event, 'destination':destination }
    def __init__(self, location, event = [],destination = []):
        self.location = location
        self.event = event
        self.destination = destination
        setData()
    def __str__(self):
        return str(self.data)
    def addDestination(self, destination):
        self.destination.append(destination)
    def setData():
        self.data = {'location': location, 'event':event, 'destination':destination }
