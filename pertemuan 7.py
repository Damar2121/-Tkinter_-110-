import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memproses prediksi berdasarkan nilai yang dimasukkan
def hasil_prediksi():
    try:
        # Loop untuk memeriksa dan memvalidasi nilai yang diinputkan di setiap entry
        for entry in entries:
            nilai = int(entry.get())  # Mengonversi teks dari entry menjadi integer
            # Memeriksa apakah nilai berada dalam rentang yang diizinkan (0 hingga 100)
            if not (0 <= nilai <= 100):
                # Memunculkan error jika nilai berada di luar rentang
                raise ValueError("Nilai harus antara 0 dan 100.")
        # Jika semua nilai valid, tampilkan hasil prediksi program studi
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError:
        # Menampilkan pesan error jika ada entry yang tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Inisialisasi jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#add8e6")  # Atur warna latar belakang menjadi biru muda

# Label judul dengan teks merah, font tebal, dan latar belakang biru muda
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"), fg="red", bg="#add8e6")
judul_label.grid(row=0, column=0, columnspan=2, pady=20)

# Membuat daftar untuk menampung widget label dan entry
labels = []
entries = []

# Loop untuk membuat 10 input nilai mata pelajaran
for i in range(10):
    # Label untuk setiap input nilai mata pelajaran
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:", bg="#add8e6")
    label.grid(row=i+1, column=0, padx=20, pady=5, sticky='w')
    # Field entry untuk setiap nilai
    entry = tk.Entry(root)
    entry.grid(row=i+1, column=1, padx=20, pady=5)
    labels.append(label)
    entries.append(entry)

# Tombol untuk menjalankan fungsi prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=20)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 12), bg="#add8e6")
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan loop utama aplikasi
root.mainloop()
