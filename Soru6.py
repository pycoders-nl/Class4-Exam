# hesap.py dosyasindaki islemler ve bakiye degerlerini import edin
# islemler listesini okuyup sirasiyla islem tipi ve miktarina gore hesaptaki tutari guncelleyen bir kod yazin.
# her bir adimi, olusturdugunuz 'islemler.txt' dosyasina yeni birer satir olarak ekleyin. orn. islem tipi para cekme, tutar=100 => txt dosyasinda
# gorunmesi gereken satir + 100
# eger islem tipi para cekme ise ve cekilmek istenen miktar halihazirda hesapta olan bakiyeden fazla ise, raise kullanarak exception olusturun ve "hesapta yeterli miktar yoktur"
# benzeri bir hata mesaji printleyin.
# en son adimda hesaptaki guncel tutari txt dosyasina yazin (bakiye: miktar) seklinde.
# tum bu akisi dosya acma/kapama islemleri ve try-except yontemi ile yapin.

# tum kod neticesinde olusturmaniz gereken islemler.txt dosyasinin icerigi asagidaki gibi olmalidir:
# + 100
# + 200
# - 50
# + 100
# - 250
# + 30
# bakiye: 130

# tum kod neticesinde terminalde gorunmesi gereken degerler:
# hesapta yeterli bakiye yoktur
# bakiye: 130

from hesap import *

operations = open('islemler.txt', 'w')

for i in islemler:
    if i['islem_tipi'] == 'para_yatirma':
        bakiye += i['miktar']
        operations.write(f"+{i['miktar']}\n")
    elif i['islem_tipi'] == 'para_cekme':
        if bakiye < i['miktar']:
            print('Unsufficiant amount in the account')
        else:
            bakiye -= i['miktar']
            operations.write(f"-{i['miktar']}\n")

operations.write(f"bakiye:{bakiye}")

print('bakiye', bakiye)
