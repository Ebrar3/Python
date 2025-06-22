# diskriminant/delta hesaplama ile kök bulma programı
from math import sqrt
def diskriminant(a,b,c):
    delta= b**2 - 4*a*c
    if delta < 0:
        print("Kök yoktur.")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"çift katlı Kök: {x}")
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print(f"Kökler: {x1} ve {x2}")

# ax2 +bx+ c =0 
a=float(input("a katsayısını giriniz:"))
b=float(input("b katsayısını giriniz:"))
c=float(input("c katsayısını giriniz:"))
diskriminant(a,b,c)