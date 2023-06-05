data_angka = [1, 7, 8, 4, 5, 6, 2, 3, 9, 0]

print(f"data angka = \n{data_angka}")

# count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"data angka 4 = {jumlah_data_4}")
print(f"data angka 3 = {jumlah_data_3}")

# ambil posisi data (index)

data = ["ucup", "dudung", "otong"]
print(f"data = {data}")
index_dudung = data.index("dudung")
index_otong = data.index("otong")
print(f"index si dudung = {index_dudung}")
print(f"index si otong = {index_otong}")

# mengurutkan list
print(f"data sebelum di sort = {data_angka}")
data_angka.sort()
print(f" data sesudah di sort = {data_angka}")

# balik list
data_angka.reverse()
print(f"data di reverse = {data_angka}")
