# 📥 IG Comment Extractor & Merger

IG Comment Extractor adalah tool sederhana berbasis Python untuk **mengambil komentar dari postingan Instagram (Reel, Feed)** dan **menggabungkannya ke dalam satu file**. Cocok untuk riset media sosial, analisis sentimen, dan keperluan data lainnya.

---

## 🚀 Fitur Utama

- 🔗 Ambil komentar dari berbagai URL Instagram
- 🗂️ Simpan komentar secara otomatis ke folder `feeds/` dan `reels/`
- 📄 Gabungkan semua komentar ke satu file teks
- 🎨 Tampilan terminal interaktif dengan `colorama` dan `tqdm`

---

## 📁 Struktur Proyek

```
.
├── 2file.py            # Script utama untuk ambil komentar dari Instagram
├── cookie.py           # Berisi data session/cookie akun Instagram
├── gabung.py           # Script untuk menggabungkan komentar
├── requirements.txt    # Dependency Python
├── output_comments/
│   ├── feeds/          # Komentar dari postingan feed
│   └── reels/          # Komentar dari postingan reels
└── output_file/        # Hasil gabungan semua komentar
```

---

## ⚙️ Cara Instalasi

1. **Clone repositori**

```bash
git clone https://github.com/HilmiAlawi/IG-Comment-Extractor.git
cd IG-Comment-Extractor
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Siapkan file `cookie.py`**

Isi dengan data cookie dari akun Instagram kamu:

```python
sessionid = "ISI_SESSION_ID_KAMU"
ds_user_id = "ISI_USER_ID"
csrftoken = "ISI_CSRF_TOKEN"
mid = "ISI_MID"
```

---

## ▶️ Cara Penggunaan

### 1. Ekstrak Komentar Instagram

```bash
python 2file.py
```

- Masukkan satu atau beberapa URL Instagram (feed/reel/tv)
- Tekan `Enter` setiap URL
- Ketik `done` saat selesai

Komentar akan otomatis tersimpan ke folder `output_comments/feeds` atau `output_comments/reels`.

---

### 2. Gabungkan Semua Komentar

```bash
python gabung.py
```

- Masukkan nama file hasil output gabungan
- File akan tersimpan di `output_file/`

---

## ❗ Catatan Penting

- Pastikan kamu login di Instagram melalui browser untuk mendapatkan cookie.
- Cookie harus valid dan aktif saat digunakan.
- Tool ini **tidak resmi dari Instagram**, gunakan secara bertanggung jawab.

---

## 🧠 Digunakan Untuk

- 📊 Analisis sentimen sosial media
- 🧪 Riset akademik atau skripsi
- 💼 Riset digital marketing dan brand monitoring

---


## 📜 License

This project is licensed under the MIT License.
© 2025 [Hilmi Alawi](https://github.com/HilmiAlawi)

---
📍 Tasikmalaya  🎥 Foto & Video • 📢 Event Organizer • 📲 Digital Marketing • 📱 Social Media Handling

```
███╗   ███╗██╗██████╗  ██████╗ ███████╗████████╗██╗███████╗██╗   ██╗
████╗ ████║██║██╔══██╗██╔═══██╗██╔════╝╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
██╔████╔██║██║██████╔╝██║   ██║███████╗   ██║   ██║█████╗   ╚████╔╝ 
██║╚██╔╝██║██║██╔═══╝ ██║   ██║╚════██║   ██║   ██║██╔══╝    ╚██╔╝  
██║ ╚═╝ ██║██║██║     ╚██████╔╝███████║   ██║   ██║██║        ██║   
╚═╝     ╚═╝╚═╝╚═╝      ╚═════╝ ╚══════╝   ╚═╝   ╚═╝╚═╝        ╚═╝   
```

---

> Jika tool ini bermanfaat, jangan lupa beri bintang ⭐ di GitHub ya!

