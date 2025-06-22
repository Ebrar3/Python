#Silindir Hacmi ve Yüzey Alanı Hesaplama Programı
import math
def s_hacim(r,h):
    return math.pi * pow(r,2) * h

def s_yuzey_alani(r,h):
    return 2 * math.pi *r *h + 2*pow(r,2)*math.pi


yari_cap=int(input("silindirin yarıçapını giriniz:"))
yukseklik=int(input("silindirin yüksekliğini giriniz:"))

print(f"Silindirin Hacmi:{s_hacim(yari_cap,yukseklik)}2 \nSilindirin Yüzey Alanı :{s_yuzey_alani(yari_cap,yukseklik)}")
      

