# Latihan

# Kalkulator sederhana
print(20 * "=")
print("kalkulator sederhana")
print(20 * "=" + "\n")

angka_1 = float(input("Masukan angka 1 = "))
operator = input("Operator (+,-,x,/) : ")
angka_2 = float(input("Masukan angka 2 = "))

# Percabangan

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else:
    print("MAsukan yang bener dong")

print("Hasil dari program, terimakasiih")
