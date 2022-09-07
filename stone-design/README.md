## Instruction Set

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

---
Untuk mengirim ataupun membaca data serial bisa mengikuti set instruksi pada dokumentasi STONE
