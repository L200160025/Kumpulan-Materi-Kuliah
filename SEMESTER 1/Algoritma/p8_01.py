def jumlah(x):
    "menerima list x dan mengembalikan jumlah dari angka di x"
    J = 0
    for angka in x:
        J = J + angka
    return J

x = jumlah([2, 4, 6])
y = jumlah([1, 7, 2, 2, 4])
a = [1, 5, -2, 4]
print jumlah(a)
