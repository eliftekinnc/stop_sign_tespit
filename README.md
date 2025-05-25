# STOP Trafik İşareti Tespiti – Python & OpenCV

Bu proje, Python programlama dili ve OpenCV kütüphanesi kullanılarak STOP trafik işaretinin tespit edilmesini amaçlamaktadır.  
Tespit, görüntüdeki kırmızı renk aralığına dayalı olarak gerçekleştirilir.  
Otonom araçlar veya mobil robotlar için temel bir görüntü işleme örneğidir.

---

##  Proje Yapısı

```
stop_sign_tespit/
├── stop_sign_tespit_etme_cv.py     
├── dataset/              
├── output/           
└── README.md            
```

---

## Gerekli Kurulumlar

Bu projeyi çalıştırmak için aşağıdaki kütüphanelere ihtiyacınız vardır:

```bash
pip install opencv-python numpy
```



---

## Nasıl Çalıştırılır?

1. Terminal veya komut satırında proje klasörüne gidin:
    ```bash
    cd stop_sign_tespit
    ```

2. Python dosyasını çalıştırın:
    ```bash
    python stop_sign_tespit_etme_cv.py
    ```

3. Her bir görselde STOP işareti tespit edilip:
   - Yeşil kutu ile kare içine alınır.
   - Terminale işaretin merkez koordinatları yazdırılır.
   - `output/` klasörüne işlenmiş görseller kaydedilir.

---

## Çıktı Örneği

```plaintext
Görüntü: stop1.jpg, STOP işareti merkezi: (312, 244)
Görüntü: stop2.jpg, STOP işareti merkezi: (288, 261)
```

İlgili görseller `output/` klasörüne şu şekilde kaydedilir:

```
output/output_stop1.jpg
output/output_stop2.jpg
```


---

## Hazırlayan
Elif Tekin
Kontrol ve Otomasyon Mühendisliği 
Yıldız Teknik Üniversitesi  
Mayıs 2025