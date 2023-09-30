
ogrenciler=["engin","derin","salih"]
ogrenciler.append("ahmet")
print(ogrenciler)
print(ogrenciler[3])
ogrenciler.remove("salih")
print(ogrenciler)

sehirler=list(("Ankara","İstanbul","Ankara"))
print(sehirler)
print(len(sehirler))

print("Ankara sayısı: "+str(sehirler.count("Ankara")))
print("Ankara indexi: "+str(sehirler.index("Ankara")))

sehirler.pop(1)
sehirler.insert(0, "İstanbul")
print(sehirler)
sehirler.reverse()
print(sehirler)

sehirler2=sehirler
sehirler3=sehirler.copy()

sehirler2[0]="İzmir"



print(sehirler)
print(sehirler3)

sehirler.extend(sehirler3)
sehirler.sort()

print(sehirler)


