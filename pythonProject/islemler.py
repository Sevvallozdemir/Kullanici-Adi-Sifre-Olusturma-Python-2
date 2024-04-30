def kullaniciAdi_sifre_uret():
    with open("bil104--projekullanicilar.txt", "r", encoding="utf-8") as file:
        satirlar = file.readlines()

    a = satirlar[1].split(',')

    i = 1
    satirsayisi = len(satirlar)
    yeni_liste = []
    while i < satirsayisi:
        a = satirlar[i].split(',')

        i += 1
        yeni_liste.append(a)
    for i in yeni_liste:
        n = int(input("Kullanıcı adı ve şifresini oluşturmak istediğiniz kişinin id'sini giriniz:"))
        with open("kullaniciAdi_sifre.txt", "a", encoding="utf-8") as file:
            file.write(str(n) + ",")
        bilgiler = yeni_liste[n - 1]
        print("Bilgiler:", bilgiler)
        break
    isim = bilgiler[1]
    soyisim = bilgiler[2]
    dogum_tarihi = bilgiler[3]
    adım1 = isim[1] + isim[3]
    son_uc_karakter = soyisim[len(soyisim) - 3:]
    adım2 = [son_uc_karakter[0], soyisim[0].lower(), son_uc_karakter[2]]
    adım2 = ''.join(adım2)
    adım3 = int(bilgiler[3][0]) + int(bilgiler[3][1]) + int(bilgiler[3][6]) + int(bilgiler[3][7]) + int(
        bilgiler[3][8]) + int(bilgiler[3][9])
    adım3 = str(adım3) + bilgiler[3][8] + bilgiler[3][9]
    kullanici_adi = adım2 + adım1 + adım3
    print("Kullanici adı:", kullanici_adi)
    with open("kullaniciAdi_sifre.txt", "a", encoding="utf-8") as file:
        file.write(str(kullanici_adi) + ",")

    import random

    with open("bil104--projekullanicilar.txt", "r", encoding="utf-8") as file:
        satirlar = file.readlines()

    i = 1
    satirsayisi = len(satirlar)
    yeni_liste = []
    while i < satirsayisi:
        a = satirlar[i].split(',')

        i += 1
        yeni_liste.append(a)
    for i in yeni_liste:
        bilgiler = yeni_liste[n - 1]

        break

    isim = bilgiler[1]
    adım1 = isim[0] + isim[-1].title()
    soyisim = bilgiler[2]
    son_iki_harf = soyisim[-2:]
    karakter_dizisi = "*, /, !, _, (, ), &, %, +, -, ., virgül, <,>"
    rastgele_karakter = random.choice(karakter_dizisi)
    son_iki_harf_list = list(son_iki_harf)
    son_iki_harf_list[0] = rastgele_karakter
    son_iki_harf = ''.join(son_iki_harf_list)
    adım2 = son_iki_harf
    dogum_tarihi = bilgiler[3]
    adım3 = dogum_tarihi[8] + dogum_tarihi[9] + str(int(dogum_tarihi[3] + dogum_tarihi[4]) ** 2)
    kesik_s = bilgiler[4][1:-2]
    adım4 = kesik_s[0].upper() + kesik_s[1:-1] + kesik_s[-1].upper()
    rastgele_iki_basamakli = random.randint(10, 99)
    print(rastgele_iki_basamakli)
    adım5 = rastgele_iki_basamakli
    sifre = str(adım4) + str(adım5) + str(adım1) + str(adım3) + str(adım2)
    print("Sifre:", sifre)
    with open("kullaniciAdi_sifre.txt", "a", encoding="utf-8") as file:
        file.write(sifre + "\n")

    return (sifre)


def kullanici_getir():
    with open("bil104--projekullanicilar.txt", "r", encoding="utf-8") as file:
        while True:
            try:
                file.seek(0)
                satirlar = file.readlines()
                n = int(input("Bilgilerini görmek istediğiniz kullanıcının id'sini giriniz:"))
                print(satirlar[n])
                break
            except IndexError:
                print("Girdiğiniz ID'ye ait bir kullanıcı yok.Lütfen geçerli bir id giriniz:")


