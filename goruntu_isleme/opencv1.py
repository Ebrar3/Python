import cv2
resim=cv2.imread("goruntu_isleme/dog.jpeg")
cv2.imshow("Kopek",resim)
cv2.waitKey(1000)
yukseklik,genislik,kanallar=resim.shape
print("Yukseklik:",yukseklik)
print("Genislik:",genislik)
print("Kanallar:",kanallar)

farkli_boyut=cv2.resize(resim,(genislik//2,yukseklik//2)) 
cv2.imshow("kirpma",farkli_boyut)
cv2.waitKey(1000)

kirpma=resim[50:350,20:100]
cv2.imshow("Kirpma",kirpma)
cv2.waitKey(100)

goruntu=cv2.imread("goruntu_isleme/dog.jpeg")
p1=(10,50)
p2=(50,150)
cv2.line(goruntu,p1,p2,(0,255,0),5) # Yeşil çizgi
cv2.imshow("Cizgi",goruntu)
cv2.waitKey(0)