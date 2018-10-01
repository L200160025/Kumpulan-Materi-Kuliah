#-----RAHMANDANI-HERLAMBANG-SCRIPT--------------#
"""
Resources:
    - http://www.materisekolah.net/2015/01/rumus-volume-prisma-dan-rumus-luas-prisma.html
    - https://utamiari191.wordpress.com/materi-pembelajaran/
    - http://www.dasarpendidikan.co.id/2013/03/rumus-prisma-luas-volume-prisma.html
    - http://www.berpendidikan.com/2015/05/rumus-luas-permukaan-prisma-volume-serta-contoh-soalnya.html
    - http://www.gudangrumus.com/2014/03/rumus-prisma-segitiga.html
    - http://www.rumusmatematika.org/2015/06/rumus-prisma.html
"""

import math

class PismaSegitiga(object):

    def __init__(self, alas, tinggi_segitiga, tinggi_prisma):
        self.alas = alas
        self.tinggi_segitiga = tinggi_segitiga
        self.tinggi_prisma = tinggi_prisma

    def luas_selubung(self):
        # Dalam kasus segitiga siku-siku
        # (self.alas * self.tinggi_prisma) + (self.tinggi_segitiga * self.tinggi_prisma) + \
        # math.sqrt((self.alas * 2) + (self.tinggi_segitiga * 2)) * self.tinggi_prisma

        # Dalam kasus segitiga sama sisi.
        return 3 * self.alas * self.tinggi_prisma
    
    def luas_prisma(self):
        return (2 * self.alas) + self.luas_selubung()

    def luas_segitiga(self):
        return (self.alas * self.tinggi_segitiga) / 2

    def luas(self):
        return (2 * self.luas_segitiga()) + self.luas_selubung()

    def volume(self):
        return self.luas_segitiga() * self.tinggi_prisma


prisma = PismaSegitiga(20, 5, 10)
print "Luas Selubung :", prisma.luas_selubung()
print "Luas Prisma   :", prisma.luas_prisma()
print "Luas Segitiga :", prisma.luas_segitiga()
print "Luas Prisma Segitiga:", prisma.luas()
print "Luas Volume Segitiga:", prisma.volume()
