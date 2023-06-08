#main dosyasi
#kutuphane tanimla ve dosyaları ice aktar.
import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

# Insan sinifindan 2 nesne olusturma ve bilgileri __str__ metoduyla ekrana yazdirma
print("\nINSANLAR")
insan1 = Insan("123456789", "Ahmet", "Yilmaz", 30, "Erkek", "Turk")
insan2 = Insan("987654321", "Ayse", "Kara", 25, "Kadin", "Turk")
print(insan1)
print(insan2)

# Issiz sinifindan 3 nesne olusturma ve bilgileri __str__ metoduyla ekrana yazdirma
print("\nISSIZLER")
issiz1 = Issiz("11111111111", "Ahmet", "Yilmaz", 30, "Erkek", "Turk", {"mavi_yaka": 50, "beyaz_yaka": 30, "yonetici": 10})
issiz2 = Issiz("22222222222", "Ayse", "Kara", 25, "Kadin", "Turk", {"mavi_yaka": 20, "beyaz_yaka": 40, "yonetici": 20})
issiz3 = Issiz("33333333333", "Mehmet", "Demir", 35, "Erkek", "Turk", {"mavi_yaka": 10, "beyaz_yaka": 20, "yonetici": 50})
print(issiz1)
print(issiz2)
print(issiz3)

# Calisan sinifindan 3 nesne olusturma ve bilgileri __str__ metoduyla ekrana yazdirma
print("\nCALISANLAR")
calisan1 = Calisan("12345678901", "Ali", "Yilmaz", 30, "Erkek", "Turk", "teknoloji", 3, 27000)
calisan2 = Calisan("98765432109", "Ayse", "Demir", 28, "Kadin", "Turk", "muhasabe", 5, 32000)
calisan3 = Calisan("55555555555", "Mehmet", "Yildiz", 35, "Erkek", "Turk", "diger", 2, 25000)
print(calisan1)
print(calisan2)
print(calisan3)

# MaviYaka sinifindan 3 nesne olusturma ve bilgileri __str__ metoduyla ekrana yazdirma
print("\nMAVI YAKALILAR")
maviyaka1 = MaviYaka("1234567890", "Ali", "Yilmaz", 30, "Erkek", "Turk", "teknoloji", 3, 18000, 0.7)
maviyaka2 = MaviYaka("9876543210", "Ayse", "Kara", 28, "Kadin", "Turk", "insaat", 7, 22000, 0.7)
maviyaka3 = MaviYaka("6543219870", "Mehmet", "Demir", 35, "Erkek", "Turk", "muhasabe", 8, 15000, 0.1)
print(maviyaka1)
print(maviyaka2)
print(maviyaka3)

# BeyazYaka sinifindan 3 nesne olusturma ve bilgileri __str__ metoduyla ekrana yazdirma
print("\nBEYAZ YAKALILAR")
beyazyaka1 = BeyazYaka("12345678910", "Ahmet", "Yildiz", 30, "Erkek", "Turk", "teknoloji", 1, 20000, 15000)
beyazyaka2 = BeyazYaka("12345678911", "Ayse", "Kara", 28, "Kadin", "Turk", "muhasabe", 3, 15000, 13000)
beyazyaka3 = BeyazYaka("12345678912", "Mehmet", "Demir", 35, "Erkek", "Turk", "insaat", 7, 18000, 14000)
print(beyazyaka1)
print(beyazyaka2)
print(beyazyaka3)

# Dataframe olusturma
data = {
    "Nesne": ["Calisan", "Mavi Yaka", "Beyaz Yaka"],
    "TC No": ["123456789", "987654321", "567890123"],
    "Ad": ["Ahmet", "Ayse", "Mehmet"],
    "Soyad": ["Yilmaz", "Kara", "Demir"],
    "Yaş": [30, 25, 35],
    "Cinsiyet": ["Erkek", "Kadin", "Erkek"],
    "Uyruk": ["Turk", "Turk", "Turk"],
    "Sektör": [None, None, None],
    "Tecrübe": [None, None, None],
    "Maaş": [None, None, None],
    "Yipranma Payi": [None, None, None],
    "Tesvik Prim": [None, None, None],
}
df = pd.DataFrame(data)

# Calisan, Mavi Yaka, Beyaz Yaka nesnelerinin degerlerini dataframe'e ekleme
calisan_grup = df["Nesne"] == "Calisan"
maviyaka_grup = df["Nesne"] == "Mavi Yaka"
beyazyaka_grup = df["Nesne"] == "Beyaz Yaka"

