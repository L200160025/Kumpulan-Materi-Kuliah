
class Karyawan():
    'membuat kelas karyawan'
    email = ''

    def __init__(self, no, nama):
        'mengisi property yang wajib ada'
        self.no_induk = no
        self.nama = nama
    
    def set_email(self, em):
        'mengisi alamat email'
        assert '@' in em, 'penulisan email salah'
        self.email = em

