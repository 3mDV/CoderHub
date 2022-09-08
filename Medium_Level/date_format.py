def date_format(date):
    # write your code here
    date1 = date.split('/')
    year, month, day = date1
  
    dt1 = date
    dt2 = date.replace('/','-')
    dt3 = month + '/' + day + '/' + year
    return f"{dt1} | {dt2} | {dt3}"

