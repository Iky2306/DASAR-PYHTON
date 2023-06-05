## List

# kumpulan data numbers
data_angka = [1, 2, 3, 4]
print(data_angka)

# kumpulan data string
data_string = ["ucup", "otong", "odah"]
print(data_string)

# kumpulan data bolean
data_bolean = [True, False, True, True]
print(data_bolean)

# kumpulan data campuran
data_campuran = [1, "cireng", 2, "bala-bala", "ucup", True, "otong", False]
print(data_campuran)

## cara alternative membuat list
data_range = range(0, 10)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_pake_for = [i**2 for i in range(0, 10)]
print(list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i**2 for i in range(0, 10) if i % 2 == 0]  # gendap
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0, 10) if i % 2 != 0]  # ganjil
print(list_pake_for_if)
