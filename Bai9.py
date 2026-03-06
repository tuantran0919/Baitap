import math

x = float(input("Nhập góc (phút): "))

deg = x / 60               # đổi phút → độ
rad = math.radians(deg)   # đổi độ → radian

# xác định góc phần tư
g = deg % 360
if 0 <= g < 90:
    print("Góc phần tư 1")
elif g < 180:
    print("Góc phần tư 2")
elif g < 270:
    print("Góc phần tư 3")
else:
    print("Góc phần tư 4")

print("cos(x) =", math.cos(rad))
