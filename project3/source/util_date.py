#Project           : GEDCOM SSW 555 Summer 2019
#Author            : Saransh Ahlawat
#Purpose           : Generic Date class to store birth, death, marriage, etc. dates. Also, it implements user story US27 and US42.
#Revision History  : Version 1.0
# Notes:  This user story checks if assorted dates for individuals occur in the future.

import datetime
import unittest


class DateTest(unittest.TestCase):
    def test_init(self):
        date_1 = Date("5 AUG 2018")
        date_2 = Date("10 JAN 1993")
        date_3 = Date("JAN 2000")
        date_4 = Date("10 1993")
        date_5 = Date("1993")

        self.assertEqual(date_1.date_time_obj.day, 5)
        self.assertEqual(date_1.date_time_obj.month, 8)
        self.assertEqual(date_1.date_time_obj.year, 2018)

        self.assertEqual(date_2.date_time_obj.day, 10)
        self.assertEqual(date_2.date_time_obj.month, 1)
        self.assertEqual(date_2.date_time_obj.year, 1993)

        self.assertEqual(date_3.date_time_obj, "JAN 2000")
        self.assertEqual(date_4.date_time_obj, "10 1993")
        self.assertEqual(date_5.date_time_obj, "1993")

    def test_is_valid_date(self):
        date_1 = Date("5 AUG 2018")
        date_2 = Date("10 JAN 1993")
        date_3 = Date("JAN 2000")
        date_4 = Date("10 1993")
        date_5 = Date("1993")

        self.assertTrue(Date.is_valid_date(date_1.date_time_obj))
        self.assertTrue(Date.is_valid_date(date_2.date_time_obj))
        self.assertFalse(Date.is_valid_date(date_3.date_time_obj))
        self.assertFalse(Date.is_valid_date(date_4.date_time_obj))
        self.assertFalse(Date.is_valid_date(date_5.date_time_obj))

    def test_get_dates_difference(self):
        date_1 = Date("5 AUG 2018")
        date_2 = Date("10 JAN 1993")
        date_3 = Date("5 AUG 2000")
        date_4 = Date("10 JAN 1969")

        self.assertEqual(Date.get_dates_difference(date_2.date_time_obj, date_1.date_time_obj), 24)
        self.assertEqual(Date.get_dates_difference(date_4.date_time_obj, date_3.date_time_obj), 30)
        self.assertEqual(Date.get_dates_difference(date_2.date_time_obj, date_4.date_time_obj), -25)
        self.assertEqual(Date.get_dates_difference(date_2.date_time_obj), 26)
        self.assertEqual(Date.get_dates_difference("NA"), "NA")
        self.assertEqual(Date.get_dates_difference(None), "NA")
        


class Date:

    __slots__ = ["date_time_obj"]

    def __init__(self, date):
        """stores the provided string date value as datetime object if the date format is valid, otherwise stores them as a string
        to keep track to faulty dates as well."""
        try:
            self.date_time_obj = datetime.datetime.strptime(date, "%d %b %Y")
        except ValueError:
            self.date_time_obj = date

    
    def __str__(self):
        if type(self.date_time_obj) is str:
            return self.date_time_obj
        else:
            return f"{self.date_time_obj.strftime('%d %b %Y')}"


    @staticmethod
    def get_dates_difference(date1, date2=None):
        """ User Story: US27
            Description: returns the date difference between two dates. If only 1 date value is provided, the difference is calculated using today's date 
        """
        if type(date1) is str or type(date2) is str or date1 == None:
            return "NA"
        today = datetime.date.today()
        difference = 0
        if date2 == None and date1 != None:
            difference = today.year - date1.year - ((today.month, today.day) < (date1.month, date1.day))
        else:
            if date1 != None:
                difference = date2.year - date1.year - ((date2.month, date2.day) < (date1.month, date1.day))
        return difference

    @staticmethod
    def is_valid_date(date):
        """ User Story: US42
            Description: this function checks whether the date provided is legitimate. It returns True or False as the return response.
        """
        try:
            if type(date) is datetime.datetime:
                return True
            datetime.datetime.strptime(date, "%d %b %Y")
            return True
        except ValueError:
            return False
        except TypeError:
            return False

