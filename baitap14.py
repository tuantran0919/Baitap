import datetime

d,m,y = map(int,input("Nhap d m y: ").split())

t = datetime.date(y,m,d)

print("Ngay sau:", (t+datetime.timedelta(1)).day,
      (t+datetime.timedelta(1)).month,
      (t+datetime.timedelta(1)).year)

print("Ngay truoc:", (t-datetime.timedelta(1)).day,
      (t-datetime.timedelta(1)).month,
      (t-datetime.timedelta(1)).year)
