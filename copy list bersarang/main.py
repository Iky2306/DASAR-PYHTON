data_0 = [1, 2]
data_1 = [3, 4]

data_2D = [data_0, data_1]
data_2D_copy = data_2D.copy()

print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# mengambil data list

data = data_2D[0][0]
print(f"data = {data}")

# addres semuanya

print(f"addres asli = {hex(id(data_2D))}")
print(f"addres copy = {hex(id(data_2D_copy))}")

print(f"addres dari member ke-1")
print(f"addres asli = {hex(id(data_2D[0]))}")
print(f"addres copy = {hex(id(data_2D_copy[0]))}")

data_2D[1][0] = 5
data_2D[0] = 9
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")

# kita gunakan deepcopy

from copy import deepcopy

data_2D = [data_0, data_1]
data_2D_deepcopy = deepcopy(data_2D)

print(f"addres asli = {hex(id(data_2D))}")
print(f"addres deep = {hex(id(data_2D_deepcopy))}")

print(f"addres dari member ke-1")
print(f"addres asli = {hex(id(data_2D[0]))}")
print(f"addres copy = {hex(id(data_2D_deepcopy[0]))}")

data_2D[1][0] = 30
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deep = {data_2D_deepcopy}")
