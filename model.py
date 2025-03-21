# Mengimpor pustaka
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import re

import random

model_path = "converted_keras4\keras_model.h5"
labels_path = "converted_keras4\labels.txt"

def classification(image_path):
    # Memuat model dan label kelas
    model = load_model(model_path, compile=False)
    class_names = [re.sub(r'^\d+\s+', '', label.strip()) for label in open(labels_path, "r").readlines()]

    # Memproses gambar
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    # Prediksi model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    return class_name, confidence_score

def randomfacts():
    fact = {
        "Komposisi atmosfer global yang dimaksud adalah komposisi material atmosfer bumi berupa Gas Rumah Kaca (Greenhouse gases), seperti Karbon Dioksida, Metana, Nitrogen, dan sebagainya.",
        "Sekitar 10 juta hektar hutan tropis hilang setiap tahun (setara 30 lapangan bola per menit). Kawasan Amazon, Indonesia, dan Kongo paling terdampak 😢",
        "Penebangan hutan disebabkan perluasan lahan untuk ternak, sawit, dan kedelai. Tambang ilegal juga merusak 1,3 juta hektar hutan Amazon tiap tahun.",
        "Ironisnya, akibat kebakaran dan kerusakan, Hutan Amazon kini melepaskan lebih banyak CO₂ daripada menyerapnya ☹️",
        "Asap kebakaran hutan (seperti yang terjadi di Kanada pada tahun 2023) tingkatkan polusi 10x lipat. Paru-paru kita jadi korban!",
        "80% hewan dan tumbuhan darat hidup di hutan. Kalau hutan hilang, 1 juta spesies bisa punah, termasuk orangutan dan harimau Sumatera 🐅🦧",
        "Pencairan es Arktik bikin ilmuwan khawatir virus kuno (seperti Pithovirus sibericum) bisa 'hidup' lagi dan kemungkinan menginfeksi manusia 😷",
        "Pemerintah Indonesia Habiskan *Rp1,5 Triliun*/Tahun untuk membersihkan sampah di sungai, laut, dan jalanan. Uang segitu bisa buat bangun 150 sekolah! 💸",
        "60% es di pegunungan Alpen (benua Eropa) sudah hilang sejak 1850. Dampaknya? Pasokan air minum Eropa terancam, dan pemandangan indah musim dingin bisa punah ❄️",
        "Polusi udara bikin anak-anak lambat belajar dan mempercepat penuaan otak orang dewasa. Bahkan bisa memperpendek umur 2,2 tahun! 🧠",
        "Sejak 1979, luas es laut Arktik di musim panas berkurang 13% per dekade. Tahun 2023 jadi rekor terendah kedua!",
        "Botol plastik butuh 450-500 tahun untuk terurai. Kalau zaman Majapahit ada Aqua, sampahnya baru hancur sejak zaman kolonial Belanda!",
        "Ada 11.000+ bank sampah di Indonesia yang mengubah sampah jadi duit. Contoh: Bank Sampah Malang bisa hasilkan Rp500 juta/bulan dari sampah daur ulang! 💰",
        "Indonesia menghasilkan 2 juta ton sampah elektronik/tahun (HP rusak, baterai, dll.). Sampah ini mengandung timbal dan merkuri yang meracuni tanah dan air 💀",
        "Destinasi wisata seperti Bali kehilangan 20% turis karena masalah sampah. Padahal, 80% sampah itu berasal dari lokal, bukan turis 😔",
        "Partikel plastik kecil (mikroplastik) sudah ditemukan di 90% ikan laut, bahkan di tubuh manusia lewat konsumsi seafood 🐟",
        "Polusi udara bikin anak-anak lambat belajar dan mempercepat penuaan otak orang dewasa. Bahkan bisa memperpendek umur 2,2 tahun! 🧠",
        "Desa Panggungharjo, Yogyakarta, berhasil kurangi 70% sampah dengan komposter dan daur ulang mandiri 🌱",
        "Biaya panel surya turun 82% sejak 2010, dan energi angin darat turun 39%. Sekarang lebih murah pakai energi terbarukan daripada batubara! 💡",
        "Negara ini daur ulang 99% sampahnya, bahkan impor sampah dari negara lain buat jadi energi! ♻️",
        "Sejak 2019, Bali kurangi sampah plastik 30%. Sekarang banyak warung kopi pakai sedotan bambu 🎋",
        "Negara Swedia, Eropa, mendaur ulang 90-98% sampahnya, bahkan impor sampah dari negara lain buat jadi energi! ♻️",
        "Perusahaan Indonesia pakai limbah sekam padi untuk bikin beton rendah emisi. Keren, kan? 🏗️",
        "Kurangi makan daging sapi 1x seminggu bisa kurangi emisi setara 1.000 km naik mobil! 🌱 *(University of Oxford, 2021)*",
        "Masyarakat Dayak di Kalimantan sukses kurangi deforestasi 40% lewat hutan adat. Mereka dapet penghasilan dari madu & rotan! 🐝",
        "Di Liuzhou, China, ada kota dengan 40.000 pohon yang bisa serap 10.000 ton CO₂/tahun. Mirip Avatar dunia nyata! 🌳🏙️",
        "Puntung rokok mengandung 7.000+ bahan kimia (arsenik, nikotin) yang mencemari tanah dan air. Butuh 10 tahun untuk terurai! 🚭"
    }

    return random.choice(list(fact))