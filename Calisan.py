#dosyayi ice aktar.
from Insan import Insan
#kalitim yoluyla calisan sinifi olustur.
class Calisan(Insan):
    #private degiskenleri tanimla.
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, deneyim, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = self.__kontrol_sektor(sektor)
        self.__deneyim = deneyim
        self.__maas = maas

    #hangi sektorde oldugunu bul.
    def __kontrol_sektor(self, sektor):
        sektorler = ["teknoloji", "muhasabe", "insaat", "diger"]
        if sektor in sektorler:
            return sektor
        else:
            return "Gecersiz sektor"

    #get/set metotlari olustur.
    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = self.__kontrol_sektor(sektor)

    def get_deneyim(self):
        return self.__deneyim

    def set_deneyim(self, deneyim):
        self.__deneyim = deneyim

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    #zam hakkini hesapla.
    def zam_hakki(self):
        if self.__deneyim <= 2:
            return 0
        elif 2 < self.__deneyim <= 4 and self.__maas < 15000:
            return (self.__maas * self.__deneyim) / 200
        else:
            return self.get_maas()
        
    #bilgileri yazdir.
    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrube: {self.__deneyim}\nYeni Maas: {self.zam_hakki()}"
