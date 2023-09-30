# -*- coding: utf-8 -*-

ogrenciler=["engin","salih","semih","ali","veli"]

file=open("ogrenciler.txt","a")

for ogrenci in ogrenciler:
    file.write(ogrenci)
    file.write("\n")

file.close()