import tkinter as tk

def hitung():
    panjang = float(entry_panjang.get())
    lebar = float(entry_lebar.get())

    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)

    text_hasil.delete(1.0, tk.END)
    text_hasil.insert(tk.END, f"Luas Persegi Panjang : {luas:g}\n")
    text_hasil.insert(tk.END, f"Keliling Persegi Panjang : {keliling:g}")

# Window utama
window = tk.Tk()
window.title("Program Persegi Panjang")

# Masukan Panjang
label_panjang = tk.Label(window, text="Masukan Panjang")
label_panjang.grid(row=0, column=0, padx=5, pady=5)
entry_panjang = tk.Entry(window)
entry_panjang.grid(row=0, column=1, padx=5, pady=5)

# Masukan Lebar
label_lebar = tk.Label(window, text="Masukan Lebar")
label_lebar.grid(row=1, column=0, padx=5, pady=5)
entry_lebar = tk.Entry(window)
entry_lebar.grid(row=1, column=1, padx=5, pady=5)

# Tombol Hitung
tombol_hitung = tk.Button(window, text="Hitung", command=hitung)
tombol_hitung.grid(row=2, column=0, padx=5, pady=5)

text_hasil = tk.Text(window, height=3, width=35)
text_hasil.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()