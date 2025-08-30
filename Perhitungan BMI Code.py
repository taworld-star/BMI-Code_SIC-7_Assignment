def hitung_bmi_dan_kategori():
    """
    Program untuk menentukan kategori BMI berdasarkan input berat dan tinggi
    Menggunakan kategori BMI menurut WHO
    """
    
    print("="*50)
    print("    PROGRAM PENENTUAN KATEGORI BMI")
    print("      (Menurut Standar WHO)")
    print("="*50)
    
    # Input dan validasi data dengan nested condition
    try:
        berat = float(input("Masukkan berat badan (kg): "))
        tinggi = float(input("Masukkan tinggi badan (m): "))
        
        # Nested condition untuk validasi input
        if berat <= 0 or tinggi <= 0:
            print("ERROR: Berat dan tinggi harus lebih dari 0!")
            return
        elif berat > 500:  # Validasi berat maksimal
            if tinggi > 3.0:  # Nested condition dengan logical operator
                print("ERROR: Input berat dan tinggi tidak realistis!")
            else:
                print("ERROR: Berat badan tidak realistis!")
            return
        elif tinggi > 3.0:
            print("ERROR: Tinggi badan tidak realistis!")
            return
        else:
            # Menghitung BMI
            bmi = berat / (tinggi ** 2)
            
            print(f"\nHasil Perhitungan:")
            print(f"Berat Badan: {berat} kg")
            print(f"Tinggi Badan: {tinggi} m")
            print(f"BMI: {bmi:.2f} kg/m²")
            print("-" * 40)
            
            # Penentuan kategori BMI menurut WHO dengan if, elif, else
            if bmi < 18.5:
                kategori = "BERAT BADAN KURANG"
                warna_status = "🔵"
                
                # Nested condition untuk tingkat keparahan
                if bmi < 16.0:
                    tingkat = "Sangat Kurus"
                    saran = "SEGERA konsultasi dokter - risiko malnutrisi tinggi"
                elif bmi >= 16.0 and bmi < 17.0:
                    tingkat = "Kurus Sedang"
                    saran = "Konsultasi dokter dan ahli gizi untuk menaikkan berat badan"
                else:  # 17.0 <= bmi < 18.5
                    tingkat = "Kurus Ringan"
                    saran = "Tingkatkan asupan kalori dengan makanan bergizi seimbang"
                
            elif bmi >= 18.5 and bmi <= 24.9:
                kategori = "BERAT BADAN NORMAL"
                warna_status = "🟢"
                
                # Nested condition untuk range optimal
                if bmi >= 20.0 and bmi <= 22.0:
                    tingkat = "Optimal"
                    saran = "Excellent! Pertahankan berat badan dan gaya hidup sehat"
                elif (bmi >= 18.5 and bmi < 20.0) or (bmi > 22.0 and bmi <= 24.9):
                    tingkat = "Normal"
                    saran = "Baik! Pertahankan pola makan sehat dan olahraga rutin"
                
            elif bmi >= 25.0 and bmi <= 29.9:
                kategori = "BERAT BADAN BERLEBIH/KELEBIHAN BERAT BADAN"
                warna_status = "🟡"
                
                # Nested condition dengan logical operator
                if bmi >= 25.0 and bmi < 27.5:
                    tingkat = "Overweight Ringan"
                    saran = "Kurangi porsi makan dan tingkatkan aktivitas fisik"
                elif bmi >= 27.5 and bmi <= 29.9:
                    tingkat = "Overweight Sedang"
                    saran = "Konsultasi ahli gizi - perlu program penurunan berat badan"
                    
            else:  # bmi >= 30.0
                kategori = "OBESITAS"
                warna_status = "🔴"
                
                # Nested condition untuk klasifikasi obesitas
                if bmi >= 30.0 and bmi < 35.0:
                    tingkat = "Obesitas Kelas I"
                    risiko = "Risiko kesehatan meningkat"
                elif bmi >= 35.0 and bmi < 40.0:
                    tingkat = "Obesitas Kelas II"
                    risiko = "Risiko kesehatan tinggi"
                else:  # bmi >= 40.0
                    tingkat = "Obesitas Kelas III (Morbid Obesity)"
                    risiko = "Risiko kesehatan sangat tinggi"
                
                saran = "WAJIB konsultasi dokter untuk program penurunan berat badan"
            
            # Output hasil dengan format yang jelas
            print(f"Status: {warna_status} {kategori}")
            print(f"Tingkatan: {tingkat}")
            
            # Nested condition untuk menampilkan informasi risiko
            if bmi >= 30.0:
                print(f"Tingkat Risiko: {risiko}")
            
            print(f"Saran: {saran}")
            
            # Informasi tambahan berdasarkan kategori dengan nested condition
            print("\n" + "="*50)
            print("INFORMASI TAMBAHAN:")
            
            # Input usia untuk rekomendasi spesifik
            try:
                usia = int(input("Masukkan usia (tahun): "))
                
                # Nested condition berdasarkan usia dan BMI
                if usia < 18:
                    print("⚠️  Catatan: Kategori BMI ini untuk dewasa (≥18 tahun)")
                    print("   Untuk anak/remaja, konsultasi dokter anak")
                elif usia >= 18 and usia < 60:
                    # Nested condition untuk dewasa
                    if bmi < 18.5 or bmi >= 25.0:
                        print("📋 Rekomendasi Dewasa: Konsultasi ahli gizi")
                        if bmi >= 30.0:  # Nested condition tambahan
                            print("🏥 Prioritas: Pemeriksaan kesehatan menyeluruh")
                    else:
                        print("✅ Rekomendasi Dewasa: Pertahankan gaya hidup sehat")
                else:  # usia >= 60
                    # Nested condition untuk lansia
                    if bmi >= 22.0 and bmi <= 27.0:
                        print("👴 Catatan Lansia: BMI dalam range yang baik untuk usia 60+")
                    elif bmi < 22.0:
                        print("⚠️  Peringatan Lansia: BMI terlalu rendah - risiko sarcopenia")
                    elif bmi > 27.0:
                        print("📋 Rekomendasi Lansia: Konsultasi dokter geriatri")
                        
            except ValueError:
                print("Input usia tidak valid")
            
            # Tabel referensi WHO
            print("\n TABEL REFERENSI BMI (WHO):")
            print("┌─────────────────┬───────────────────────────┐")
            print("│ Range BMI       │ Kategori                  │")
            print("├─────────────────┼───────────────────────────┤")
            print("│ < 18,5          │ Berat badan kurang        │")
            print("│ 18,5 - 24,9     │ Berat badan normal        │")
            print("│ 25 - 29,9       │ Berat badan berlebih      │")
            print("│ ≥ 30            │ Obesitas                  │")
            print("└─────────────────┴───────────────────────────┘")
            
    except ValueError:
        print(" ERROR: Masukkan angka yang valid untuk berat dan tinggi!")
        return
    
    print(f"\n  BMI Anda: {bmi:.2f} kg/m² - {kategori}")
    print(" Perhitungan Sumber: World Health Organization (WHO)")

# Menjalankan program utama
if __name__ == "__main__":
    # Loop untuk menghitung BMI berkali-kali
    while True:
        hitung_bmi_dan_kategori()
        
        print("\n" + "="*50)
        # Nested condition untuk pilihan mengulang
        while True:
            pilihan = input("Apakah ingin menghitung BMI lagi? (y/n): ").lower()
            
            if pilihan == 'y' or pilihan == 'yes':
                print("\n" + "="*50)
                break  # Keluar dari loop pilihan, lanjut hitung BMI
            elif pilihan == 'n' or pilihan == 'no':
                print("\n Terima kasih telah menggunakan BMI Calculator!")
                print(" Jaga kesehatan dan tetap semangat!")
                exit()  # Keluar dari program
            else:
                print("Input tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")
                # Program akan terus meminta input hingga pengguna memberikan jawaban yang valid