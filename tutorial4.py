class Hallo:
    __privateAngka = 1

    def __init__(self, nama):
        self.nama = nama
        self.__privateDaerah = 'Bandar Lampung'


namaDaerah = Hallo("Metro")

print(namaDaerah.__dict__)
print(Hallo.__dict__)

print(namaDaerah.__privateDaerah)
print(Hallo.__privateAngka)
