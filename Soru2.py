# Kullanici tarafindan girilen n sayisi kadar elemani olan ve elemanlari arasinda (i:i*i) iliskisi bulunan bir sozluk olusturunuz.
# Ornek input: 8
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

num = int(input('Enter a number: '))

obj = {}
for i in range(1, num+1):
    obj[i] = i * i

print(obj)
