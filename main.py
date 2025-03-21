import discord
from discord.ext import commands
import requests
import os
from model import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

# Saran untuk mencegah isu
solutions = {
    "garbages": (
        "# SAMPAH & PENCEMARAN LINGKUNGAN\n\n"
        "## Penyebab Utama:\n"
        "- **Kurangnya Kesadaran Masyarakat:** Banyak orang tidak peduli dampak sampah bagi lingkungan, seperti membuang puntung rokok atau plastik sembarangan.\n"
        "- **Tempat Sampah Tidak Memadai:** Kurangnya fasilitas tempat sampah di area publik sekitar memicu banyak orang membuang sampah sembarangan.\n"
        "- **Kebiasaan 'Asal cepat':** Misalnya, membuang sampah dari kendaraan atau saat piknik karena malas mencari tempat sampah.\n"
        "- **Budaya 'Itu urusan Petugas':** Anggapan bahwa sampah adalah tanggung jawab petugas kebersihan.\n\n"
        "## Solusi:\n"
        "- **Buang Sampah pada Tempatnya:** Pastikan sampah dibuang ke tempat yang sesuai 🚮\n"
        "- **Daur Ulang & Kompos:** Kurangi limbah dengan memilah sampah yang bisa didaur ulang atau dikompos.\n"
        "- **Ikut Serta dalam Aksi Bersih-Bersih:** Bergabung atau adakan kegiatan bersih lingkungan di sekitar 🧹\n"
        "- **Gunakan Produk Ramah Lingkungan:** Kurangi penggunaan plastik sekali pakai dengan beralih ke produk yang bisa digunakan kembali.\n\n"
        "♻️ *Kenapa ini penting?* Sampah yang berserakan mencemari lingkungan, merusak ekosistem, dan membahayakan makhluk hidup sekitar."
    ),
    "deforestation": (
        "# DEFORESTASI (Penggundulan Hutan)\n\n"
        "## Penyebab Utama:\n"
        "- **Ekspansi Lahan Pertanian:** Hutan ditebang untuk dijadikan perkebunan kelapa sawit, kedelai, atau peternakan sapi.\n"
        "- **Pertambangan Ilegal:** Penambangan emas, batu bara, atau mineral lain yang merusak hutan.\n"
        "- **Pembangunan Infrastruktur:** Pembuatan jalan tol, perumahan, atau industri yang mengorbankan kawasan hutan.\n"
        "- **Kebakaran Hutan:** Terjadi secara alami (petir) atau disengaja (membuka lahan dengan cara dibakar).\n"
        "- **Eksploitasi Kayu Komersial:** Penebangan pohon untuk kayu bangunan, furnitur, atau kertas.\n\n"
        "## Solusi:\n"
        "- **Menanam Pohon:** Dukung atau ikut program penanaman pohon seperti *Trees4Trees* atau *Indonesia Menanam*. Bayar *Rp50.000*, kamu bisa 'punya' pohon di hutan rehabilitasi 🌱\n"
        "- **Kurangi Penggunaan Kertas & Kayu:** Beralih ke alternatif digital dan gunakan produk berbahan dasar kayu yang berkelanjutan.\n"
        "- **Pilih Produk Ramah Hutan:** Cari logo RSPO (sawit berkelanjutan) atau FSC (kayu lestari), dan hindari produk yang bikin hutan Sumatera/Kalimantan makin gundul 🛒\n"
        "- **Tekan Pemerintah & Perusahaan:** Tag mereka di medsos kalau ada kasus tambang ilegal. Dukung kebijakan larangan ekspor kayu mentah agar hutan tak dieksploitasi 💪\n"
        "- **Sebarkan Kesadaran:** Edukasi orang lain tentang pentingnya hutan dalam menjaga keseimbangan alam.\n\n"
        "🌍🌱 *Kenapa ini penting?* Hutan berperan dalam menyerap karbon, menjaga keseimbangan iklim, dan menjadi habitat bagi banyak spesies."
    ),
    "icemelting": (
        "# PENCAIRAN ES\n\n"
        "## Penyebab Utama:\n"
        "- **Pemanasan Global:** Emisi gas rumah kaca (CO₂, metana) dari industri, kendaraan, dan pembakaran fosil memerangkap panas di atmosfer.\n"
        "- **Polusi Udara:** Partikel black carbon (jelaga) dari asap pabrik/kendaraan menempel di es, mempercepat penyerapan panas.\n"
        "- **Perubahan Arus Laut:** Suhu laut yang menghangat mengikis es dari bawah (misal: gletser Antartika).\n"
        "- **Aktivitas Manusia di Kutub:** Eksplorasi minyak, pariwisata, atau penelitian yang mengganggu ekosistem es.\n\n"
        "## Solusi:\n"
        "- **Hemat Air & Listrik: Matikan keran saat gosok gigi, cabut charger HP kalau udah penuh. **Ingat❗** Sebagian 60% listrik Indonesia masih dari batubara.\n"
        "- **Transportasi Umum:** Gunakan transportasi umum seperti Bus, Kereta, Sepeda dll. Selain hemat BBM, kurangi emisi CO₂. *Bonus:* Badan makin sehat! 🚴\n"
        "- **Konsumsi dengan Bijak:** Kurangi konsumsi daging, pilih produk ramah lingkungan, dan kurangi pemborosan makanan.\n"
        "- **Dukung Kebijakan Iklim:** Berpartisipasi dalam gerakan atau kebijakan yang bertujuan mengurangi emisi dan mendukung energi hijau.\n\n"
        "❄️ *Kenapa ini penting?* Pencairan es menyebabkan kenaikan permukaan laut yang mengancam kota-kota pesisir dan ekosistem laut."
    )
}

# < Perintah Bot Discord >
@bot.event
async def on_ready():
    print(f'Successfully logged in as {bot.user}. Type any commands to get started!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hai! Saya {bot.user}. Senang bertemu denganmu!')

@bot.command()
async def facts(ctx):
    await ctx.send(f"# Tahukah kamu❓\n{randomfacts()}")

# Perintah untuk mengklasifikasi gambar (sesuai dengan 3 kelas)
@bot.command()
async def resolve(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            response = requests.get(file_url)
            if response.status_code == 200:
                with open(file_name, 'wb') as f:
                    f.write(response.content)

                class_name, confidence = classification(file_name)
                cleaned_class = class_name.strip().lower()
                solution = solutions.get(cleaned_class, "Tidak ada solusi.")
                
                await ctx.send(f"**Prediksi:** {class_name}\n"
                               f"**Skor kepercayaan:** {confidence:.2f}\n\n"
                               f"{solution}")
                
                print(f"Predicted class (raw): {class_name}")

                # Menghapus gambar setelah diklasifikasikan
                os.remove(file_name)
    else:
        await ctx.send("Tolong di-upload gambarnya ya.")
        return
    
bot.run("")