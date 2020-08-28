class Student:
    def __init__(self, _ad,_soyad, _username,_pass):
        self.ad=_ad
        self.soyad=_soyad
        self.username=_username
        self.password=_pass
    def show(self):
        print(f"Ad:{self.ad}, soyad:{self.soyad}, username:{self.username}, password:{self.password}")