df.loc[df["Nesne"] == "Calisan", ["Sektor", "Tecrube", "Maas"]] = [calisan1.get_sektor(), calisan1.get_deneyim(), calisan1.get_maas()]
df.loc[df["Nesne"] == "Calisan", ["Sektor", "Tecrube", "Maas"]] = [calisan2.get_sektor(), calisan2.get_deneyim(), calisan2.get_maas()]
df.loc[df["Nesne"] == "Calisan", ["Sektor", "Tecrube", "Maas"]] = [calisan3.get_sektor(), calisan3.get_deneyim(), calisan3.get_maas()]
df.loc[df["Nesne"] == "Mavi Yaka", ["Sektor", "Tecrube", "Maas", "Yipranma Payi"]] = [maviyaka1.get_sektor(), maviyaka1.get_deneyim(), maviyaka1.get_maas(), maviyaka1.get_yipranma_payi()]
df.loc[df["Nesne"] == "Mavi Yaka", ["Sektor", "Tecrube", "Maas", "Yipranma Payi"]] = [maviyaka2.get_sektor(), maviyaka2.get_deneyim(), maviyaka2.get_maas(), maviyaka2.get_yipranma_payi()]
df.loc[df["Nesne"] == "Mavi Yaka", ["Sektor", "Tecrube", "Maas", "Yipranma Payi"]] = [maviyaka1.get_sektor(), maviyaka3.get_deneyim(), maviyaka3.get_maas(), maviyaka3.get_yipranma_payi()]
df.loc[df["Nesne"] == "Beyaz Yaka", ["Sektor", "Tecrube", "Maas", "Tesvik Prim"]] = [beyazyaka1.get_sektor(), beyazyaka1.get_deneyim(), beyazyaka1.get_maas(), beyazyaka1.get_tesvik_primi()]
df.loc[df["Nesne"] == "Beyaz Yaka", ["Sektor", "Tecrube", "Maas", "Tesvik Prim"]] = [beyazyaka2.get_sektor(), beyazyaka2.get_deneyim(), beyazyaka2.get_maas(), beyazyaka2.get_tesvik_primi()]
df.loc[df["Nesne"] == "Beyaz Yaka", ["Sektor", "Tecrube", "Maas", "Tesvik Prim"]] = [beyazyaka3.get_sektor(), beyazyaka3.get_deneyim(), beyazyaka3.get_maas(), beyazyaka3.get_tesvik_primi()]


# Degerleri bos olan yerlere 0 değerini atama
df = df.fillna(0)

# Calısan, Mavi Yaka, Beyaz Yaka icin tecrube ve yeni maas ortalamalarıini hesaplama ve ekrana yazdirma
calisan_grup = df[df["Nesne"] == "Calisan"]
maviyaka_grup = df[df["Nesne"] == "Mavi Yaka"]
beyazyaka_grup = df[df["Nesne"] == "Beyaz Yaka"]

calisan_tecrube_ort = calisan_grup["Tecrube"].mean()
calisan_yeni_maas_ort = calisan_grup["Maas"].mean()
print("Calisan - Tecrube Ortalamasi:", calisan_tecrube_ort)
print("Calisan - Yeni Maas Ortalamasi:", calisan_yeni_maas_ort)

maviyaka_tecrube_ort = maviyaka_grup["Tecrube"].mean()
maviyaka_yeni_maas_ort = maviyaka_grup["Maas"].mean()
print("Mavi Yaka - Tecrube Ortalamasi:", maviyaka_tecrube_ort)
print("Mavi Yaka - Yeni Maas Ortalamasi:", maviyaka_yeni_maas_ort)

beyazyaka_tecrube_ort = beyazyaka_grup["Tecrube"].mean()
beyazyaka_yeni_maas_ort = beyazyaka_grup["Maas"].mean()
print("Beyaz Yaka - Tecrube Ortalamasi:", beyazyaka_tecrube_ort)
print("Beyaz Yaka - Yeni Maas Ortalamasi:", beyazyaka_yeni_maas_ort)

# Maasi 15000 TL'nin uzerinde olanlarin toplam sayisini bulma
maas_ust_limit = 15000
maas_ust_limit_sayisi = len(df[df["Maas"] > maas_ust_limit])
print("Maasi 15000 TL'nin uzerinde olanlarin sayisi:", maas_ust_limit_sayisi)

# Yeni maasa gore dataframe'i kucukten buyuge siralama ve ekrana yazdirma
print("\nYENI MAAS SIRALAMA")
df = df.sort_values("Maas")
print(df)

# Tecrubesi 3 seneden fazla olan beyaz yakalilarıi bulma ve ekrana yazdirma
print("\nTECRUBESI 3 YILDAN FAZLA OLAN BEYAZ YAKALILAR")
beyazyaka_tecrube_fazla = beyazyaka_grup[beyazyaka_grup["Tecrube"] > 3]
print(beyazyaka_tecrube_fazla)

# Yeni maaşı 10000 TL üzerinde olanların tc no ve yeni maaş sütunlarını seçerek gösterme ve ekrana yazdırma
print("\nYENİ MAASI 10000 TL USTUNDE OLANLAR")
yeni_maas_limit = 10000
yeni_maas_limit_df = df[df["Maas"] > yeni_maas_limit][["TC No", "Maas"]]
print(yeni_maas_limit_df)

# Ad, soyad, sektor ve yeni maası iceren yeni bir dataframe olusturma ve ekrana yazdirma
print("\nYENI DATAFRAME")
yeni_df = df[["Ad", "Soyad", "Sektor", "Maas"]]
print(yeni_df)
