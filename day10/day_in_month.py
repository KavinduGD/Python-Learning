def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  

def days_in_month(y,m):
  """This Function is created for getting the days count of a month \n
  author name- Kavindu Gihan"""
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  
  leap=is_leap(y)
  
  if not leap:
      return month_days[m-1]
  else:
      if m!=2:
          return month_days[m-1]
      else:
          return 29
        

"""oh my god e""" 

year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)



