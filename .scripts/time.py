import datetime

delta = datetime.timedelta(hours = 2)
print((datetime.datetime.now() - delta).strftime(' %H:%M  '))
