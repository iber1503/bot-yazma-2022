#metot.range()
#range fonksiyonunu belli bir aralaıkta bulunan sayıları
#döndürmek için kullanırız

#1-10 arasındaki saılardan oluşan bir liste

liste = list(range(1,10))
print(liste)

#Ekrana 50 defa phyton yazdıralım
#1.phyton

for sayi in range(50):

    print(f"{sayi+1}.Phyton")

    #metot: enumerate()
    #İngilizcede enumerate kelimesi numaralandırmak anlamına gelir
    #Fonksiyonun görevi nesne elemanlaırnı numaralandırarak döndürmek

    #"phyton" kelimesinin karakterlerini enumarete
    #ile numaralandırıp ekrana yazdıralım
    kelime = "phyton"
    kelime_enum = list(enumerate(kelime))
    print(kelime_enum)

    for index,harf in enumerate(kelime):
        print(index,harf)

        #metot zip()
        #zip listeleri birleştirme işlemi yapar
        # #sayılardan ve o sayıların okunuşlarından oluşan 2 liste oluşturalım
# sayilar= [1,2,3]

okunuslar= ["bir"]["iki"]["üç"]

        #bu listeleri zip() ile birleştirelim
        sayilar_zip = list(zip(sayilar,okunuslar))
        print(sayilar_zip)

        #for döngüsü içinde sayıları ve okunusları ekrana yazdıralım
        for sayi,okunus in zip (sayilar,okunuslar):
            print(sayi,okunus)

