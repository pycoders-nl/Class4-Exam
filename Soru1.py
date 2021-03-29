# 2000 ve 3200 sayilari arasinda (2000 ve 3200 dahil) 7'ye tam bolunebilen fakat 5'in kati olmayan tum sayilari
# aralarinda virgul olacak sekilde tek satirda terminale bastirin.

numbers = [str(x) for x in range(200, 3201) if x % 7 == 0 and x % 5 != 0]

print(', '.join(numbers))
