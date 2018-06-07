import pytz
from datetime import datetime


tz = pytz.timezone('US/Eastern')
now = datetime.now(tz)

print now