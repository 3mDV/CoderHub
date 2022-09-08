from typing import List
from datetime import date
def timePeriod(date1: str, date2: str) -> bool:
    # write your code here ^_^
    today = date.today()
    date1 = date1[:date1.index("T")].split("-")
    date1 = date(int(date1[0]), int(date1[1]), int(date1[2]))
    date2 = date2[:date2.index("T")].split("-")
    date2 = date(int(date2[0]), int(date2[1]), int(date2[2]))
    return date1 < date2 < today > date1
