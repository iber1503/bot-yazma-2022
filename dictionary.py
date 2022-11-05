"""
Dictionary "anahtar", "değer" ikililerinden oluşur
    "ad": "Eren"
    "soyad": "Özdal"
"""

#belirli bir numaraya sahip öğrenciyi bulma işlemini liste ile yapalım
#numaralar=[66,75]
#isimler=["Ahmet","Mehmet"]
#numara=int(input("Öğrenci numarası yazınız:"))
#konum=numaralar.index(numara)
#print(isimler[konum]) karşımasın diye

##belirli bir numaraya sahip öğrenciyi bulma işlemini DİCTİONARY ile yapalım
#ogrenciler={66:"Ahmet",75:"Mehmet"}
#print(ogrenciler[numara])





#detaylı örnek
kisiler= {
1: {
  "ad":"Eren",
  "soyad":"Gönden",
  "cinsiyet":"Erkek",
  "dersler":["Türkçe","Matematik"]
},
45:{
    "ad":"Ahmet",
    "soyad":"Gönden",
    "cinsiyet":"Erkek",
    "dersler":["Görsel Sanatlar",["Türkçe"]]
}
}
print(kisiler[1]["dersler"])

print(kisiler[45]["cinsiyet"])


