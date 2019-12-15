import datetime

delta = datetime.timedelta(hours = 0)
print((datetime.datetime.now() - delta).strftime(' %H:%M  '))
