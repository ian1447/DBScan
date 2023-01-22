from datetime import datetime
import calendar

currentDateAndTime = datetime.now()

t = datetime(currentDateAndTime.year, currentDateAndTime.month, currentDateAndTime.day, currentDateAndTime.hour, currentDateAndTime.minute, currentDateAndTime.second)
epoch = calendar.timegm(t.timetuple())
print(epoch)