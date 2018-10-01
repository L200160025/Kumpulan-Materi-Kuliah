#-----RAHMANDANI-HERLAMBANG-SCRIPT--------------#

# RUMUS Eclips
# GAMBAR Eclips

#      0000000000
#    00    |     00
#   0------|-------0    ECLIPS BUKAN LINGKARAN
#    00    |     00
#      0000000000
#
# SUMBU MAYOR ADALAH JARI JARI TERPANJANG
# SUMBU MINOR JARI JARI SATUNYA

# Pada gambar diatas Sumbu mayor adalah -------------

# Sumbu minor adalah |
#                    |
#                    |

# RUMUS LUAS = phi * minor(jari jari) * mayor(jari jari)
# RUMUS eksentrisitas = c / a, dimana c = akar (a^2 - b^2) | a = mayor


from math import sqrt


class Ellips():
    
##    def __init__(self, minor, mayor):
##        self.minor = minor
##        self.mayor = mayor

    def luas(self , minor, mayor):
        return 3.14 * minor * mayor

    def eksentrisitas(self, mayor , minor):
        c = sqrt((mayor ** 2) - (minor ** 2))
        return float(c / mayor)


minor = 4
mayor = 5
print Ellips().luas(20,20)
##print "Luas", Ellips(minor, mayor).luas()
##print "Eksentrisitas", Ellips(minor, mayor).eksentrisitas()



























"""
import math

class Ellips(object):
    #http://opencvpython.blogspot.co.id/2012/04/contour-features.html
    
    def __init__(self, minor, mayor):
        self.minor = min(minor)
        self.mayor = max(mayor)

    def luas(self):
        return ''

    def eksentrisitas(self):
        return math.sqrt(1-(self.minor/self.mayor)**2)



minor = [-1, -2, -3, -4]
mayor = [1, 2, 3, 4]
print Ellips(minor, mayor).eksentrisitas()
"""
