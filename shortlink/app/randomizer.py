import datetime
import random

def short_random():
    #assigning letters to month and hour numbers
    month_letters = {"01":"a","02":"b","03":"c","04":"d","05":"e","06":"f","07":"g","08":"h","09":"x","10":"j","11":"k","12":"z"}
    hour_letters = {"01":"a","02":"b","03":"c","04":"d","05":"e","06":"f","07":"g","08":"h","09":"x","10":"j","11":"k","12":"z","13":"m","14":"n","15":"o","16":"p","17":"q","18":"r","19":"s","20":"t","21":"u","22":"v","23":"w","24":"x"}
    number_letters = {"0":"a","1":"b","2":"c","3":"d","4":"e","5":"f","6":"g","7":"h","8":"x","9":"j"}
    #get last digit of current year
    year_digits = datetime.datetime.now().strftime("%Y")
    year_last_digit = year_digits[-1]
    #creat shortcut string
    shortcut_string = ""
    shortcut_string += random.choice('abcdefghjkmnopqrstuvwxyz')
    shortcut_string += hour_letters[datetime.datetime.now().strftime("%H")]
    shortcut_string += random.choice('abcdefghjkmnopqrstuvwxyz')
    shortcut_string += number_letters[year_last_digit]
    shortcut_string += random.choice('abcdefghjkmnopqrstuvwxyz')
    shortcut_string += month_letters[datetime.datetime.now().strftime("%m")]
    return shortcut_string
