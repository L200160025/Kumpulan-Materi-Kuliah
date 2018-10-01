#-----RAHMANDANI-HERLAMBANG-SCRIPT--------------#

import datetime


class Masa(object):
    
    """
    Menjadikan time delta (baik pengurangan/penambahan) tanggal
    ke sebuah masa.

    Input:
        - time delta
    Output:
        - string masa

    Contoh:
    ------------------------------------------
    >>> import datetime
    >>> dahulu   = datetime.date(2000, 11, 21)
    >>> sekarang = datetime.date(2016, 11, 21) # atau => datetime.datetime.now().date()
    >>> delta = sekarang - dahulu
    >>> delta
    datetime.timedelta(5844)
    >>>
    >>> masa = Masa(delta)
    >>> masa.total_hari()
    5844 hari
    >>> masa.total_tahun()
    15 tahun
    >>> masa.masa_full()
    15 tahun, 11 bulan, 31 hari
    >>>
    ------------------------------------------
    """
    
    def __init__(self, delta):
        self.delta = delta
        self.jumlah_hari = datetime.datetime.fromordinal(self.delta.days)

    def total_hari(self):
        """
        Menampilkan total hari yang dihasilkan dari delta.
        """
        return "{} hari".format(self.delta.days)

    def total_tahun(self):
        """
        Menampilkan total tahun yang dihasilkan dari delta.
        """
        return "{} tahun".format(self.jumlah_hari.year - 1)
    
    def masa_full(self):
        """
        Menampilkan masa secara lengkap, berupa:
        - tahun
        - bulan
        - hari
        """
        return "{0} tahun, {1} bulan, {2} hari".format(
            self.jumlah_hari.year - 1,
            self.jumlah_hari.month - 1,
            self.jumlah_hari.day
        )


class Karyawan(object):

    def __init__(self, nama, tgl_lahir, tgl_masuk):
        self.nama = nama
        self.tgl_lahir = tgl_lahir
        self.tgl_masuk = tgl_masuk

    def tgl_sekarang(self):
        """
        Mengembalikan nilai tanggal saat ini berformat `date`.
        
        Contoh:
            - datetime.date(2016, 11, 23)
        """
        return datetime.datetime.now().date()

    def umur_saat_masuk(self):
        """
        Mengembalikan nilai umur karyawan
        pada saat mulai masuk kerja,
        dengan memanfaatkan class `Masa(delta)`.

        Rumus:
            tanggal masuk - tanggal lahir.
        """
        delta = self.tgl_masuk - self.tgl_lahir
        return Masa(delta) #.masa_full()

    def masa_kerja(self):
        """
        Mengembalikan nilai masa kerja karyawan
        dari mulai masuk kerja sampai saat ini,
        dengan memanfaatkan class `Masa(delta)`.

        Rumus:
            tanggal sekarang - tanggal masuk.
        """
        delta = self.tgl_sekarang() - self.tgl_masuk
        return Masa(delta) #.tahun()

    def informasi_karyawan(self):
        """
        Menampilkan seluruh informasi karyawan.
        - nama
        - tanggal lahir
        - tanggal masuk kerja
        - umur/usia karyawan pada saat masuk kerja, dan
        - masa kerja karyawan dari masuk sampai saat ini:
            - total hari
            - total tahun
            - total masa secara komplit.
        """
        informasi = "Nama      : {0}\n" \
                    "Tgl lahir : {1}\n" \
                    "Tgl masuk : {2}\n" \
                    "-------------------------------------\n" \
                    "Umur karyawan pada saat masuk       : {3} / {4} / ({5})\n" \
                    "Masa kerja karyawan sampai saat ini : {6} / {7} / ({8})".format(
                        self.nama,
                        self.tgl_lahir,
                        self.tgl_masuk,
                        self.umur_saat_masuk().total_hari(),
                        self.umur_saat_masuk().total_tahun(),
                        self.umur_saat_masuk().masa_full(),
                        self.masa_kerja().total_hari(),
                        self.masa_kerja().total_tahun(),
                        self.masa_kerja().masa_full()
                    )
        return informasi


print "-------------------------------------"

nama = "Aldino Kemal"
tgl_lahir = datetime.date(2000, 11, 21)
tgl_masuk = datetime.date(2016, 11, 21)

karyawan = Karyawan(nama, tgl_lahir, tgl_masuk)
print karyawan.informasi_karyawan()
#print Masa(tgl_masuk - tgl_lahir).masa_full()

print help(Masa)
print "-------------------------------------"

