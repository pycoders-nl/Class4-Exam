# En az iki metodu olan bir Class olusturunuz.
# 1.metot =>  inputAl: Kullanicidan input alma.
# 2.metot =>  yazdir: Alinan inputu terminale buyuk harflerle yazdirma metodu.

class Person:

    def input_al(self):
        name = input('Enter Your name: ')
        self.name = name

    def print(self):
        print(f'Hi, {self.name}. Nice to meet you.')
