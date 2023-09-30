# -*- coding: utf-8 -*-

class Matematik:
    def topla(self,a,b):
        return a+b
    
    
mat=Matematik()
x=mat.topla(14,74)
print(x)


class Mat:
    def __init__(self,sayi1,sayi2):
        self.sayi1=sayi1
        self.sayi2=sayi2
        
    def toplam(self):
        return self.sayi1+self.sayi2
        
    
mat2=Mat(14, 2)
print(mat2.toplam())


class Person:
    def __init__(self,name,family,age):
        self.name=name
        self.family=family
        self.age=age
        

insan1=Person("Ali", "Veli", 32)
print(insan1.family)

class Worker(Person):
    def __init__(self,salary):
        self.salary=salary

insan2=Worker()

        
        
        
        
        