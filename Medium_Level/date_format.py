def date_format(date):
  # write your code here
  date1 = date.split('/')
  year, month, day = date1
  
  f1 = date
  f2 = date.replace('/','-')
  f3 = month + '/' + day + '/' + year
  return f"{f1} | {f2} | {f3}"