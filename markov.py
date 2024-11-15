import numpy as np
import matplotlib.pyplot as plt

# Matriks transisi antara pulsa dan kuota internet
T = np.array([[0.7, 0.3],  # Baris pertama: Pulsa
              [0.6, 0.4]]) # Baris kedua: Kuota Internet

# Kondisi awal (misalkan dimulai dengan penggunaan pulsa dan kuota internet seimbang)
# Anda bisa mengganti initial_state berdasarkan data tahun 2024, misalnya jika data menunjukkan penggunaan 60% pulsa dan 40% kuota internet
initial_state = np.array([0.6, 0.4])

# Iterasi hingga mencapai kondisi stabil (steady state)
threshold = 1e-5  # Ambang batas untuk perubahan yang sangat kecil
max_iterations = 1000  # Jumlah iterasi maksimum
iteration = 0
current_state = initial_state

# List untuk menyimpan hasil tiap iterasi (untuk visualisasi)
history = [current_state]

while iteration < max_iterations:
    next_state = np.dot(current_state, T)
    difference = np.linalg.norm(next_state - current_state)
    
    history.append(next_state)  # Simpan hasil tiap iterasi untuk grafik
    
    if difference < threshold:
        break
    
    current_state = next_state
    iteration += 1

# Menampilkan hasil
print("a. Matriks Transisi T:")
print(f"T = \n{T}")

print("\nKondisi awal penggunaan (tahun 2024):")
print(f"Initial state = {initial_state}")

print(f"\nb. Kondisi stabil dicapai pada iterasi ke-{iteration + 1}:")
print(f"Steady state = {next_state}")

# Visualisasi perubahan penggunaan pulsa dan kuota internet dari tahun 2024 ke belakang
# Kita akan menampilkan tahun 2024 hingga 2019
history = np.array(history)
years = np.arange(2024, 2024 - len(history), -1)

plt.figure(figsize=(10, 6))
plt.plot(years, history[:, 0], label="Pulsa", marker='o')
plt.plot(years, history[:, 1], label="Kuota Internet", marker='x')
plt.xlabel("Tahun")
plt.ylabel("Probabilitas Penggunaan")
plt.title("Perubahan Probabilitas Penggunaan Pulsa dan Kuota Internet (2024 - 2019)")
plt.legend()
plt.grid(True)
plt.show()

# Pertanyaan c: Prediksi penggunaan lebih dominan antara pulsa dengan kuota internet
print("\nc. Penggunaan lebih dominan mana antara pulsa dengan kuota internet?")
if next_state[0] > next_state[1]:
    print("Penggunaan pulsa lebih dominan dibanding kuota internet di kondisi stabil.")
else:
    print("Penggunaan kuota internet lebih dominan dibanding pulsa di kondisi stabil.")
