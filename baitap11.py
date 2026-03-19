import random

u = input("b/d/k: ")
c = random.choice("bdk")
print("May:", c)

if u == c:
    print("Hoa")
elif (u=='b' and c=='d') or (u=='d' and c=='k') or (u=='k' and c=='b'):
    print("Ban thang")
else:
    print("Ban thua")
