#100 ile 200 arasındaki sayıları numaralar değikenine aktaralım
numaralar=[]
for sayi in range(100,200):
   numaralar.append(sayi)
print(numaralar)

#yukardaki işlemi list comprehsions şeklinde yapalım
numaralar2=[sayi for sayi in range(100,200)]
print(numaralar2)

#100-200 arasındaki çift sayılara bir listeye aktaralım
cift_sayilar=[sayi for sayi in range(100,200)if sayi %2 ==0]
print(cift_sayilar)

numaralar3=[f"{sayi}TEK" if sayi %2 ==1 else f"{sayi}ÇİFT"for sayi in range(100,200)]


liste = [(x, y) for x in range(3) for y in range(3)]

print(liste) 

