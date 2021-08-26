class Hallo:
    def __init__(self, nama):
        self.nama = nama


# cara pertama

    def PanggilNama(self):
        return self.nama

# cara kedua
    def PanggilNamaPrint(self):
        print(self.nama)

# cara ketiga
    def PanggilAngka(self, angka):
        return "ini angka " + str(angka)


lampungKode = Hallo('Hallo semuaaa!')


print('cara pertama')
print(lampungKode.PanggilNama())

print('\ncara kedua')
lampungKode.PanggilNamaPrint()

print('\ncara ketiga')
print(lampungKode.PanggilAngka(5))
