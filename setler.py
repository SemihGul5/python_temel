# indexsiz ve sırasızdır
# tüm elemanlar eşsizdir

studentSet={"Engin","Derin","Salih","Ahmet"}
studentSet2=set({"Ali","Veli"})
print(studentSet)
print(studentSet2)


for students in studentSet:
    print(students)

print("Derin" in studentSet)

if "Derin" in studentSet:
    print("Var")
else:
    print("Yok")
    
studentSet.add("Ali")
print(studentSet)

studentSet.update(["Merve","Mert"])
print(studentSet)

print(len(studentSet))

studentSet.remove("Merve")
print(len(studentSet))

studentSet.discard("Mert")#yoksa hata çıkartmıyor
print(len(studentSet))

del studentSet


setA={1,2,3}
setB={2,3,4,5}
print(setA.union(setB))
print(setA.intersection(setB))





