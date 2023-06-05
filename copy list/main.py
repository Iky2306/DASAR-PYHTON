## teknik menduplikat list

a = ["ucup", "otong", "dudung"]
print(f"a = {a}")

b = a
print(f"b = {b}")

# kita akan merubah member dari a

# ini akan merubah kedua list
a[1] = "mihcel"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# addres dari kedua list a dan b
print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")

# menduplikat list dengan menggunakan copy
print(f"membuat list C dengan a.copy()")
c = a.copy()  # full duplikat data baru

print(f"addres a = {hex(id(a))}")
print(f"addres b = {hex(id(b))}")
print(f"addres c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")
c[0] = "dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 1")
a[1] = "otong"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
