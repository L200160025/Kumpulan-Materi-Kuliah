class Pohon():
    'membuat kelas pohon'
    tinggi = 0
    jenis = 'monokotil'
    
    def set_tinggi(self, t):
        'mengubah property tinggi'
        self.tinggi = t

class Mangga(Pohon):
    'membuat kelas mangga'
    jenis = 'dikotil'
    berbuah = True
    
    def get_tinggi(self):
        'membaca nilai property tinggi'
        return self.tinggi

