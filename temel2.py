mesaj="merhaba"
print(mesaj[2:5])

yeniMesaj=mesaj[:5]
print(yeniMesaj)

if(mesaj.upper()==yeniMesaj.upper()):
    print("aynı")
else:
    print("farkli")

yeniMesaj2=mesaj[len(mesaj)-1:len(mesaj)]
print(yeniMesaj2)

