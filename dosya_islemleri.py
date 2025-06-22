dosya=open("deneme.txt","w",encoding="utf-8") # "w" modu dosyayı yazma modunda açar.
dosya.write("Merhaba Dünya")
dosya.write("\nSelamlarr")
dosya.close()
dosya=open("deneme.txt","r",encoding="utf-8") # "r" modu dosyayı okuma modunda açar.
icerik=dosya.readline() # readline() metodu dosyadan bir satır okur.
print(icerik)
dosya.close()
print("\n")
with open("deneme.txt","a",encoding="utf-8") as d: # "a" modu dosyaya ekleme yapar.
    d.write("\nPython Programlama Dili")
with open("deneme.txt","r",encoding="utf-8") as d:
    icerik=d.read()
    print(icerik)
# with kullanımı, dosyayı açıp kapatmayı otomatik olarak yapar.
# Bu sayede dosyayı açık bırakma veya kapatma unutma gibi hatalardan kaçınılır.

