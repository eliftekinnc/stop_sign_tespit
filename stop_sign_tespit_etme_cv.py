import cv2 as cv
import numpy as np
import os

input_dir = "stop_sign_dataset"
output_dir = "output"


os.makedirs(output_dir, exist_ok=True)  # Klasör yoksa oluşturur, varsa görmezden gelir.


# HSV renk uzayında kırmızı renk aralığı, kırmızı hem 0-10 hem de 170-180 arasında bulunur o yüzden çift maskeleme yapıp bunları birleştiriyoruz
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# Her veriyi işliyoruz
for veri in os.listdir(input_dir):
  # Görüntüyü oku
  image_path = os.path.join(input_dir, veri)
  image = cv.imread(image_path)
  if image is None:
      print(f"Görüntü yüklenemedi: {veri}")
      continue

  # HSV renk uzayına çevir
  hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

  # Kırmızı renk maskesi oluştur
  mask1 = cv.inRange(hsv, lower_red1, upper_red1)
  mask2 = cv.inRange(hsv, lower_red2, upper_red2)
  mask = mask1 + mask2

  # Gürültüyü azaltmak için morfolojik işlemler
  kernel = np.ones((5, 5), np.uint8)
  mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)

  # Konturları bul
  contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

  # Her konturu işle
  for contour in contours:

      # Küçük gürültüleri filtrele
      if cv.contourArea(contour) > 1000:

          # Sınır kutusunu al
          x, y, w, h = cv.boundingRect(contour)

          # Görüntüye dikdörtgen çiz
          cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

          # Merkez koordinatlarını hesapla
          center_x = x + w // 2
          center_y = y + h // 2
          print(f"Görüntü: {veri}, STOP işareti merkezi: ({center_x}, {center_y})")

  # Çıktı görüntüsünü kaydet
  output_path = os.path.join(output_dir, f"output_{veri}")
  cv.imwrite(output_path, image)

print("İşlem tamamlandı. Çıktı görüntüleri:", output_dir)