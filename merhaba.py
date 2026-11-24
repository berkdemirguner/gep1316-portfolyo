from datetime import datetime  # Bilgisayarın geçerli tarihini almak için datetime sınıfını içe aktarır.

ad = input("Adınızı girin: ").strip()  # Kullanıcıdan adını alır ve baştaki/sondaki boşlukları temizler.
dogum_yili_metni = input("Doğum yılınızı girin: ").strip()  # Doğum yılını metin olarak alır.

if not dogum_yili_metni.isdigit():  # Girilen değerin yalnızca rakamlardan oluşup oluşmadığını kontrol eder.
    print("Lütfen doğum yılını dört rakamla girin.")  # Giriş geçersizse kullanıcıyı bilgilendirir.
    raise SystemExit  # Programı güvenli biçimde sonlandırır.

dogum_yili = int(dogum_yili_metni)  # Doğum yılı metnini tam sayıya dönüştürür.
bu_yil = datetime.now().year  # Sistemin tarihinden içinde bulunulan yılı alır.

if dogum_yili > bu_yil:  # Doğum yılının gelecek bir yıl olup olmadığını kontrol eder.
    print("Doğum yılı gelecekte olamaz. Lütfen bilgiyi kontrol edin.")  # Gelecek yıl girildiyse uyarı verir.
    raise SystemExit  # Hatalı bilgiyle yaş hesabı yapılmasını önler.

if dogum_yili < 1900:  # Gerçekçi olmayan eski bir yıl girilip girilmediğini kontrol eder.
    print("Lütfen geçerli bir doğum yılı girin.")  # Kullanıcıya geçerli bir yıl girmesini söyler.
    raise SystemExit  # Geçersiz girişte programı sonlandırır.

yas = bu_yil - dogum_yili  # İçinde bulunulan yıldan doğum yılını çıkararak yaklaşık yaşı hesaplar.

if ad == "":  # Kullanıcının ad alanını boş bırakıp bırakmadığını kontrol eder.
    ad = "Arkadaşım"  # Ad girilmediyse genel bir hitap kullanır.

print(f"Merhaba {ad}! {yas} yaşındasın. GEP1316 portfolyoma hoş geldin!")  # Kişiye özel karşılama mesajını ekrana yazdırır.
