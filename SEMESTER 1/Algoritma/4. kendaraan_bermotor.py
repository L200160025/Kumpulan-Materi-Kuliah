#-----RAHMANDANI-HERLAMBANG-SCRIPT--------------#

import datetime

class KendaraanBermotor(object):

    def __init__(self, no_pol, tgl_pajak):
        self.no_pol = no_pol
        #self.tahun = tahun
        self.tgl_pajak = tgl_pajak


    def umur(self):
        tgl_sekarang = datetime.datetime.now().date()
        delta = tgl_sekarang - self.tgl_pajak
        umur = datetime.datetime.fromordinal(delta.days)
        umur_tahun = umur.year - 1
        umur_bulan = umur.month - 1
        umur_tanggal = umur.day
        
        print_out = "Kendaraan plat {0} berumur: {1} hari, atau \n" \
                    "Kendaraan plat {2} berumur: {3} tahun, {4} bulan, {5} hari".format(
                        self.no_pol, delta.days,
                        self.no_pol, umur_tahun, umur_bulan, umur_tanggal
                    )
        return print_out


tanggal_pajak = datetime.date(2016, 11, 21)
print KendaraanBermotor('AD134', tanggal_pajak).umur()

print "-" * 50

tanggal_pajak = datetime.date(2009, 2, 28)
print KendaraanBermotor('AD134', tanggal_pajak).umur()
