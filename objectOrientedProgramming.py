class Mobil:
    def __init__(self, kecepatan, waktu):
        self.kecepatan = kecepatan
        self.waktu = waktu
        
    def hitung_jarak(self):
        print("\nJarak = Kecepatan * Waktu")
        print("Kecepatan = ", self.kecepatan, "\nWaktu = ", self.waktu)
        jarak = self.kecepatan * self.waktu
        print("Jarak yang ditempuh = ", jarak)
        
# Membuat objek Mobil
mobil1 = Mobil(5, 3)
mobil2 = Mobil(7, 5)

# Menghitung jarak yang ditempuh
mobil1.hitung_jarak()
mobil2.hitung_jarak()
