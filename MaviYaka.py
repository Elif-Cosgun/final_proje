from Calisan import Calisan
# Kalitim yoluyla MaviYaka sinifini olustur.
class MaviYaka(Calisan):
    # private degiskenleri tanimla.
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, deneyim, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, deneyim, maas)
        self.__yipranma_payi = yipranma_payi

    # get/set metotlarini olustur.
    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

     # zam_hakki method
    def zam_hakki(self):
        try:
            if self.get_deneyim() <= 2:
                return self.get_maas() * (self.__yipranma_payi * 10)
            elif 2 < self.get_deneyim() <= 4 and self.get_maas() < 15000:
                return (self.get_maas() * self.get_deneyim()) / 2 + (self.__yipranma_payi * 10)
            elif self.get_deneyim() > 4 and self.get_maas() < 25000:
                return (self.get_maas() * self.get_deneyim()) / 3 + (self.__yipranma_payi * 10)
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




