from Calisan import Calisan
#kalitim yoluyla beyazyaka sinifi olustur.
class BeyazYaka(Calisan):
    # private degiskenleri tanimla.
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, deneyim, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, deneyim, maas)
        self.__tesvik_primi = tesvik_primi

    # get/set metotlarini olustur.
    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi
    
    # zam hakkini hesapla.
    def zam_hakki(self):
        try:
            if self.get_deneyim() <= 2:
                return (self.get_maas() * self.get_deneyim()) + self.__tesvik_primi
            elif 2 < self.get_deneyim() <= 4 and self.get_maas() < 15000:
                return (self.get_maas() * self.get_deneyim() / 100) * 5 + self.__tesvik_primi
            elif self.get_deneyim() > 4 and self.get_maas() < 25000:
                return (self.get_maas() * self.get_deneyim() / 100) * 4 + self.__tesvik_primi
            else:
                return self.get_maas()
        except Exception as e:
            return f"Hata: {e}"

    # bilgileri ekrana yazdir.
    def __str__(self):
        try:
            return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrube: {self.get_deneyim()}\nYeni Maas: {self.zam_hakki()}"
        except Exception as e:
            return f"Hata: {e}"


