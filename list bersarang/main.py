data_0 = [1, 2]
data_1 = [3, 4]

data_list_biasa = [1, 2, 3, 4]

print(f"list biasa = {data_list_biasa}")

list_2D = [data_0, data_1]

print(f"list 2D = {list_2D}")

# contoh penggunaan

peserta_0 = ["ucup", 25, "Laki-Laki"]
peserta_1 = ["otong", 10, "Laki-Laki"]
peserta_2 = ["dedeh", 50, "wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]

print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")

