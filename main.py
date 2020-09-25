
import datetime


class Event:
    def __init__(self, title):
        self.title = title
        self.date = datetime.date.today()

    def __str__(self):
        return self.title
