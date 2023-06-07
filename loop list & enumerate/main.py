# looping dari lsit

# for loop
print("for loop")
kumpulan_angka = [4, 3, 2, 5, 6, 1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")

peserta = ["ucup", "otong", "dadang", "diding", "dudung"]

for nama in peserta:
    print(f"nama = {nama}")

# for loop dan range
print("\nfor loop and range")
kumpulan_angka = [10, 5, 4, 2, 6]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"angka = {kumpulan_angka[i]}")

# while
print("\nwhile loop")
kumpulan_angka = [10, 5, 4, 2, 6]

panjang = len(kumpulan_angka)
i = 0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i += 1

# list comprehension
print("\nloop comprehension")
data = ["ucup", 1, 2, 3, "otong"]

[print(f"data={i}") for i in data]

# enumerate
print("\nloop enumerate")
data_list = ["ucup", 1, 2, 3, "otong"]

for index, data in enumerate(data_list):
    print(f"index = {index}, data={data}")
