## Instruction Set

| Halaman Home | Halaman Pertama | Halaman Kedua |
| --- | --- | --- |
|<img src = "https://github.com/jidan-fikri/vital-sign-patient-monitoring/blob/master/stone-design/image/home_page.png" width="1000"/>|<img src = "https://github.com/jidan-fikri/vital-sign-patient-monitoring/blob/master/stone-design/image/first_page.png" width="1000"/>|<img src = "https://github.com/jidan-fikri/vital-sign-patient-monitoring/blob/master/stone-design/image/second_page.png" width="1000"/>|

---
Beberapa anotasi tiap - tiap blok pada desain tampilan vital sign monitor dengan menggunakan tampilan HMI Stone:
- Data Numerik
1. spo2_value = nilai data numerik SpO2 (persen)
2. hr_value = nilai data numerik heart rate (bpm)
3. rr_value = nilai data respiratory rate (rpm)
4. nibp_value_sys = nilai data numerik nibp systolic
5. nibp_value_dias = nilai data numerik nibp diastolic
6. map_value = nilai data numerik nibp MAP (mean arterial pressure)
7. temp_value = nilai data numerik suhu tubuh

- Data Grafik
1. line_series_spo2 = nilai data grafik SpO2
2. line_series_rr = nilai data grafik respiratory rate
3. line_series_ecg(*ecg lead channel*) = nilai data grafik ecg sesuai lead (ex: line_series_ecg1 = untuk grafik lead 1)

- Tombol/Button
1. nib_start = tombol untuk memulai alat nibp/pengukuran tekanan darah

---
Untuk mengirim ataupun membaca data serial bisa mengikuti set instruksi pada dokumentasi STONE. Sebagai contoh:
- Kirim serial berikut ke HMI STONE untuk menampilakan tampilan grafik
  - ST<{"cmd_code":"set_value","type":"line_series","widget":"line_series_ecg1","mode":"push","value":'+str(lead1)+'}>ET \
    Contoh diatas untuk menampilkan grafik ECG untuk lead channel 1. Pada bagian widget bisa diubah sesuai blok yang ingin diisi data (misal contoh lain: line_series_spo2), dan bagian value bisa diisi variabel nilai/data yang ingin dikirimkan ke HMI STONE untuk ditampilkan.
  - ST<{"cmd_code":"set_value","type":"image_value","widget":"hr_value","value":'+str(EKGnum_int)+'}>ET \
    Contoh diatas untuk menampilkan grafik numerik untuk data heart rate. Pada bagian widget bisa diubah sesuai blok yang ingin diisi data (misal contoh lain: spo2_value), dan bagian value bisa diisi variabel nilai/data yang ingin dikirimkan ke HMI STONE untuk ditampilkan.

Untuk instruksi lengkap dapat dilihat [disini](https://github.com/jidan-fikri/vital-sign-patient-monitoring/blob/71c8a120824c5e0fd543c57070f030e95487ef7c/stone-design/%23Instruction%20Sets%20V1.5RC-20220615.pdf)
