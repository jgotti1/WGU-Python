import datetime

def currentDate(x):
# Student code goes here
    timeSpan = datetime.timedelta(days=x)
    print(f"The total number of seconds is {timeSpan.total_seconds()}.")

 
currentDate(4) #expected outcome: The total number of seconds is 345600.0.
currentDate(7) #expected outcome: The total number of seconds is 604800.0.