def yeni_kullanici():
    with open("bil104--projekullanicilar.txt", "a", encoding="utf-8") as file:
        file.write(input("İd:") + ",")
        file.write(input("İsim:") + ",")
        file.write(input("Soyisim:") + ",")
        file.write(input("Dogum Tarihi:") + ",")
        file.write(input("Dogum yeri:") + "\n")


def anlik_uret():
    with open("bil104--projekullanicilar.txt", "a", encoding="utf-8") as file:
        try:

            id_value = int(input("İd: "))
            file.write(str(id_value) + ",")
            file.write(input("İsim:") + ",")
            file.write(input("Soyisim:") + ",")
            file.write(input("Dogum Tarihi:") + ",")
            file.write(input("Dogum yeri:") + "\n")
        except ValueError:
            print("HATA:İd string bir değer olamaz!")
        except:
            print("Bir hata oluştu!")
    with open("bil104--projekullanicilar.txt", "r", encoding="utf-8") as file:
        satirlar = file.readlines()

    a = satirlar[1].split(',')

    i = 1
    satirsayisi = len(satirlar)
    yeni_liste = []
    while i < satirsayisi:
        a = satirlar[i].split(',')

        i += 1
        yeni_liste.append(a)
    for i in yeni_liste:
        with open("kullaniciAdi_sifre.txt", "a", encoding="utf-8") as file:
            file.write(str(id_value) + ",")
        bilgiler = yeni_liste[id_value - 1]
        print("Bilgiler:", bilgiler)
        break
    isim = bilgiler[1]
    soyisim = bilgiler[2]
    dogum_tarihi = bilgiler[3]
    adım1 = isim[1] + isim[3]
    son_uc_karakter = soyisim[len(soyisim) - 3:]
    adım2 = [son_uc_karakter[0], soyisim[0].lower(), son_uc_karakter[2]]
    adım2 = ''.join(adım2)
    adım3 = int(bilgiler[3][0]) + int(bilgiler[3][1]) + int(bilgiler[3][6]) + int(bilgiler[3][7]) + int(
        bilgiler[3][8]) + int(bilgiler[3][9])
    adım3 = str(adım3) + bilgiler[3][8] + bilgiler[3][9]
    kullanici_adi = adım2 + adım1 + adım3
    print("Kullanici adı:", kullanici_adi)
    kullanici_adlari = []
    kullanici_adlari.append(kullanici_adi)
    with open("kullaniciAdi_sifre.txt", "a", encoding="utf-8") as file:
        file.write(str(kullanici_adi) + ",")

    import random

    with open("bil104--projekullanicilar.txt", "r", encoding="utf-8") as file:
        satirlar = file.readlines()

    i = 1
    satirsayisi = len(satirlar)
    yeni_liste = []
    while i < satirsayisi:
        a = satirlar[i].split(',')

        i += 1
        yeni_liste.append(a)
    for i in yeni_liste:
        bilgiler = yeni_liste[id_value - 1]

        break

    isim = bilgiler[1]
    adım1 = isim[0] + isim[-1].title()
    soyisim = bilgiler[2]
    son_iki_harf = soyisim[-2:]
    karakter_dizisi = "*, /, !, _, (, ), &, %, +, -, ., virgül, <,>"
    rastgele_karakter = random.choice(karakter_dizisi)
    son_iki_harf_list = list(son_iki_harf)
    son_iki_harf_list[0] = rastgele_karakter
    son_iki_harf = ''.join(son_iki_harf_list)
    adım2 = son_iki_harf
    dogum_tarihi = bilgiler[3]
    adım3 = dogum_tarihi[8] + dogum_tarihi[9] + str(int(dogum_tarihi[3] + dogum_tarihi[4]) ** 2)
    kesik_s = bilgiler[4][1:-2]
    adım4 = kesik_s[0].upper() + kesik_s[1:-1] + kesik_s[-1].upper()
    rastgele_iki_basamakli = random.randint(10, 99)
    print(rastgele_iki_basamakli)
    adım5 = rastgele_iki_basamakli
    sifre = str(adım4) + str(adım5) + str(adım1) + str(adım3) + str(adım2)
    print("Sifre:", sifre)
    sifreler = []
    sifreler.append(sifre)
    with open("kullaniciAdi_sifre.txt", "a", encoding="utf-8") as file:
        file.write(sifre + "\n")

