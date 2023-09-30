# -*- coding: utf-8 -*-

dosya=open("musteriler.txt")
#r read, a append, w write, x create, default=r
# print(dosya.read())

print("*************************")

# print(dosya.readline())# tek satır okuma işlemi

for i in dosya:
    print(i)
    
    
dosya.close()