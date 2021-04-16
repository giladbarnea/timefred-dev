from datetime import datetime as dt
dt_today: dt = dt.today()
def today():
	return dt_today.strftime('%a %b %d %G')

def now():
	return dt_today.strftime("%X")