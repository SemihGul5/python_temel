# -*- coding: utf-8 -*-
sehirler=["Ankara","İstanbul","İzmir"]

for sehir in sehirler:
    if sehir !="Ankara":
        print(sehir+" için kod: "+sehir[0:3])
    print("*****************")
    
print("----------------------------------")
for sehir in sehirler:
    if sehir =="İstanbul":
        break
    print(sehir+" için kod: "+sehir[0:3])
    print("*****************")
    
print("----------------------------------")
for sehir in sehirler:
    if sehir =="İstanbul":
        continue
    print(sehir+" için kod: "+sehir[0:3])
    print("*****************")
    
print("----------------------------------")

for i in range(1,10):
    print(i)
    
for i in range(1,10,3):
    print(i)