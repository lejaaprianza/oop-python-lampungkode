# class Hallo1:
#     def __init__(self):
#         print('hello world')


# lampungkode1 = Hallo1()
# lampungkode2 = Hallo1()
# lampungkode3 = Hallo1()


# class Hallo2:
#     def __init__(self, nama, angka):
#         print('Hello ', nama, 'ini angka', angka)


# lampungkode1 = Hallo2('Lampung', 1)
# lampungkode2 = Hallo2('Kode', 2)
# lampungkode3 = Hallo2('Leja', "mantap")

# class Hallo2:
#     def __init__(self, nama, angka):
#         print('Hello ', nama, 'ini angka', int(angka))


# lampungkode1 = Hallo2('Lampung', 1)
# lampungkode2 = Hallo2('Kode', 2)
# lampungkode3 = Hallo2('Leja', 'mantap')

class Hallo3:
    def __init__(self, nama, angka):
        self.nama = nama
        self.angka = angka


lampungkode1 = Hallo3('Lampung', 1)
lampungkode2 = Hallo3('Kode', 2)
lampungkode3 = Hallo3('Leja', 3)

print('Hallo', lampungkode1.nama)
print('Hallo', lampungkode2.nama)
print('Hallo', lampungkode3.nama)
print('\n')
print('Angka', lampungkode1.angka)
print('Angka', lampungkode2.angka)
print('Angka', lampungkode3.angka)
