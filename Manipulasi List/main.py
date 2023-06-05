## operasi

data = ["ucup", "otong", "dudung"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir = {data_terakhir}")

data_ucup = data[-3]
print(f"data ucup =  {data_ucup}")

# mengambil info jumlah data
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

## manipulasi data list

# menambahkan item pada data list
print(f"data sebelum di tambah = \n{data}")

data.insert(1, "asep")
print(f"data yang di tambah = \n{data}")

# menambah data di akhir
data.append("jajang")
print(f"data di akhir = \n{data}")

# menambahkan list dengan list
data_baru = ["ujang", "usep", "dedeng"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# merubah data
data[2] = "michel"
print(f"data rubah = \n{data}")

# meremove data
data.remove("ujang")
print(f"data yang dihapus = \n{data}")

# meremove data paling belakang
data.pop()
print(f"data akhir = \n{data}")
