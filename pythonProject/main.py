import islemler
def menu_goruntule():
    print("      Kullanıcı Adı ve Şifre Oluşturma Uygulamasına Hoşgeldiniz!     \n")
    print("1-Yeni Kullanıcı Girme\n2-Var olan kullanıcıları görüntüleme\n3-Kullanıcı adı-Şifre oluşturma\n4-Anlık girdiyle kullanıcı adı-Şifre oluşturma")
    islem=int(input("Yapmak istediğiniz işlemi seçiniz:\n"))
    if islem==1:
        islemler.yeni_kullanici()
    elif islem==2:
        islemler.kullanici_getir()
    elif islem==3:
        islemler.kullaniciAdi_sifre_uret()
    elif islem==4:
        islemler.anlik_uret()
    else:
        print("Geçersiz işlem..")
menu_goruntule()
