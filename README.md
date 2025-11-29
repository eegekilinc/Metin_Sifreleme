# 🔐 Basit XOR Şifreleme Projesi

Bu proje, Python kullanılarak geliştirilmiş, metinleri sabit bir sayısal anahtarla (parola) şifreleyen ve çözen basit bir simetrik şifreleme uygulamasıdır. Algoritma, her karakter üzerinde **Bitsel XOR** (`^`) işlemini temel alır.


## ✨ Özellikler

* **Simetrik Şifreleme:** Şifreleme ve şifre çözme için aynı anahtar kullanılır.
* **Sabit Anahtar:** Şifreleme anahtarı koda sabitlenmiştir (`password = 15`).
* **Basitlik:** Şifreleme mantığı XOR işleminin matematiksel özelliğine dayanır.

---

## 🛠️ Nasıl Çalışır?

Proje iki ana fonksiyondan oluşur:

1.  `Encrypt(metin, anahtar)`
    * Girdi olarak alınan metindeki her karakteri alır.
    * Karakterin sayısal değeri ile sabit anahtarı **XOR** işlemine tabi tutar.
    * Sonuç olarak şifreli karakterler dizisi üretir.

2.  `Decrypt(şifreli_metin, anahtar)`
    * Şifreli metni alır.
    * Şifreli karakterleri tekrar aynı sabit anahtar ile **XOR** işlemine tabi tutarak orijinal karakter değerlerini geri getirir
