#asal sayı bulma programı
def asal_mi(sayi):
    if sayi==1 or sayi==0:
        return False
    elif sayi==2:
        return True
    else:
        for i in range (2,int(sayi**0.5)+1):
            if sayi %i==0:
                return False
        return True
    
# Kullanıcıdan sayı alma
sayi = int(input("Bir sayı giriniz: "))

print(f"{sayi} sayısı asal mı? {asal_mi(sayi)}")