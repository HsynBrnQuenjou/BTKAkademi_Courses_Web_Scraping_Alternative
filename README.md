# BTKAkademi_Courses_Web_Scraping_Alternative
# BTK Akademi Kurs Verisi Web Scraper

Bu Python projesi, [BTK Akademi](https://www.btkakademi.gov.tr/portal/catalog) katalog sayfasındaki tüm kursları otomatik olarak tarayıp `Excel` dosyasına kaydeder. Kurslar arasında sayfanın en altındaki kurslar da dahil olmak üzere tamamı çekilir.

## 🚀 Özellikler

- Tüm "Daha Fazla Göster" butonlarına otomatik tıklama
- Sayfadaki tüm kurs kartlarının yakalanması
- Kurs adı, seviye, kullanıcı sayısı ve kurs bağlantısı bilgileri
- Kurs listesinin tersine (`reverse()`) çevrilerek **en alt kursun en üstte** olması
- Excel dosyasına (`.xlsx`) temiz ve tekrar içermeyen veri aktarımı

## 🔧 Gereksinimler

- Python 3.x
- `selenium`
- `pandas`
- Google Chrome ve ChromeDriver (uyumlu sürüm)

### Gerekli paketleri yüklemek için:

Aşağıdaki komutla gerekli kütüphaneleri yükleyebilirsiniz:

```bash
pip install selenium pandas openpyxl
````

Sorun yaşarsanız sırayla kütüphaneleri yükleyiniz:

```bash
pip install selenium
````

```bash
pip install openpyxl pandas
````

---

> **Not:** ChromeDriver'ın sistem PATH'ine ekli olduğundan emin olun veya `webdriver.Chrome(executable_path="...")` ile tam yol verin.

## 📁 Kullanım

1. `scraper.py` (veya bu scripti barındıran Python dosyasını) çalıştırın:

```bash
python btkakademi_web_scraping_alternative.py
```

2. İşlem tamamlandığında, aynı dizine `btkakademi_courses_all.xlsx` isimli Excel dosyası kaydedilecektir.

## 🔄 Değişiklikler (Bu Sürüm)

* **reverse()** fonksiyonu ile liste sıralaması değiştirildi:

  * Artık sayfanın **en altındaki kurslar ilk satırda**, en üsttekiler en sonda yer alır.
* Önceki versiyona göre daha kısa, sade ve odaklanmış yapı

## 📌 Örnek Çıktı (Excel Başlıkları)

| Kurs Adı                | Seviye      | Kullanıcı Sayısı | Bağlantı     |
| ----------------------- | ----------- | ---------------- | ------------ |
| Elektronik Haberleşme Hizmeti Yetkilendirmelerine İlişkin Başvuru ve Değerlendirme Süreci | Temel Seviye | 3.8K | https://www.btkakademi.gov.tr/portal/course/elektronik-haberlesme-hizmeti-yetkilendirmelerine-iliskin-basvuru-ve-degerlendirme-sureci-1050 |
| Elektronik Haberleşme Sektöründe Ar-Ge Çalışmaların Yerli ve Mili Şebeke Kurulmasının Desteklenmesi | Temel Seviye | 3K | https://www.btkakademi.gov.tr/portal/course/elektronik-haberlesme-sektorunde-ar-ge-calismalarin-yerli-ve-mili-sebeke-kurulmasinin-desteklenmesi-1052) |

---

✅ Bu script sayesinde BTK Akademi'deki tüm kurslara hızlıca ulaşabilir ve analiz edebilirsiniz.

## ⚠️ Notlar

* Eğer Excel dosyası başka bir programda açıkken çalıştırırsanız, script dosyayı `btkakademi_kurslar_2.xlsx` adıyla yedek olarak kaydetmeyi dener.
* BTK Akademi web sitesinin HTML yapısı değişirse, scriptteki sınıf/ID seçicileri güncellemeniz gerekebilir.
* ChromeDriver, Chrome tarayıcı sürümünüzle uyumlu olmalıdır. Uyum problemi yaşarsanız yeni sürüm indirin.

---

## 📌 Excel Düzenleme İpucu

Excel'deki veri görünümünü otomatik olarak düzgün hale getirmek için:

1. `Sheet1` sekmesine sağ tıklayın → **Kod Görüntüle** seçeneğine tıklayın.
2. Sol üstte açılan kod penceresinde `(General)` yazan yeri **Worksheet** olarak değiştirin.
3. Aşağıdaki kod satırını ekleyin:

```vba
Columns.AutoFit
```

4. `Ctrl + S` ile kaydedin ve dosyayı kapatın.
5. Şimdi Excel dosyanız açıldığında sütunlar otomatik olarak içeriklere göre hizalanmış olacaktır.

---

## 👨‍💻 Geliştirici

**Baran Hüseyin Kençü**
Otomasyon ve veri işleme tutkusu ile geliştirildi. 💻❤️
