#dosyayi ice aktar.
from Insan import Insan

# Kalitim yoluyla Issiz sinifini olustur.
class Issiz(Insan):
    # Private degisken olustur.
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, durumlar):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__durumlar = durumlar
        self.__statu = self.__durum_bul()

    # Get/set metotları olustur.
    def get_durumlar(self):
        return self.__durumlar

    def set_durumlar(self, durumlar):
        self.__durumlar = durumlar
        self.__statu = self.__durum_bul()

    def get_statu(self):
        return self.__statu

    # En uygun statuyu bul.
    def __durum_bul(self):
        try:
            max_etki = 0
            en_uygun_durum = ""
            for durum, yil in self.__durumlar.items():
                if durum == "mavi_yaka":
                    etki = yil * 0.2
                elif durum == "beyaz_yaka":
                    etki = yil * 0.35
                elif durum == "yonetici":
                    etki = yil * 0.45
                else:
                    continue

                if etki > max_etki:
                    max_etki = etki
                    en_uygun_durum = durum

            if en_uygun_durum == "":
                raise ValueError("En uygun durum bulunamadi.")

            return en_uygun_durum

        except Exception as e:
            raise ValueError("Hata:", e)

    # Bilgileri ekrana yazdır.
    def __str__(self):
        try:
            return f"Kullanici: {self.get_ad()} {self.get_soyad()}\nEn uygun durum: {self.get_statu()}"
        except Exception as e:
            return "Hata: Kullanici bilgileri eksik."
