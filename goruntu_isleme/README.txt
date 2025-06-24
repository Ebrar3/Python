Merhaba 
Bu projede görüntü işlemeye girişeceğiz.
ilk önce OpenCv modülünü kurmamız gerekiyor: "pip install opencv-python " kodu ile (terminalde)
projemizin içine bir görsel koyalım mesela dog.jpeg var bende.

python dosyamıza yazmaya başlıyoruz...
benimki opencv1.py dosyası
ilk önce import etmeliyiz opencv modülünü: import cv2
sonra görüntütyü okumalıyız: cv2.imread("dog.jpeg")            kodu ile
bunu bir değşkene daha doğrusu matrise atarız ben resim'e atadım: resim=cv2.imread("dog.jpeg") 
şimdi resim matrisini kullanmaya geldi, şimdi bir fonksiyon öğreneceğiz imshow fonksiyornu,
bu fonksiyon iki parametre alır. Biri resmin gösterileceği pencerenin adı diğer ise kullanılacak resim matrisi
kullanımı şöyle: cv2.imshow("Kopek",resim)      
Kopek adlı bir pencere çıkacak karşımıza ama hemen kapanacak. 

***Not: eğer error verirse dosya klasörüyle görüntüyü tekrar okutup sorun çözülebilir. bende hata çıktı ve şöyle düzelttim: resim=cv2.imread("goruntu_isleme/dog.jpeg")***

Eğer kapanmasını istemiyorsak cv2.waitKey(0) ile ben bir tuşa basana kadar açık kalır ama belli bir süre dursun istiyorsak o zaman milisaniye cinsinden waitkey in içine yazarız
mesela 1 saniye olsun stersek cv2.waitKey(1000) yazarız

Şimdi görüntümüzün yükseklik,genişlik ve kanal sayısına ulaşmada: resim.shape ile 3 değer de tuple cinsinden döndürür eğer tek tek değişkenlere atamak istiyorsak benim gibi üç değişkeni de yazar öyle assign ederiz.
yukseklik,genislik,kanallar=resim.shape   ile

Görüntünün boyutunu değiştirebiliriz. resize fonksiyonu ile: farkli_boyut=cv2.resize(resim,(genislik//2,yukseklik//2)) 
aynı görüntü olucak sadece boyutu değiştirilmiş halde.
görüntülemek içinse bu boyutta: cv2.imshow("kirpma",farkli_boyut) kodlarını yazdık.
tekrardan waitKey ekledik.

belirli bir bölgeyi kırpabiliriz:
mesela: kirpma=resim[50:350,20:100]
bu ne demek? 50.satırdan 350ye, 20.sütundan 100e kadar seç yani kırp demek.
görüntülersek cv2.imshow("kirpma",kirpma)  ile sonucu görürüz.

#çizim fonksiyonları:
line() fonksiyonu çizgi çizmek için kullanırız.
line(matris_degiskeni,bas_nokta,bit_nokta,renk,kalinlik)    şeklindedir
renk BGR (blue,green,red) şeklindedir (255,0,0) yazarsak bu mavi olur mesela
ben beyaz yapacağım o yüzden (255,255,255) yazacağım. 
