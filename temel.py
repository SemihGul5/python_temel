mesaj="merhaba dünya"
print(mesaj[2:5])

yeniMesaj=mesaj[:5]
print(yeniMesaj)

if(mesaj.upper()==yeniMesaj.upper()):
    print("aynı")
else:
    print("farkli")

yeniMesaj2=mesaj[len(mesaj)-1:len(mesaj)]
uzunluk=len(mesaj)
print(yeniMesaj2)
print(mesaj[uzunluk-1 : uzunluk])

rplc=mesaj.replace("ü", "u")
print(rplc)

# strip() ise boşlukları atar ilgili değişkende
bilgi=mesaj
print(bilgi.split())
bilgi="merhaba;dünya"
print(bilgi.split(";"))

sayi1= input("Sayı 1: ")
sayi2= input("Sayı 2: ")
print(int(sayi1)+int (sayi2))
