#This is a function.
def readable_timedelta(days):
   """To get the number of weeks and days in given number of days"""
   number_of_weeks = days // 7 #To get number of weeks
   number_of_days = days % 7 # To get number of days
   return('{} week(s) and {} day(s)'.format(number_of_weeks, number_of_days))
   
