
#tuple liste ile aynı ama eleman değiştirmeye izin yok


tupleList=(2,4,6,"Ankara",(2,3,4),[])
liste=[2,4,6,"Ankara",[2,3,4],()]

liste[0]=6
tupleDeger=("Engin",)
print(type(tupleDeger))

print(tupleList[1:2])
print(liste[1:2])

print(tupleList[-2])
print(liste[-2])

print(tupleList)
print(liste)