class Hallo:
    increment = 0

    def __init__(self, nama):
        self.nama = nama
        Hallo.increment += 1

lampungkode1 = Hallo('Lampung')
print('Selamat datang di', lampungkode1.nama)
print(Hallo.increment)
lampungkode2 = Hallo('Bandung')
print('Selamat datang di', lampungkode2.nama)
print(Hallo.increment)
lampungkode3 = Hallo('Majalengka')
print('Selamat datang di', lampungkode3.nama)
print(Hallo.increment)
