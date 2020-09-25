
import datetime


class Event:
    def __init__(self, title, *args, **kwargs):
        self.title = title
        self.date = datetime.date.today()

        for key, value in kwargs.items():
            setattr(key, value)

    def __str__(self):
        return self.title
