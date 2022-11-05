liste=[1,2,3]
tuple=("bir","iki","üç")
#tuple'ı ekarana yazdıralım
print(liste)
print(type(liste))
print(tuple)
print(type(tuple))

#belirli bir elemanı ekrana yazdıralım
print(tuple[0])


#listenin tuple'ı bir elemanını değiştirelim
liste[0]=7
print(liste)
#tuple[0]="yedi" TypeError: 'tuple' object does not support item assignment hata verdiiiiiiiiiiiiii
print(tuple)

#tuple içindeki belirli bir elemanın indexini bulalım:index()
print(tuple.index("iki"))

#iki tuple'ı birleştirelim
tuple1=(1,2,3)
tuple2="bir","iki","üç"
print(tuple1)+(tuple2)