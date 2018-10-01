# Program demo membuat kelas/objek

class PersegiPanjang():
    """ Kelas bangun geometri persegi panjang
    krb: tuple berisi koordinat kiri bawah
    kna: tuple berisi koordinat kanan atas """
    krb = (0, 0)
    kna = (2, 1)

    def luas(self):
        "menghitung luas persegi panjang"
        pj = self.kna[0] - self.krb[0]  # panjang
        lb = self.kna[1] - self.krb[1]  # lebar
        L = pj * lb  # luas = panjang * lebar
        return L

    def keliling(self):
        "menghitung keliling persegi panjang"
        pj = self.kna[0] - self.krb[0]  # panjang
        lb = self.kna[1] - self.krb[1]  # lebar
        K = 2 * (pj + lb)
        return K


class Persegi():
    """ Kelas bangun geometri persegi panjang
    krb: tuple berisi koordinat kiri bawah
    kna: tuple berisi koordinat kanan atas """
    def __init__(self, krb, kna):
        "nilai property krb dan kna harus diisi saat membuat objek/instance"
        self.krb = krb
        self.kna = kna

    def luas(self):
        "menghitung luas persegi panjang"
        pj = self.kna[0] - self.krb[0]  # panjang
        lb = self.kna[1] - self.krb[1]  # lebar
        L = pj * lb  # luas = panjang * lebar
        return L

    def keliling(self):
        "menghitung keliling persegi panjang"
        pj = self.kna[0] - self.krb[0]  # panjang
        lb = self.kna[1] - self.krb[1]  # lebar
        K = 2 * (pj + lb)
        return K


class PersegiBaru(PersegiPanjang):
    " Kelas turunan "

    def is_portrait(self):
        """mengembalikan True jika persegi panjang portrait"""
        pj = self.kna[0] - self.krb[0]  # panjang
        lb = self.kna[1] - self.krb[1]  # lebar
        if pj < lb:
            return True
        else:
            return False
