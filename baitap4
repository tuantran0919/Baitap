import math

a, b, c = map(float, input("Nhập a b c: ").split())

if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        loai="Tam giác đều"
    elif a==b or a==c or b==c:
        loai="Tam giác cân"
    elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        loai="Tam giác vuông"
    else:
        loai="Tam giác thường"
        
    p=(a+b+c)/2
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    
    print(loai)
    print("Diện tích:",S)
else:
    print("Không phải tam giác")
