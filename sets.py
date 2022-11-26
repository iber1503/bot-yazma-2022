"""
sets listeleri süslü parantezler '{}' içinde tanımlanır.
sets liste elemanlarına indeks numaraları ile ulaşılamaz.
sets liste elemanlarına döngü içinde ulaşılır.
sets listeleri içinde aynı eleman birden fazla yer alamaz.
"""
#sets liste oluşuralım

sets_liste ={1,2,3,4}

#sets listesinin içindeki bir elemana ulaşalım
#print(sets_liste[0]) hata verdi

#sets liste elemanlarına döngü ile ulaşalım
for eleman in sets_liste:


""    print(eleman)

#sets listesine bir eleman ekleyelim add()
sets_liste.add(5)
print(sets_liste)

#sets listesine bir veya birden fazla eleman ekleyelim: update([])
sets_liste.update(19,20,21)