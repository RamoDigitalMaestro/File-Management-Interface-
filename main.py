import subprocess
#Dosya Yönetim Arayüzü


def dosya_goruntule():
    subprocess.call(["ls","-l"])
    
def dosya_sil():
    hedef_dosya = input("Hedef Dosya İsmi: ")
    subprocess.call(["rm",hedef_dosya])
    
def dizin_olustur():
    dizinismi = input("Dizin ismi ne olsun? : ")
    subprocess.call(["mkdir",dizinismi])
    
def dosya_olustur():
    dosyaismi = input("Dosya ismi ne Olsun?: ")
    subprocess.call(["touch",dosyaismi])
    
def dosya_okuma():
    okunacakdosya = input("Okunacak ismini giriniz: ")
    subprocess.call(["cat",okunacakdosya])
    
def dosya_kopyala():
    kopyadosya = input("Kopyalanacak dosya'nın ismini giriniz : ")
    kopyalanacakdizin = input("Dosya'nın kopyalanacağı hedef dizini girin : ")
    subprocess.call(["cp",kopyadosya,kopyalanacakdizin])
    
def dosya_tasi():
    taşınacakdosya = input("Taşınacak dosya ismini giriniz : ")
    taşinacakdizin = input("Taşınacağı dizini giriniz : ")
    subprocess.call(["mv",taşınacakdosya,taşinacakdizin])


def dosyabilgi_al():
    bilgialincakdosya = input("Bilgi alınacak dosyanın ismini giriniz : ")
    subprocess.call(["stat",bilgialincakdosya])





while True:
    
    print("1-Dosyaları Görüntüle\n 2-Dosya Sil\n 3-Dizin Oluştur\n 4-Dosya Oluştur\n 5-Dosya Oku\n 6-Dosya kopyala\n 7-Dosya Taşı\n 8-Dosya Hakkında Detaylı Bilgi Al\n 9-Çıkış")
    
    seçim = input(" : ")
    
    if seçim == "1":
        dosya_goruntule()
    
    elif seçim == "2":
        dosya_sil()
    
    elif seçim == "3":
        dizin_olustur()
    
    elif seçim == "4":
        dosya_olustur()
    
    elif seçim == "5":
        dosya_okuma()
    
    elif seçim == "6":
        dosya_kopyala()
    
    elif seçim == "7":
        dosya_tasi()
    
    elif seçim == "8":
        dosyabilgi_al()
    
    elif seçim == "9":
        break
    
    
    else:
        print("Hatalı giriş")
    continue
