import datetime

d = int(input("Ngày: "))
m = int(input("Tháng: "))
y = int(input("Năm: "))

try:
    date = datetime.date(y, m, d)
    print("Ngày hợp lệ")

    thu = date.weekday()   # 0=Thứ 2 ... 6=Chủ nhật
    ds = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật"]
    print("→", ds[thu])

except:
    print("Ngày KHÔNG hợp lệ")
