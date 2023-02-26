from datetime import datetime
import time

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)
pattern = '%d/%m/%Y %H:%M:%S'
epoch = int(time.mktime(time.strptime(dt_string, pattern)))
print(epoch)