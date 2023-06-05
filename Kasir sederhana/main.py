print(25 * "=")  # Ini nama toko
print(
    """
     KOPI INSPIRASI 
    ORANG INDONESIA
"""
)
print(25 * "=")

# Ini adalah bagian menu
print(
    """
    List Menu Kopi
---------------------------
|NO|  NAMA KOPI |  HARGA  |
---------------------------
|1.| KOPI HITAM | Rp. 7000|
|2.| KOPI SUSU  | Rp. 6500|
|3.| KOPI JAHE  | Rp. 5000|
---------------------------
"""
)

print("SILAHKAN PESAN")

pesan = int(input("\nMasukkan list angka menu kopi : "))
jmlpesan = int(input("Masukkan Jumlah Pesanan: "))
if pesan == 1:
    harga = 7000 * jmlpesan
    nama = "KOPI HITAM"
    print("Nama pesanan : ", nama, "\nJumlah pesanan : ", jmlpesan, "\nHarga : ", harga)
elif pesan == 2:
    harga1 = 6500 * jmlpesan
    nama1 = "KOPI SUSU"
    print(
        "Nama pesanan : ", nama1, "\nJumlah pesanan : ", jmlpesan, "\nHarga : ", harga1
    )
elif pesan == 3:
    harga2 = 5000 * jmlpesan
    nama2 = "KOPI JAHE"
    print(
        "Nama pesanan : ", nama2, "\nJumlah pesanan : ", jmlpesan, "\nHarga : ", harga2
    )
else:
    print("MENU TIDAK TERSEDIA !!!")
