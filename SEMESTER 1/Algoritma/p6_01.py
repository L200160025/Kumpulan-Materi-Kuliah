##dt = (3, 7, 2.1, 14, 5)
##if dt[-1] > 0:
##    print "data terakhir positif"
##else:
##    print "data terakhir negatif"


##usia = raw_input("Masukkan umur: ")
##if int(usia) > 50:
##    print "Anda sudah tua ;)"
##else:
##    print "Anda masih muda :)"


##angka = int(raw_input("Masukkan angka: "))
##if angka >= 50:
##    print "masuk kategori besar"
##elif 20 <= angka < 50:
##    print "masuk kategori sedang"
##else:
##    print "masuk kategori kecil"


##angka = int(raw_input("Masukkan angka: "))
##if angka >= 77:
##    print "nilai A"
##elif 60 <= angka < 77:
##    print "nilai B"
##elif 50 <= angka < 60:
##    print "nilai C"
##elif 35 <= angka < 50:
##    print "nilai D"
##elif angka < 35:
##    print "nilai E"


# Program menentukan tahun kabisat
# catatan: 2100 bukan kabisat, 1996 dan 2000 adalah kabisat
angka = int(raw_input("Masukkan angka tahun: "))
##if angka % 4 == 0 and angka % 100 == 0:
##    print "bukan tahun kabisat"
##elif angka % 400 == 0:
##    print "tahun kabisat"
if angka % 4 != 0:
    print "bukan kabisat"
elif angka % 100 == 0:
    if angka % 400 != 0:
        print "bukan kabisat"
    else:
        print "tahun kabisat"
else:
    print "tahun kabisat"
