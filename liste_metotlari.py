sayilar=[9,12,85,32,54]
harfler=["t","c","z","a","s"]


#listenin eleman sayısını bulalım: len(liste)
print(len(sayilar))
print(len(harfler))

#listenin en küçük elamanını bulalım: min()
print(min(sayilar))
print(min(harfler))

#listenin en büyük elamanını bulalım: max()
print(max(sayilar))
print(max(harfler))

#metin ve sayılardan oluşan listleri birleştirip en büyüğünü bulalım
birlesmis= sayilar+ harfler
#TypeError: '>' not supported between instances of 'str' and 'int' sayı ve harf birleşemez HATA
#print(max(birlesmis))
#listenin sonuna yeni eleman ekleyelim:append()
sayilar.append(95)
print(sayilar)

#listenin istediğimiz konumuna yeni eleman ekleyelim:insert()
harfler.insert(2,"b")
print(harfler)

#listenin sonundaki elemanı silelim: pop()
harfler.pop() #yazılmadığı zaman sondaki harfi siler
print(harfler)
harfler.pop(2) #belirli konumdaki b harfi silinir
print(harfler)

#listede belirli bir elemanları silielim: remove("değer")
harfler.append("a")
print(harfler)
harfler.remove("a")
print(harfler)


#listedeki elemanları sıralayalım: sort()
print(sayilar)
sayilar.sort()
#Büyükten küçüğe
print(sayilar())
sayilar.reverse()
print(sayilar)

#Listedeki isimleri alfabetik sıraya göre sıralayalım
isimler=["Eren","Ersin","Hüseyin","Kaan"]
isimler.sort()
print(isimler)

#listeyi temizleyelim:clear()
isimler.clear()
print(isimler)






