# -*- coding: utf-8 -*-

def selamVer(isim = "ziyaretçi"):
    print("Merhaba "+isim)
    
selamVer("Semih")

def selamVer2(isim,soyIsim="arkadaş"):
    print("Merhaba "+isim+" "+soyIsim)
    
selamVer2("Engin")


def alanHesabi(a,b):
    x=a*b
    return x

alan=alanHesabi(5, 8)
print(alan)