#-----RAHMANDANI-HERLAMBANG-SCRIPT--------------#

class Piramida(object):
    """
    Piramida / Segitiga.
    """
    
    def __init__(self, sisi_alas, tinggi):
        self.sisi_alas = sisi_alas
        self.tinggi = tinggi

    def luas(self):
        segitiga = (self.sisi_alas * self.tinggi) / 2  # 1/2 * ALAS * TINGGI
        persegi  = self.sisi_alas * 2                  # PANJANG * LEBANR
        return segitiga + persegi

    def volume(self):
        return (self.sisi_alas * 2 * self.tinggi) / 3


print "Luas", Piramida(20, 5).luas()
print "Volume", Piramida(20, 5).volume()

