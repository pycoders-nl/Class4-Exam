# Input ile alinan bir stringi, harfleri tekrar etmeyecek sekilde ve alfabetik olarak siralayan bir fonksiyon olusturun. Boslugu da dikkate alin.
# Ornek input: 'monty pythons flying circus'
# Ornek output: ' cfghilmnoprstuy'

# Ayni inputu tersten siralayip bir liste haline ceviren bir fonksiyon olusturun.
# Ornek input: 'monty pythons flying circus'
# Ornek output: ['circus', 'flying', 'pythons', 'monty']


def unique_chars():
    string = input('Enter a string: ')
    list_string = sorted(list(set(string)))
    return ''.join(list_string)


# print(unique_chars())


def reverse_order():
    list_words = input('Enter a string: ').split()
    return list_words[::-1]


print(reverse_order())
