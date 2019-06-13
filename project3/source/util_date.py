import datetime

class Date:

    __slots__ = ["date_time_obj"]

    def __init__(self, date):
        try:
            self.date_time_obj = datetime.datetime.strptime(date, "%d %b %Y")
        except ValueError:
            print("ERROR: The date provided is not in the expected format. Expected 'D M YY'")

    
    def __str__(self):
        return f"{self.date_time_obj.strftime('%d %b %Y')}"


    @staticmethod
    def get_dates_difference(date1, date2=None):
        today = datetime.date.today()
        difference = 0
        if date2 == None and date1 != None:
            difference = today.year - date1.year - ((today.month, today.day) < (date1.month, date1.day))
        else:
            if date1 != None:
                difference = date2.year - date1.year - 1
        return difference if difference > -1 else 0