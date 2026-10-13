# Modul 2 Komputasi Awan — Jenkins + Docker + Database

Aplikasi contoh Flask dengan database SQLite untuk latihan pipeline Jenkins.

## Menjalankan secara lokal

Pastikan Docker Desktop sudah berjalan, lalu jalankan di folder proyek:

```bash
docker build -t garda05/modul2-flask-db .
docker run --rm -p 5000:5000 -v modul2_data:/data garda05/modul2-flask-db
```

Buka `http://localhost:5000` dan `http://localhost:5000/health`.

## Sebelum menjalankan Jenkinsfile

1. Buat repository GitHub dan unggah semua file proyek ini.
2. Username Docker Hub sudah disesuaikan ke `garda05` di `Jenkinsfile`.
3. Di Jenkins, buat credential jenis **Username with password**:
   - ID: `dockerhub-credentials`
   - Username: `garda05`
   - Password: Docker Hub access token (bukan password akun)
4. Buat job **Pipeline**, pilih **Pipeline script from SCM**, SCM **Git**, lalu masukkan URL repository.
5. Jenkins agent harus memiliki akses ke Docker Engine dan perintah `docker`. Jika agent Linux, pipeline di atas menggunakan `sh`.

## Catatan database

Aplikasi menggunakan SQLite dan menyimpan data di `/data/app.db`. Untuk menyimpan data ketika container dihentikan, jalankan container dengan volume seperti perintah di atas. Pipeline membangun image dan menguji import Flask sebelum push ke Docker Hub.
